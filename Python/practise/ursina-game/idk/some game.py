from ursina import *

app = Ursina()
WIDTH = 800
HEIGHT = 600
DEFAULT_TICK = .03
VERTICAL_MVMNT_REDUCER = 2
MOUSE_SENSITIVITY = 50
mouse.locked = True

cube = Entity(model="cube",
              scale=(1, 1, 1),
              texture="crate",
              x=0, y=1, z=0
              )


floor = Entity(model="cube",
               scale=(20, 1, 20),
               x=0, y=-0, z=0,
               collider="box",
               collision=True,
               texture="floor"
               )

crosshair = Entity(model="cube",
                   scale=.007,
                   rotation_z=45,
                   parent=camera.ui,
                   color=color.blue
                   )

Sky = Sky()


def window_setup(W, H):
    window.title = "Game"
    window.borderless = False
    window.fullscreen = False
    window.exit_button.visible = False
    window.fps_counter.enabled = True
    window.size = (W, H)


def FPC(entity):
    global TICK
    if held_keys["left control"]:
        TICK = DEFAULT_TICK * 1.5
    else:
        TICK = DEFAULT_TICK
    if held_keys["r"]:
        cube.rotation_y += time.dt * 100


    camera.position = Vec3(entity.x, entity.y + 5, entity.z)
    entity.direction = Vec3(
        entity.forward * (held_keys['w'] - held_keys['s']) * TICK +
        entity.right * (held_keys['d'] - held_keys['a']) * TICK
    )
    entity.position += entity.direction

    entity.y += (held_keys['space'] - held_keys["shift"]) * \
                (TICK / VERTICAL_MVMNT_REDUCER)
    camera.rotation_y += mouse.velocity[0] * MOUSE_SENSITIVITY
    camera.rotation_x -= mouse.velocity[1] * MOUSE_SENSITIVITY
    camera.rotation_x = clamp(camera.rotation_x, -90, 90)
    entity.rotation_y = camera.rotation_y



def update():
    FPC(player)
    window.fps_counter.enabled = True

player = Entity(colider="box",
                collision=True
                )

window_setup(WIDTH, HEIGHT)
update()

app.run()
