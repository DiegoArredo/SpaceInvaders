import os
import sys

import numpy as np
from pyglet import clock
from pyglet.app import run
from pyglet.gl import *  # type: ignore
from pyglet.window import Window, key

from invaders import *
from utils import shapes
from utils.drawables import Model
from utils.scene_graph import SceneGraph

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


class Controller(Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # =========== Idealmente no modificar, usen estas variables globales ===========
        self.time = 0

        # Teclas de movimiento
        self.left = False
        self.right = False

        # Cámara actual
        self.camera_mode = 0

        # constantes en todo el programa
        # deben inicializarse
        self.pipeline = None
        self.atlas = None


        # listas de objetos
        self.enemies = []
        self.bullets = []

        #Contador de balas puede serle útil
        self.bullet_counter = 0

        # Variable de dirección puede serle útil
        self.direction = 1

        #variable para pausa
        self.paused = False

        #variable para el dt
        self.dt = 0

        # variable para el toggle de la luz
        self.light = True

if __name__ == "__main__":

    controller = Controller( 800, 600, "Space Invaders" )
    controller.set_exclusive_mouse(True)

    # La siguiente función inicializa el controlador y viene dada!
    init_controller(controller)


    # ============================ COMPLETAR DESDE AQUÍ ============================

    # Se definen dos cámaras inicialmente iguales
    ship_camera = MyCam(np.array([0, 2.2, 12.0]))
    ship_camera.pitch = 0

    top_camera = MyCam(np.array([0, 15, -3]))
    top_camera.pitch = -np.pi / 2 + 0.01 # type: ignore


    # A continuación declare las geometrías usando la clase "Model"
    # Necesitará una geometría para la nave y una para las balas
    uv_ship = get_atlas_uv(xoffset=2,yoffset=1, atlas=controller.atlas)
    ship_mesh = Model(
        shapes.Cube["position"],
        uv_ship * 6,
        index_data=shapes.Cube["indices"],
        normal_data=shapes.Cube["normal"]
    )

    # Ojo con esta geometría pues se utiliza por la función "shoot"
    uv_bullet = get_atlas_uv(xoffset=2,yoffset=0, atlas=controller.atlas)
    bullet_mesh = Model(
        shapes.Cube["position"],
        uv_bullet * 6,
        index_data=shapes.Cube["indices"],
        normal_data=shapes.Cube["normal"]
    )

    
    # El grafo de escena a usar, con su cámara por defecto
    world = SceneGraph(ship_camera)

    # Se agrega el nodo de la nave y nodo padre de las balas
    # luego utilice la función auxiliar "init_enemies" para los enemigos
    world.add_node(
        "ship",
        mesh=ship_mesh,
        texture=controller.atlas,
        pipeline=controller.pipeline
    )

    world.add_node(
        "bullets",
        mesh=None,
        texture=None,
        pipeline=controller.pipeline
    )

    world["ship"]["position"] = [0.0, 0.5, 10.0]
    world["ship"]["scale"] = [1.0, 0.5, 1.0]
    

    init_enemies(world, controller)
    world.update()
    # ============================= NO MODIFICAR on_key_press ============================
    @controller.event
    def on_key_press(symbol, modifiers):

        #Key presses para pausar "p"
        if symbol == key.P:
            controller.paused = not controller.paused

        #Key presses para toggle de luz "f"
        if symbol == key.F:
            controller.light = not controller.light

        if symbol == key.A or symbol == key.LEFT:
            controller.left = True

        if symbol == key.D or symbol == key.RIGHT:
            controller.right = True

        if symbol == key.SPACE and not controller.paused:
            shoot(world["ship"]["position"], world, bullet_mesh, controller)

        if symbol == key.C:

            if controller.camera_mode == 0:
                world.camera = ship_camera
                controller.camera_mode = 1

            else:
                world.camera = top_camera
                controller.camera_mode = 0

    # ============================ NO MODIFICAR on_key_release ============================
    @controller.event
    def on_key_release(symbol, modifiers):

        if symbol == key.A or symbol == key.LEFT:
            controller.left = False

        if symbol == key.D or symbol == key.RIGHT:
            controller.right = False


    # ============================ COMPLETAR update() ============================
    def update(dt):
        if controller.paused:
            return

        controller.time += dt
        controller.dt = dt
        
        # Debe utilizar las funciones auxiliares de update aquí
        update_ship(world, controller)
        update_enemies(world, controller)
        update_bullets(world, controller)
        update_camera(ship_camera, dt, world)  

        #posicion nave para el fragment shader
        controller.pipeline["u_shipPos"] = world["ship"]["position"]
        #toggle de luz para el fragment shader
        controller.pipeline["u_toggleLight"] = controller.light

        world.update()


    # ============================ on_draw()============================
    @controller.event
    def on_draw():

        controller.clear()

        glClearColor(0.1,0.1,0.15,1)

        glEnable(GL_DEPTH_TEST)

        glEnable(GL_BLEND)

        glBlendFunc(
            GL_SRC_ALPHA,
            GL_ONE_MINUS_SRC_ALPHA
        )
        world.draw()

    clock.schedule_interval(
        update,
        1 / 60
    )

    run()
