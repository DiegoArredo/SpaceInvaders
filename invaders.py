import os

import numpy as np
from pyglet.gl import * #type: ignore

from utils import shapes
from utils.camera import FreeCamera
from utils.drawables import Model, Texture
from utils.helpers import init_pipeline
# ============================ COMPLETAR a continuación ============================

# init_enemies recibe un grafo de escena y el controlador
# Esta función no entrega nada pero agrega a los enemigos en
# sus posiciones iniciales al grafo de escena y al controlador

def init_enemies(world, controller):
    # CONSIDERACIONES:
    # - Recuerde que deben existir al menos dos tipos de enemigos distintos,
    #   estos se diferenciarán por su textura.
    # - Los enemigos deben estar organizados en filas y columnas como se muestra en el enunciado
    # - Para la geometría puede utilizar un cubo, como el que está en el archivo shapes @aux6!
    # - Puede utilizar la función vista en el auxiliar get_atlas_uv()!
    # - Se le recomienda mantener una lista de los enemigos en el controlador, para mantener sus nombres, su posicion y su estado (alive/dead)

    #uvs
    uv_white_enemy = get_atlas_uv(xoffset=0,yoffset=1, atlas=controller.atlas)
    uv_red_enemy = get_atlas_uv(xoffset=1,yoffset=0, atlas=controller.atlas)
    uv_yellow_enemy = get_atlas_uv(xoffset=1,yoffset=1, atlas=controller.atlas)
    uv_green_enemy = get_atlas_uv(xoffset=0,yoffset=0, atlas=controller.atlas)
    
    #meshs
    white_enemy_mesh = Model(
            shapes.Cube["position"],
            uv_white_enemy * 6,
            index_data=shapes.Cube["indices"],
            normal_data=shapes.Cube["normal"]
        )
    
    red_enemy_mesh = Model(
            shapes.Cube["position"],
            uv_red_enemy * 6,
            index_data=shapes.Cube["indices"],
            normal_data=shapes.Cube["normal"]
        )
    
    yellow_enemy_mesh = Model(
            shapes.Cube["position"],
            uv_yellow_enemy * 6,
            index_data=shapes.Cube["indices"],
            normal_data=shapes.Cube["normal"]
        )
    
    green_enemy_mesh = Model(
            shapes.Cube["position"],
            uv_green_enemy * 6,
            index_data=shapes.Cube["indices"],
            normal_data=shapes.Cube["normal"]
        )

    #agregar enemigos como un nodo a world
    world.add_node(
        "enemies",
        mesh=None,
        texture=None,
        pipeline=controller.pipeline
    )

    for i in range(7):
        #red_enemies
        world.add_node(
            attach_to="enemies",    
            name=f"red_enemy_{i}",
            mesh=red_enemy_mesh,
            texture=controller.atlas,
            pipeline=controller.pipeline
        )
        world[f"red_enemy_{i}"]["position"] = [i*2-6, 0, -6]
        controller.enemies.append({
            "name": f"red_enemy_{i}",
            "position": [i*2-6, 0, -6],
            "alive": True
        })
        #white_enemies
        world.add_node(
            attach_to="enemies",
            name=f"white_enemy_{i}",
            mesh=white_enemy_mesh,
            texture=controller.atlas,
            pipeline=controller.pipeline
        )
        world[f"white_enemy_{i}"]["position"] = [i*2-6, 0, -4]
        controller.enemies.append({
            "name": f"white_enemy_{i}",
            "position": [i*2-6, 0, -4],
            "alive": True
        })
        #green_enemies
        world.add_node(
            attach_to="enemies",
            name=f"green_enemy_{i}",
            mesh=green_enemy_mesh,
            texture=controller.atlas,
            pipeline=controller.pipeline
        )
        world[f"green_enemy_{i}"]["position"] = [i*2-6, 0, -2]
        controller.enemies.append({
            "name": f"green_enemy_{i}",
            "position": [i*2-6, 0, -2],
            "alive": True
        })
        #yellow_enemies
        world.add_node(
            attach_to="enemies",
            name=f"yellow_enemy_{i}",
            mesh=yellow_enemy_mesh,
            texture=controller.atlas,
            pipeline=controller.pipeline
        )
        world[f"yellow_enemy_{i}"]["position"] = [i*2-6, 0, 0]
        controller.enemies.append({
            "name": f"yellow_enemy_{i}",
            "position": [i*2-6, 0, 0],
            "alive": True
        })

    




# shoot recibe la posicion de la nave, un grafo de escena, la geometría de una bala y el controlador
# Esta función es llamada cuando el usuario presiona SPACE (vea el archivo principal para corroborarlo)
# En esta función se debe crear una bala en la posición de la cámara y agregarla al grafo de escena y el controlador
def shoot(ship_position, world, bullet_mesh, controller):
    # CONSIDERACIONES
    # - Se le recomienda mantener una lista "bullets" en el controlador con las balas para mantener los nombres de las balas, su posicion y su estado (alive/dead)
    
    #Visual
    world.add_node(
        attach_to="bullets",
        name=f"bullet_{controller.bullet_counter}",
        mesh=bullet_mesh,
        texture=controller.atlas,
        pipeline=controller.pipeline
    )
    world[f"bullet_{controller.bullet_counter}"]["position"] = ship_position
    world[f"bullet_{controller.bullet_counter}"]["scale"] = [0.25, 0.25, 0.5]

    #Controller
    controller.bullets.append({
        "name": f"bullet_{controller.bullet_counter}",
        "position": ship_position,
        "alive": True
    })

    controller.bullet_counter += 1
    




