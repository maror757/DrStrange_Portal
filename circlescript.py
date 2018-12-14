import maya.cmds as cmds
import maya.mel as mel
from random import random
# H:\SFX\DrStrange_Portal (import functions)

# Declare functions   
def setNucleus( n ):
    # Physics prefs
    #Old Version nucleusWindSpeed = 2.414
    nucleusWindSpeed = 5.414
    nucleusWindNoise = 1
    
    # Physics
    cmds.setAttr( myNucleus + '.usePlane', 1 )
    cmds.setAttr( myNucleus + '.windSpeed', nucleusWindSpeed)
    #Old Version cmds.setAttr( myNucleus + '.windDirectionX', 1)
    cmds.setAttr( myNucleus + '.windDirectionX', -1)
    cmds.setAttr( myNucleus + '.windDirectionY', 1)
    cmds.setAttr( myNucleus + '.windDirectionZ', 1)
    cmds.setAttr( myNucleus + '.windNoise', nucleusWindNoise)
    #cmds.keyTangent( 'motionPath1_uValue', itt='linear', ott='linear', an='objects' )  

   
def setEmitter( e, p, pos ):
    # Keyframes prefs
    loops = 10
    time = 300
    
    # Keyframes
    cmds.move( 0,5,0, e )
    cmds.move( 0,-2,0, e + '.scalePivot', r=True )
    cmds.move( 0,-2,0, e + '.rotatePivot', r=True )
    
    cmds.setKeyframe( e + '.rotateX', v=pos, t=0 )
    cmds.setKeyframe( e + '.rotateX', v=pos+360*loops, t=time, itt='linear', ott='linear' )
    cmds.setKeyframe( e + '.scaleY', v=0, t=0 )
    cmds.setKeyframe( e + '.scaleY', v=0.0, t=60 )
    cmds.setKeyframe( e + '.scaleY', v=0.2, t=100 )
    cmds.setKeyframe( e + '.scaleY', v=1, t=200 )
    cmds.setKeyframe( e + '.rate', v=500, t=0 )
    cmds.setKeyframe( e + '.rate', v=3000, t=200 )
    
    # Looks prefs
    particlesPerSec = 3000
    particlesSpeed = 1
    particlesSpread = 0.2
    particlesWeight = 0.04
    #OldVersion particlesLifespan = 1.5
    particlesLifespan = 1.0
    #OldVersion particlesLifespanRandom = 1.0
    particlesLifespanRandom = 2.0
    particlesTailSize = 4
 
    # Looks
    cmds.setAttr( p + '.particleRenderType', 6 )
    cmds.setAttr( p + '.bounce', 1 )
    cmds.setAttr( p + '.color[0].color_Color', 0, 0, 0 )
    cmds.setAttr( p + '.incandescence[1].incandescence_Position', 1 )
    cmds.setAttr( p + '.incandescence[0].incandescence_Color', 1, 0.75, 0 )
    cmds.setAttr( p + '.incandescence[1].incandescence_Color', 1, 0.492, 0 )
    cmds.setAttr( p + '.incandescence[1].incandescence_Interp', 1)
    cmds.setAttr( p + '.incandescenceInput', 1)
    #cmds.setAttr( p + '.aiRadiusMultiplier', 0.2 )
    cmds.setAttr( p + '.dynamicsWeight', particlesWeight )
    cmds.setAttr( p + '.lifespanMode', 2)
    cmds.setAttr( p + '.lifespan', particlesLifespan )
    cmds.setAttr( p + '.lifespanRandom', particlesLifespanRandom )
    cmds.setAttr( p + '.collide', 0 )
    #New addition  
    cmds.setAttr( p + '.pointMass', 3.4 )
    
    cmds.setAttr( e + '.rate', particlesPerSec )
    cmds.setAttr( e + '.emitterType', 0 )
    cmds.setAttr( e + '.directionX', 0 )
    cmds.setAttr( e + '.directionY', 0 )
    cmds.setAttr( e + '.directionZ', -1 )
    cmds.setAttr( e + '.speed', particlesSpeed )
    cmds.setAttr( e + '.spread', particlesSpread )  
    

