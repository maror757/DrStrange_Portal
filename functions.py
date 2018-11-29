def setEmitterPrefs( e, p, pos ):
    # Prefs
    loops = 10
    particlesPerSec = 3000
    particlesSpeed = 1
    particlesSpread = 0.2
    particlesWeight = 0.04
    particlesLifespan = 1.5
    particlesLifespanRandom = 1.0
    particlesTailSize = 4
    time = 200
 
  
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
    
    
def setEmitterKeyframes(e):
    cmds.setKeyframe( e + '.rotateX', v=pos, t=0 )
    cmds.setKeyframe( e + '.rotateX', v=pos+360*loops, t=time )
    cmds.setKeyframe( e + '.scaleY', v=0, t=0 )
    cmds.setKeyframe( e + '.scaleY', v=0.0, t=30 )
    cmds.setKeyframe( e + '.scaleY', v=0.2, t=50 )
    cmds.setKeyframe( e + '.scaleY', v=1, t=100 )
    cmds.setKeyframe( e + '.rate', v=500, t=0 )
    cmds.setKeyframe( e + '.rate', v=3000, t=100 )