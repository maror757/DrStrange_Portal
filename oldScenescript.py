def createSampleEnvironment():
    cmds.CreatePolygonPlane()
    floor = 'pPlane1'
    cmds.setAttr( floor + '.scaleX', 30 )
    cmds.setAttr( floor + '.scaleZ', 30 )
    floor_material = cmds.shadingNode('lambert', asShader=True)
    cmds.select( floor )
    cmds.hyperShade( assign=floor_material )
    cmds.setAttr( floor_material + '.color', 0.6, 0.4, 0.3 )
    
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
    wall_material = cmds.shadingNode('lambert', asShader=True)
    cmds.select( wall1 )
    cmds.hyperShade( assign=wall_material )
    cmds.select( wall2 )
    cmds.hyperShade( assign=wall_material )
    cmds.setAttr( wall_material + '.color', 0.1, 0.6, 0.5 )
    
    cmds.CreatePolygonCube()
    cube = 'pCube1'
    cmds.setAttr( cube + '.scale', 3, 3, 3 )
    cmds.setAttr( cube + '.translateY', 1.5 )
    cmds.setAttr( cube + '.translateX', -5 )
    cmds.setAttr( cube + '.translateZ', -3 )
    cmds.setAttr( cube + '.rotateY', 30 )
    cube_material = cmds.shadingNode('lambert', asShader=True)
    cmds.select( cube )
    cmds.hyperShade( assign=cube_material )
    cmds.setAttr( cube_material + '.color', 1.0, 0.1, 0.1 )
    
    cmds.CreatePointLight()
    light = 'pointLight1'
    cmds.setAttr( light + '.translateX', 20 )
    cmds.setAttr( light + '.translateY', 20 )
    cmds.setAttr( light + '.translateZ', -10 )