"""Requires Python 3"""

# General imports 
import os, sys, shutil

# Third-Party imports
from PySide2 import QtCore
import maya.cmds as cmds
from maya.app.startup import basic
import maya.utils



# Base path definitions
MODULENAME = "speedLocator"
DRAGGEDFROMPATH = os.path.dirname(__file__)
DEFAULTMODULEPATH = f"{os.environ['MAYA_APP_DIR']}/modules"
DEFAULTSCRIPTSPATH = f"{os.environ['MAYA_APP_DIR']}/scripts"
# Custom module path definitions
MODULESCRIPTSPATH = f"{DEFAULTMODULEPATH}/{MODULENAME}/scripts"
# List of required files to install
INSTALLATIONPACKAGE = [
	f"{DRAGGEDFROMPATH}/{MODULENAME}/plug-ins/windows/2022/{MODULENAME}.mll",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/plug-ins/windows/2020/{MODULENAME}.mll",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/plug-ins/linux/2022/{MODULENAME}.so",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/scripts/AE{MODULENAME}Template.mel",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/scripts/userSetup.py",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/icons/{MODULENAME}.png",
	f"{DRAGGEDFROMPATH}/{MODULENAME}/icons/out_{MODULENAME}.png",
	f"{DRAGGEDFROMPATH}/{MODULENAME}.mod"
]

def validatePythonVersion():
	"""Python required version validation function."""
	if os.environ['MAYA_PYTHON_VERSION'] == "2":
		raise RuntimeError("Drag and drop installer requires Python 3, aborting installation!")

def _validateInstallationFiles():
	"""Checks if all required installation files exist in source."""
	missingFilesList = []
	for pkg in INSTALLATIONPACKAGE:
		if not QtCore.QFileInfo(pkg).exists():
			missingFilesList.append(pkg)
	
	if missingFilesList:
		raise RuntimeError(
			f"Installation package reported missing files: {missingFilesList}, aborting!"
		)

def _removePreviousModule():
	installationDestination = QtCore.QDir(f"{DEFAULTMODULEPATH}/{MODULENAME}")
	if installationDestination.exists():
		installationDestination.removeRecursively()

	previousModFile = QtCore.QFile(f"{DEFAULTMODULEPATH}/{MODULENAME}.mod")
	if previousModFile.exists():
		previousModFile.remove()

def _createDirsForCopying():
	"""TODO: Create a proper recrusive functrion for copying files over - temp workaround
	but at least we don't have to deal with '\\' '/' slashes
	"""
	modulePath = QtCore.QDir(DEFAULTMODULEPATH)
	modulePath.mkpath(f"{MODULENAME}/plug-ins/windows/2022/")
	modulePath.mkpath(f"{MODULENAME}/plug-ins/windows/2020/")
	modulePath.mkpath(f"{MODULENAME}/plug-ins/linux/2020/")
	modulePath.mkpath(f"{MODULENAME}/scripts/")
	modulePath.mkpath(f"{MODULENAME}/icons/")

def clearMemory():
	"""Clean the current sys.path and sys.modules from anything to do with MODULENAME."""
	pathsList = sys.path[:]
	for index, path in enumerate(pathsList[::-1]):
		if MODULENAME in path.lower():
			sys.path.remove(path)

	for module in list(sys.modules):
		if MODULENAME in module:
			del sys.modules[module]

def createDialog(message="Default Message", title="Default Title",	icon="question",
		buttons=["Install", "Cancel"], cancelButton="Cancel") -> str:
	"""Convinience wrapper method for creating confirmDialogs."""
	return(cmds.confirmDialog(
		title=title,
		message=message,
		icon=icon,
		button=buttons,
		cancelButton=cancelButton,
		dismissString=cancelButton
	))

def _finalizeInstallation():
	"""Performs final installation procedures."""
	clearMemory()
	
	# Add path if its not already there
	if not MODULESCRIPTSPATH in sys.path:
		sys.path.append(MODULESCRIPTSPATH)

	# Reload all the modules
	cmds.loadModule(scan=True)
	cmds.loadModule(allModules=True)

	# Reload userSetup files
	basic.executeUserSetup()

def onMayaDroppedPythonFile(*args, **kwargs):
	"""Main function that runs when dragging the file into Maya.

	Installation is performed by copying the module to the user preferences and creating
	a module file.

	"""
	validatePythonVersion()

	_validateInstallationFiles()

	# Create install dialog
	input = createDialog(
		message=f"This will install SpeedLocator in:\n{DEFAULTMODULEPATH}",
		title="SpeedLocator Installer"
	)

	if input == "Cancel":  # Installation was cancelled
		raise RuntimeError("Installation of SpeedLocator has been cancelled!")
	else:  # Installation continues
		_createDirsForCopying()

		finished = False
		for pkg in INSTALLATIONPACKAGE:
			pkgQt = QtCore.QFile(pkg)
			finished = pkgQt.copy(pkg.replace(DRAGGEDFROMPATH, DEFAULTMODULEPATH))

		if finished:
			_finalizeInstallation()
