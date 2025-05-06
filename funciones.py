from PIL import Image
import numpy as np
import math

def get_grid_coords(h, w, dot_size, angle_deg):
    positions = []
    angle_rad = math.radians(angle_deg)
    cx, cy = w / 2, h / 2

    diag = int(math.hypot(w, h))
    num_x = diag // dot_size + 3
    num_y = diag // dot_size + 3

    offset_x = cx - (num_x * dot_size) / 2
    offset_y = cy - (num_y * dot_size) / 2

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

def radios(canal, h, w):
    matriz_radios = np.zeros((h, w), dtype=float)
    positions = get_grid_coords(h, w, dot_size=5, angle_deg = 15)
    dot_size = 5
    for (x, y) in positions:
        if 0 <= x < w and 0 <= y < h:
            intensidad = canal[y, x]
            r = ((1 - intensidad/255) * dot_size * 0.7)
            matriz_radios[y, x] = r
    return matriz_radios
        
def dibujar_circulo(matriz, matriz_radios):
    alto, ancho = matriz.shape
    matriz_resultado = matriz.copy()  # Crear una copia para no modificar la original
    
    # Recorrer toda la matriz de radios
    for y in range(alto):
        for x in range(ancho):
            r = matriz_radios[y, x]  # Obtener el radio para esta posición
            
            # Solo dibujar si hay un radio mayor que cero
            if r > 0:
                # Dibujar un círculo centrado en (x,y) con radio r
                y_min = max(0, int(y - r))
                y_max = min(alto, int(y + r) + 1)
                x_min = max(0, int(x - r))
                x_max = min(ancho, int(x + r) + 1)
                
                # Recorrer el área del círculo
                for cy in range(y_min, y_max):
                    for cx in range(x_min, x_max):
                        # Verificar si el punto está dentro del círculo
                        if (cx - x)**2 + (cy - y)**2 <= r**2:
                            matriz_resultado[cy, cx] = 0  # Dibujar punto negro
    
    return matriz_resultado