def setGlow( g ):
    cmds.setAttr( g[1] + '.radius', 2 )
    cmds.setAttr( g[1] + '.sectionRadius', 0.01 )
    cmds.setAttr( g[1] + '.subdivisionsAxis', 40 )
    cmds.setAttr( g[1] + '.subdivisionsHeight', 10 )
    cmds.setAttr( g[0] + '.rotateZ', 90 )
    cmds.setAttr( g[0] + '.translateY', 3 )
    
    glow_material = cmds.shadingNode('lambert', asShader=True)
    cmds.select( g[0] )
    cmds.hyperShade( assign=glow_material )
    cmds.setAttr( glow_material + '.color', 1.0, 0.6, 0.1 )
    cmds.setAttr( glow_material + '.transparency', 0.2, 0.2, 0.2 )
    cmds.setAttr( glow_material + '.hideSource', True )
    cmds.setAttr( glow_material + '.glowIntensity', 0.0 )
    
    cmds.CreatePointLight()
    pLight = 'pointLight1'
    cmds.setAttr( pLight + '.translateY', 3 )
    cmds.setAttr( pLight + '.color', 0.48, 0.24, 0.0 )
    cmds.setAttr( pLight + '.intensity', 10 )
    cmds.setAttr( pLight + '.decayRate', 2 )
    
    # Keyframes prefs
    loops = 10
    time = 300
    
    # Keyframes
    cmds.setKeyframe( glow_material + '.glowIntensity', v=0.0, t=180 )
    cmds.setKeyframe( glow_material + '.glowIntensity', v=0.5, t=200 )
    
    cmds.setKeyframe( pLight + '.intensity', v=0 , t=0 )
    cmds.setKeyframe( pLight + '.intensity', v=4 , t=100 )
    cmds.setKeyframe( pLight + '.intensity', v=5 , t=110 )
    cmds.setKeyframe( pLight + '.intensity', v=3 , t=120 )
    cmds.setKeyframe( pLight + '.intensity', v=6 , t=130 )
    cmds.setKeyframe( pLight + '.intensity', v=4, t=140 )
    cmds.setKeyframe( pLight + '.intensity', v=9, t=150 )
    cmds.setKeyframe( pLight + '.intensity', v=5 , t=160 )
    cmds.setKeyframe( pLight + '.intensity', v=8 , t=170 )
    cmds.setKeyframe( pLight + '.intensity', v=7 , t=180 )
    cmds.setKeyframe( pLight + '.intensity', v=10 , t=190 )
    s = 200;
    
    for x in range(0, 10):
        cmds.setKeyframe( pLight + '.intensity', v=9+random() , t=s+x*10 )
        cmds.setKeyframe( pLight + '.intensity', v=5+random() , t=s+x*10+5 )

def setSun():
    cmds.CreateDirectionalLight()
    sun = 'directionalLight1'
    cmds.setAttr( sun + '.rotateX', -40 )
   
   
# Clear scene
cmds.select('emitter1')
cmds.select('nParticle1', add=True)
cmds.select('nucleus1', add=True)
cmds.select('emitter2', add=True)
cmds.select('nParticle2', add=True)
cmds.select('pTorus1', add=True)
cmds.select('directionalLight1', add=True)
cmds.select('pointLight1', add=True)
cmds.delete()

# Setup new scene
# Setup environment
#createSampleEnvironment()

# Setup particle system
cmds.NCreateEmitter()
cmds.NCreateEmitter()
myEmitter1 = 'emitter1'
myParticle1 = 'nParticle1'
myEmitter2 = 'emitter2'
myParticle2 = 'nParticle2'
myNucleus = 'nucleus1'
setNucleus( myNucleus )
setEmitter( myEmitter1, myParticle1, 0 )
setEmitter( myEmitter2, myParticle2, 180 )

# Setup glow
cmds.CreatePolygonTorus()
myGlow = ['pTorus1', 'polyTorus1', 'lambert1']
setGlow( myGlow )
# Setup sun
setSun()
