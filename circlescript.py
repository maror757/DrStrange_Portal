import maya.cmds as cmds
import maya.mel as mel
#import functions

# Clear scene
cmds.select(all=True)
cmds.delete()

# Setup new scene
cmds.NCreateEmitter()
cmds.NCreateEmitter()

myEmitter1 = 'emitter1'
myParticle1 = 'nParticle1'
myEmitter2 = 'emitter2'
myParticle2 = 'nParticle2'
myNucleus = 'nucleus1'

nucleusWindSpeed = 2.139
nucleusWindNoise = 1

cmds.setAttr( myNucleus + '.usePlane', 1 )
cmds.setAttr(myNucleus + '.windSpeed', nucleusWindSpeed)
cmds.setAttr(myNucleus + '.windDirectionX', 1)
cmds.setAttr(myNucleus + '.windDirectionY', 1)
cmds.setAttr(myNucleus + '.windDirectionZ', 1)
cmds.setAttr(myNucleus + '.windNoise', nucleusWindNoise)
#cmds.keyTangent( 'motionPath1_uValue', itt='linear', ott='linear', an='objects' )

# Scale kanske inte behövs??????????
cmds.move( 0,5,0, myEmitter1 )
cmds.move( 0,-2,0, myEmitter1 + '.scalePivot', r=True )
cmds.move( 0,-2,0, myEmitter1 + '.rotatePivot', r=True )
cmds.move( 0,5,0, myEmitter2 )
cmds.move( 0,-2,0, myEmitter2 + '.scalePivot', r=True )
cmds.move( 0,-2,0, myEmitter2 + '.rotatePivot', r=True )


def setEmitterPrefs( e, p ):
    # Prefs
    particlesPerSec = 3000
    particlesSpeed = 1
    particlesSpread = 0.2
    particlesWeight = 0.04
    particlesLifespan = 1.5
    particlesLifespanRandom = 1.0
    particlesTailSize = 4
 
    # Setting attr
    cmds.setAttr( p + '.particleRenderType', 6 )
    cmds.setAttr( p + '.bounce', 1 )
    cmds.setAttr( p + '.color[1].color_Position', 1 )
    cmds.setAttr( p + '.color[0].color_Color', 1, 0.75, 0 )
    cmds.setAttr( p + '.color[1].color_Color', 1, 0.3259, 0 )
    # Varför fungerar inte tailSize?
    cmds.addAttr( p, ln='colorAccum' )
    cmds.addAttr( p, ln='useLighting' )
    cmds.addAttr( p, ln='lineWidth' )
    cmds.addAttr( p, ln='tailFade' )
    cmds.addAttr( p, ln='tailSize')
    cmds.addAttr( p, ln='normalDir' )
  
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
    
    
def setEmitterKeyframes( e, pos ):
    # Prefs
    loops = 10
    time = 200
    
    cmds.setKeyframe( e + '.rotateX', v=pos, t=0 )
    cmds.setKeyframe( e + '.rotateX', v=pos+360*loops, t=time )
    cmds.setKeyframe( e + '.scaleY', v=0, t=0 )
    cmds.setKeyframe( e + '.scaleY', v=0.0, t=30 )
    cmds.setKeyframe( e + '.scaleY', v=0.2, t=50 )
    cmds.setKeyframe( e + '.scaleY', v=1, t=100 )
    cmds.setKeyframe( e + '.rate', v=500, t=0 )
    cmds.setKeyframe( e + '.rate', v=3000, t=100 )


setEmitterPrefs( myEmitter1, myParticle1 )
setEmitterPrefs( myEmitter2, myParticle2 )

setEmitterKeyframes( myEmitter1, 0 )
setEmitterKeyframes( myEmitter2, 180 )

