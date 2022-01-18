# speedLocator
Custom locator which shows the speed of moving objects in Autodesk Maya.

![speedLocator loaded in Maya](/images/speedLocatorStill2.png)

# Video Tutorial:
[![Watch the video](/images/introSlate.png)](https://vimeo.com/667222084)

# How to install:
https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2022/ENU/Maya-Customizing/files/GUID-FA51BD26-86F3-4F41-9486-2C3CF52B9E17-htm.html

### On windows copy the content of:
`speedLocator/plug-ins/windows/2022/*` to
`C:/Users/<username>/Documents/maya/2022/plug-ins`

`speedLocator/prefs/icons/*` to `C:/Users/<username>/Documents/maya/2022/prefs/icons`

`speedLocator/scripts/*` to `C:/Users/<username>/Documents/maya/scripts`

# How to use:
After loading the plugin in maya, type `speed` in the mel command line. Works with selection. You can as well provide a custom name with the -n flag. Some practical use examples:
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


# Release Notes:
```
Version 1.0.0

Initial release

```
