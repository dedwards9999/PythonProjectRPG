
from ursina import *

#ursina.application.development_mode = False
def update():
    #firstEntity.rotation_y += 10 * time.dt
    firstEntity.position += firstEntity.forward * time.dt
app = Ursina()
firstEntity = Entity(model='cube',
                     color=color.red,
                     texture='brick',
                     position=(0,0,0,),
                     rotation=(0,0,0),
                     scale=(3,5,3)
                     )
EditorCamera()
app.run()

