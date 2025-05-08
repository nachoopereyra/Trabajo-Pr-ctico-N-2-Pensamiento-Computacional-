from PIL import Image
import numpy as np
from funciones import *

imagen = Image.open("../Trabajo-Pr-ctico-N-2-Pensamiento-Computacional-/test_images/sunrise.bmp")
canal_rojo, canal_verde, canal_azul = dividir_canales(imagen)
w, h = imagen.size

datos_canal_rojo = np.array(canal_rojo)
datos_canal_verde = np.array(canal_verde)
datos_canal_azul = np.array(canal_azul)
positions = get_grid_coords(h, w, dot_size = 5, angle_deg = 15)

radio_rojo = radios(datos_canal_rojo, h, w)
matriz_rojo = dibujar_circulo(datos_canal_rojo, radio_rojo)
radio_verde = radios(datos_canal_verde, h, w)
matriz_verde = dibujar_circulo(datos_canal_verde, radio_verde)
radio_azul = radios(datos_canal_azul, h, w)
matriz_azul = dibujar_circulo(datos_canal_azul, radio_azul)

# Juntar los tres canales en una imagen a color
imagen_final = np.stack((matriz_rojo, matriz_verde, matriz_azul), axis=2)
imagen_resultado = Image.fromarray(imagen_final.astype('uint8'))

# Mostrar la imagen
imagen_resultado.show()