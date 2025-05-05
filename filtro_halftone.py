from PIL import Image
import numpy as np
import math
from funciones import *
imagen = Image.open("../Trabajo-Pr-ctico-N-2-Pensamiento-Computacional-/test_images/alonso.jpeg")
canal_rojo, canal_verde, canal_azul = dividir_canales(imagen)
w, h = imagen.size

canal_rojo = np.array(canal_rojo)
canal_verde = np.array(canal_verde)
canal_azul = np.array(canal_azul)
positions = get_grid_coords(w,h, dot_size=5,angle_deg = 15)

radio = radios(canal_rojo,w,h)
print(radio)