# update_ship recibe el grafo de escena y el controlador
# Esta función se llamará en cada frame y debe actualizar la posición de la nave de acuerdo al input del usuario
def update_ship(world, controller):
    # CONSIDERACIONES
    # - Utilice las variables booleanas controller.left y controller.right estas indican cuando se presionan las teclas
    # - Recuerde las limitantes del movimiento de la nave indicadas en el enunciado
    
    if controller.left:
        world["ship"]["position"][0] = np.clip(world["ship"]["position"][0] - 0.1, -6.0, 6.0)

    if controller.right:
        world["ship"]["position"][0] = np.clip(world["ship"]["position"][0] + 0.1, -6.0, 6.0)

  




# update_enemies recibe un grafo de escena y un controlador
# Esta función se llamará en cada frame y debe actualizar la posicion de los enemigos vivos
# Debe reproducir el movimiento demostrado en el enunciado
def update_enemies(world, controller):
    # CONSIDERACION
    # - Se le recomienda actualizar primero la lista en el controlador y luego copiar eso al grafo de escena!
    # - Se deberá imitar el movimiento indicado en el enunciado

    pass




# update_bullets recibe un grafo de escena y el controlador
# Esta función se llamará en cada frame y actualiza la posición y el estado de las balas vivas
# Además revisa si una bala ha colisionado con un enemigo, actualizando la bala y el enemigo
def update_bullets(world, controller):
    # CONSIDERACIONES
    # - Se le recomienda separar el movimiento de la bala de la detección de colisión para mayor claridad
    # - Se le recomienda actualizar primero las listas en el controlador y luego el grafo de escena
    # - Puede utilizar la función dada "check_collision" que recibe una bala y un enemigo (revise el formato en que recibe)
    # - Encuentre una forma de "eliminar" las balas y enemigos muertos, hay varias formas...

    for bullet in controller.bullets:
        bullet["position"]= bullet["position"] + np.array([0, 0, -0.2])
        world[bullet["name"]]["position"] = bullet["position"]




# update_camera recibe un objeto cámara, el timepo entre frames (dt) y un grafo de escena
# Esta función se llama en cada frame y actualiza la posición de la cámara en función de la posición de la nave
def update_camera(ship_camera, dt, world):
    if world.camera is ship_camera:
        ship_position = world["ship"]["position"]
        ship_camera.position = ship_position + np.array([0, 2, 2.3])
    world.camera.time_update(dt)








# ============================ FUNCIONES DADAS ============================

# init_controller recibe un controlador e inicializa el pipeline y el atlas de texturas
# aquí se indica cual es la imagen que se usa de textura
def init_controller(controller):

    root = os.path.dirname(__file__)
    controller.pipeline = init_pipeline(root + "/tarea2.vert", root + "/tarea2.frag")
    controller.atlas = Texture(
        root + "/atlas.png",
        minFilterMode=GL_NEAREST,
        maxFilterMode=GL_NEAREST
    )

# get_atlas_uv recibe las coordenadas de una textura y un objeto Texture con la textura en cuestión
# entrega las coordenadas uv correspondientes a las coordenadas dadas, en la textura dada
def get_atlas_uv(xoffset, yoffset, atlas):

    # Para imagenes con objetos de 16x16
    sizex = 11
    sizey = 8

    deltax = sizex / atlas.width
    deltay = sizey / atlas.height

    return [
        deltax * xoffset,
        deltay * yoffset,

        deltax * (xoffset + 1),
        deltay * yoffset,

        deltax * (xoffset + 1),
        deltay * (yoffset + 1),

        deltax * xoffset,
        deltay * (yoffset + 1)
    ]


class MyCam(FreeCamera):
    def __init__(self, position=np.array([0, 0, 0]), camera_type="perspective"):
        super().__init__(position, camera_type)
        self.direction = np.array([0,0,0])
        self.speed = 2

    def time_update(self, dt):
        self.update()
        dir = self.direction[0]*self.forward + self.direction[1]*self.right
        dir_norm = np.linalg.norm(dir)
        if dir_norm:
            dir /= dir_norm
        self.position += dir*self.speed*dt
        self.focus = self.position + self.forward




# check_collision recibe una bala y un enemigo
# entrega un valor booleano indicando si los dos objetos se encuentran colisionando
# IMPORTANTE: bullet y enemy DEBEN ser diccionarios y tener al menos un campo "position".
# Por ejemplo:
# {
# "position" : [2, 3, 4],
# "name" : "enemy 1",
# "alive" : True
# }
def check_collision(bullet, enemy):

    bx, by, bz = bullet["position"]
    ex, ey, ez = enemy["position"]

    bw, bh, bd = [0.5, 0.5, 0.5]
    ew, eh, ed = [0.8, 0.8, 0.8]

    bullet_min_x = bx - bw / 2
    bullet_max_x = bx + bw / 2

    bullet_min_y = by - bh / 2
    bullet_max_y = by + bh / 2

    bullet_min_z = bz - bd / 2
    bullet_max_z = bz + bd / 2

    enemy_min_x = ex - ew / 2
    enemy_max_x = ex + ew / 2

    enemy_min_y = ey - eh / 2
    enemy_max_y = ey + eh / 2

    enemy_min_z = ez - ed / 2
    enemy_max_z = ez + ed / 2

    collision_x = (
        bullet_min_x <= enemy_max_x and
        bullet_max_x >= enemy_min_x
    )

    collision_y = (
        bullet_min_y <= enemy_max_y and
        bullet_max_y >= enemy_min_y
    )

    collision_z = (
        bullet_min_z <= enemy_max_z and
        bullet_max_z >= enemy_min_z
    )

    return collision_x and collision_y and collision_z
