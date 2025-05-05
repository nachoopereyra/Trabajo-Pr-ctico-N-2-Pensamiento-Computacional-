from PIL import Image
import numpy as np
import math

def get_grid_coords(h, w, dot_size, angle_deg):
    positions = []
    angle_rad = math.radians(angle_deg)
    cx, cy = w / 2, h / 2 # centro de la imagen

    # calcular la dimension de la grilla
    diag = int(math.hypot(w, h))
    num_x = diag // dot_size + 3
    num_y = diag // dot_size + 3

    # alinear el centro de la grilla con el centro de la imagen
    offset_x = cx - (num_x * dot_size) / 2
    offset_y = cy - (num_y * dot_size) / 2

    # recorrer la grilla y calcular las posiciones (geometría 👻) 
    for i in range(num_y):
        for j in range(num_x):
            gx = offset_x + j * dot_size + dot_size / 2 - cx
            gy = offset_y + i * dot_size + dot_size / 2 - cy
            rx = gx * math.cos(angle_rad) - gy * math.sin(angle_rad) + cx
            ry = gx * math.sin(angle_rad) + gy * math.cos(angle_rad) + cy

            ix, iy = int(round(rx)), int(round(ry))
            if 0 <= iy < h and 0 <= ix < w:
                positions.append((ix, iy))
    return positions


def dividir_canales(imagen):
    imagen_rgb = imagen.convert("RGB")
    canal_rojo, canal_verde, canal_azul = imagen_rgb.split()
    return canal_rojo, canal_verde, canal_azul

def radios(canal,w,h):
    matriz = []
    for i in range(w):
        for j in range(h):
            matriz+= [255]
    positions = get_grid_coords(w,h, dot_size=5,angle_deg = 15)
    dot_size = 5
    radio = []
    i=0
    j=0
    for x, y in positions:
        intensidad = canal[x][y] 
        i+=1
        j+=1
        radio += [(1 - (intensidad/255) * dot_size * 0.7)]
    return radio
        
