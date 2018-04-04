from matplotlib.pyplot import imsave

from renderer.shapes import Sphere, Plane
from renderer.light import Light
from renderer.camera import Camera
from renderer.scene import Scene
from renderer.material import Material
from renderer.mathlib import Vector
from renderer.raytracer import Raytracer

red = Material('red', .8, .1, .1, .25)
green = Material('green', .5, .9, .1, .25)
blue = Material('blue', .1, .4, .8, .25)
white = Material('white', 1.0, 1.0, 1.0, 0.9)

shapes = [
    Sphere(-.5, 0., -2., .75, red),
    Sphere(1., 0., -2., .5, blue),
    Sphere(-.5, -.25, -1.25, .8, green),
    Plane(Vector(0.0, -0.5, 0.0), Vector(0.0, 1.0, 0.0), white)
]

lights = [
    Light(0., 2, -2., 0.75),
    Light(0., .5, -1., 0.75)
]

camera = Camera(0, 0, -.5, ray_depth=4, width=600, height=600)

scene = Scene(shapes, lights, camera)

raytracer = Raytracer(scene)

image = raytracer.render(subsamples=0)

imsave(image, 'render.png')

