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
clusters = []
valores_pixeles_principales = []

#Selecciono los pixeles aleatoriamente y los pongo en una lista. Ademas cada uno es la primera posición de cada cluster
for coordenada in range(k):
    x = random.randint(0, w-1)
    y = random.randint(0, h-1)
    r = datos_canal_rojo[y, x]
    g = datos_canal_verde[y, x]
    b = datos_canal_azul[y, x]
    valores_pixeles_principales.append((r, g, b))
    clusters.append(x,y)

#Recorro todos los píxeles y los pongo en cada cluster segun a cual centroide se asemeja más
for i in range(h):
    for j in range(w):
        rojo = datos_canal_rojo[i, j]
        verde = datos_canal_verde[i, j]
        azul = datos_canal_azul[i, j]
        lista_valores= []
        for (rojo2, verde2, azul2) in valores_pixeles_principales:
            valor_punto = math.sqrt(((int(rojo) - int(rojo2)) ** 2) + ((int(verde) - int(verde2)) ** 2) + ((int(azul) - int(azul2)) ** 2))
            lista_valores.append(valor_punto)
        cluster_mas_cercano = lista_valores.index(min(lista_valores))
        for i in range(len(clusters)):
    

            
                



