import maya.cmds as cmds
import maya.mel as mel
# H:\SFX\DrStrange_Portal (import functions)

# Declare functions   
def setNucleus( n ):
    # Physics prefs
    nucleusWindSpeed = 2.139
    nucleusWindNoise = 1
    
    # Physics
    cmds.setAttr( myNucleus + '.usePlane', 1 )
    cmds.setAttr( myNucleus + '.windSpeed', nucleusWindSpeed)
    cmds.setAttr( myNucleus + '.windDirectionX', 1)
    cmds.setAttr( myNucleus + '.windDirectionY', 1)
    cmds.setAttr( myNucleus + '.windDirectionZ', 1)
    cmds.setAttr( myNucleus + '.windNoise', nucleusWindNoise)
    #cmds.keyTangent( 'motionPath1_uValue', itt='linear', ott='linear', an='objects' )  

   
def setEmitter( e, p, pos ):
    # Keyframes prefs
    loops = 10
    time = 200
    
    # Keyframes
    cmds.move( 0,5,0, e )
    cmds.move( 0,-2,0, e + '.scalePivot', r=True )
    cmds.move( 0,-2,0, e + '.rotatePivot', r=True )
    
    cmds.setKeyframe( e + '.rotateX', v=pos, t=0 )
    cmds.setKeyframe( e + '.rotateX', v=pos+360*loops, t=time )
    cmds.setKeyframe( e + '.scaleY', v=0, t=0 )
    cmds.setKeyframe( e + '.scaleY', v=0.0, t=30 )
    cmds.setKeyframe( e + '.scaleY', v=0.2, t=50 )
    cmds.setKeyframe( e + '.scaleY', v=1, t=100 )
    cmds.setKeyframe( e + '.rate', v=500, t=0 )
    cmds.setKeyframe( e + '.rate', v=3000, t=100 )
    
    # Looks prefs
    particlesPerSec = 3000
    particlesSpeed = 1
    particlesSpread = 0.2
    particlesWeight = 0.04
    particlesLifespan = 1.5
    particlesLifespanRandom = 1.0
    particlesTailSize = 4
 
    # Looks
    cmds.setAttr( p + '.particleRenderType', 6 )
    cmds.setAttr( p + '.bounce', 1 )
    cmds.setAttr( p + '.color[1].color_Position', 1 )
    cmds.setAttr( p + '.color[0].color_Color', 1, 0.75, 0 )
    cmds.setAttr( p + '.color[1].color_Color', 1, 0.3259, 0 )
    #cmds.setAttr( p + '.aiRadiusMultiplier', 0.2 )
    cmds.setAttr( p + '.dynamicsWeight', particlesWeight )
    cmds.setAttr( p + '.lifespanMode', 2)
    cmds.setAttr( p + '.lifespan', particlesLifespan )
    cmds.setAttr( p + '.lifespanRandom', particlesLifespanRandom )
    cmds.setAttr( p + '.collide', 0 )
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


def createSampleEnvironment():
    cmds.CreatePolygonPlane()
    floor = 'pPlane1'
    cmds.setAttr( floor + '.scaleX', 30 )
    cmds.setAttr( floor + '.scaleZ', 30 )
    
    cmds.CreatePolygonPlane()
    wall1 = 'pPlane2'
    cmds.setAttr( wall1 + '.scaleX', 20 )
    cmds.setAttr( wall1 + '.scaleZ', 30 )
    cmds.setAttr( wall1 + '.rotateZ', 90 )
    cmds.setAttr( wall1 + '.translateX', -15 )
    cmds.setAttr( wall1 + '.translateY', 10 )
    
    cmds.CreatePolygonPlane()
    wall2 = 'pPlane3'
    cmds.setAttr( wall2 + '.scaleX', 30 )
    cmds.setAttr( wall2 + '.scaleZ', 20 )
    cmds.setAttr( wall2 + '.rotateX', 90 )
    cmds.setAttr( wall2 + '.translateZ', -15 )
    cmds.setAttr( wall2 + '.translateY', 10 )
    
    cmds.CreatePolygonCube()
    cube = 'pCube1'
    cmds.setAttr( cube + '.scale', 3, 3, 3 )
    cmds.setAttr( cube + '.translateY', 1.5 )
    cmds.setAttr( cube + '.translateX', -5 )
    cmds.setAttr( cube + '.translateZ', -3 )
    cmds.setAttr( cube + '.rotateY', 30 )


def moveCamera():
    cmds.setAttr('persp.translateX', 9 )
    cmds.setAttr('persp.translateY', 5 )
    cmds.setAttr('persp.translateZ', 2 )
    
    cmds.setAttr('persp.rotateX', -12 )
    cmds.setAttr('persp.rotateY', 77 )
    cmds.setAttr('persp.rotateZ', 0 )


# Clear scene
cmds.select(all=True)
cmds.delete()

# Setup new scene
# Setup environment
createSampleEnvironment()

# Move camera
moveCamera()

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
myGlow = ['pTorus1', 'polyTorus1']
setGlow( myGlow )
