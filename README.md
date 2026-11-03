# 👾 Tarea 02: Space Invaders

Proyecto desarrollado para el ramo **CC3501 - Modelacion y Computacion Grafica para Ingenieros**.

Este repositorio contiene una aproximacion minima y simplificada a algunos elementos de *Space Invaders*. No busca recrear el juego completo, sino explorar sus componentes fundamentales, como una nave, enemigos, disparos, movimiento, colisiones e iluminacion.

La implementacion fue realizada utilizando Python, OpenGL, shaders y un grafo de escena, sin depender de un motor de videojuegos.

## 🎯 Objetivo

Aplicar conceptos de computacion grafica mediante la construccion de una escena interactiva en 3D. La tarea permite trabajar con:

- manejo de una escena y sus objetos;
- transformaciones y movimiento en el espacio;
- texturas y atlas de sprites;
- deteccion de colisiones;
- camaras interactivas;
- shaders e iluminacion mediante un foco y una luz direccional.

## 🚀 Como ejecutar el programa

Se necesita tener instalado [uv](https://docs.astral.sh/uv/). Desde la carpeta raiz del proyecto, ejecutar:

```bash
uv run tarea2.py
```

`uv` instala y utiliza las dependencias declaradas en `pyproject.toml`. El programa abre una ventana con la escena del juego.

## 🎮 Controles

- `A` o `Flecha izquierda`: mover la nave hacia la izquierda. ◀️
- `D` o `Flecha derecha`: mover la nave hacia la derecha. ▶️
- `SPACE`: disparar una bala. 💥
- `C`: alternar entre la camara que sigue a la nave y la camara superior. 📷

## 📋 Elementos solicitados en la tarea

El enunciado solicita, principalmente:

1. Implementar una nave 🚀 y grupos de enemigos 👾 con texturas.
2. Incorporar movimiento, dos camaras, disparos 💥 y colisiones.
3. Hacer que los enemigos se desplacen en conjunto y avancen hacia la nave.
4. Agregar iluminacion general y un foco proyectado desde la nave. 🔦

## 🧠 Resultados y aprendizajes

Esta seccion se completara posteriormente con los resultados obtenidos y los principales aprendizajes del desarrollo.

<small><em>README elaborado con la ayuda de GitHub Copilot.</em></small>
