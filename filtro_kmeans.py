from PIL import Image
import numpy as np
import random
from funciones import *

imagen = Image.open("../Trabajo-Pr-ctico-N-2-Pensamiento-Computacional-/test_images/sunrise.bmp")
canal_rojo, canal_verde, canal_azul = dividir_canales(imagen)
w, h = imagen.size

datos_canal_rojo = np.array(canal_rojo)
datos_canal_verde = np.array(canal_verde)
datos_canal_azul = np.array(canal_azul)

k = 8
k_coordenadas = []
k_colores = []

for coordenada in range(k):
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)
    k_coordenadas.append((x, y))
    r = datos_canal_rojo[y, x]
    g = datos_canal_verde[y, x]
    b = datos_canal_azul[y, x]
    k_colores.append((r, g, b))

for i in range(h):
    for j in range(w):
        rojo = datos_canal_rojo[i, j]
        verde = datos_canal_verde[i, j]
        azul = datos_canal_azul[i, j]
        for punto in k_colores:
            rojo2 = punto[0]
            verde2 = punto[1]
            azul2 = punto[2]
            d = math.sqrt(((rojo - rojo2) ** 2) + ((verde - verde2) ** 2) + ((azul - azul2) ** 2))
            for color in k_colores:
                distancia = abs(d, color)

print(k_colores)