P# speedLocator
SpeedLocator is a user-defined MPxLocatorNode which shows the speed of moving objects in Autodesk Maya.

![speedLocator loaded in Maya](/images/speedLocatorStill2.png)



# Video Tutorial:
[![Watch the video](/images/introSlate.png)](https://vimeo.com/667222084)



# How to install:

### Automated installation: (Requires Maya 2022 with Python 3.7)
1. Unzip the archive.
2. Drag and drop the "dragDropInstaller.py" into the Maya 3d viewport.
3. Follow the steps on screen.

### Manual installation:
1. Close all running instances of Maya.
2. Go to your Maya modules directory (create the "modules" folder if it does not exist):
```
(Windows) /Users/<username>/Documents/maya/modules/
(Mac OS X) $HOME/Library/Preferences/Autodesk/maya/modules/
(Linux)	$HOME/maya/modules/
```
3. Copy the "speedLocator" folder and "speedLocator.mod" file in the modules folder.

![speedLocator loaded in Maya](/images/speedLocatorManualInstallation.png)

4. Start Maya, the module will be loaded and the console should print out:
```
// Successfully imported plugin module 'speedLocator' v.X.X.X //
```



# How to use:
After loading the plugin in Maya, type `speed` in the mel command line. Works with selection. You can as well provide a custom name with the -n flag. Some practical use examples:
#### Mel:
```
speed;
speed "pCube1";
speed -n "speedometer";
```
#### Python:
```
from maya import cmds

cmds.speed()
cmds.speed("pCube1")
cmds.speed(n="speedometer")
```


# Supported Maya versions and platforms:
```
Windows: Maya 2022, 2020
Linux:   Maya 2022
MacOS:   Coming Soon
```

# Release Notes:
```
Version 1.0.0

Initial release
```
