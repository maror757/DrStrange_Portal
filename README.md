# DrStrange Portal
Python script for creating the Doctor Strange portal effect in Maya

### Arnold Renderer (for Maya 2017)
Make these changes in Maya
* Render Settings >> Arnold Renderer >> Motion Blur >> Enable
* Arnold >> Lights >> Skydome Lights

### Mental Ray Renderer (for Maya 2016)
* Render Settings >> Presets >> Load Presets >> Production
To remove shadows from nParticles
* Windows >> Relationship Editors >> Light Linking >> Light-Centric ... Remove nParticles from pointLight
Not done in the Python script
* nParticles tailsize

### Links
* https://help.autodesk.com/cloudhelp/2018/CHS/Maya-Tech-Docs/CommandsPython/index.html
* https://www.turbosquid.com/Search/3D-Models/free (free meshed)
* https://www.youtube.com/watch?v=FLCwZs-EKJE

* https://www.youtube.com/watch?v=rX-Xmr-v57k
* https://www.youtube.com/watch?v=3JwUNmw0rQQ

### Todo
* Mer flimmer
* Keyframes till glown
* Högre FPS
* Rendera med "rätt" inställningar
