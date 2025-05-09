from PIL import Image
import numpy as np
import random
import math
from funciones import *

# Abrir la imagen
imagen = Image.open("../Trabajo-Pr-ctico-N-2-Pensamiento-Computacional-/test_images/soccer.bmp")
canal_rojo, canal_verde, canal_azul = dividir_canales(imagen)
w, h = imagen.size

# Convertir canales a arrays de numpy
datos_canal_rojo = np.array(canal_rojo)
datos_canal_verde = np.array(canal_verde)
datos_canal_azul = np.array(canal_azul)

k = int(input("¿Cuántos colores querés usar?: "))

# 1️⃣ Seleccionar k centroides aleatorios
valores_pixeles_principales = []
for _ in range(k):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    r = datos_canal_rojo[y, x]
    g = datos_canal_verde[y, x]
    b = datos_canal_azul[y, x]
    valores_pixeles_principales.append([int(r), int(g), int(b)])

# 🚀 Iterar 10 veces
for iteracion in range(10):
    print(f"\nIteración {iteracion + 1}")

    # Inicializar clusters vacíos
    clusters = [[] for _ in range(k)]

    # Asignar cada píxel al cluster más cercano
    for i in range(h):
        for j in range(w):
            rojo = int(datos_canal_rojo[i, j])
            verde = int(datos_canal_verde[i, j])
            azul = int(datos_canal_azul[i, j])
            lista_valores = []

            # Calcular la distancia a cada centroide
            for (rojo2, verde2, azul2) in valores_pixeles_principales:
                valor_punto = math.sqrt(
                    ((rojo - rojo2) ** 2) +
                    ((verde - verde2) ** 2) +
                    ((azul - azul2) ** 2)
                )
                lista_valores.append(valor_punto)

            # Encontrar el índice del cluster más cercano
            indice_minimo = lista_valores.index(min(lista_valores))

            # Agregar el píxel (i, j) al cluster correspondiente
            clusters[indice_minimo].append((i, j))

    # Calcular el promedio RGB para cada cluster
    nuevos_valores_pixeles_principales = []

    for cluster in clusters:
        if len(cluster) == 0:
            # Si el cluster quedó vacío, mantener el centroide anterior (o poner 0,0,0 si preferís)
            nuevos_valores_pixeles_principales.append([0, 0, 0])
            continue

        suma_r = 0
        suma_g = 0
        suma_b = 0

        for (i, j) in cluster:
            suma_r += int(datos_canal_rojo[i, j])
            suma_g += int(datos_canal_verde[i, j])
            suma_b += int(datos_canal_azul[i, j])

        cantidad = len(cluster)
        promedio_r = suma_r // cantidad
        promedio_g = suma_g // cantidad
        promedio_b = suma_b // cantidad

        nuevos_valores_pixeles_principales.append([promedio_r, promedio_g, promedio_b])

    # Mostrar nuevos centroides para esta iteración
    for idx, (r, g, b) in enumerate(nuevos_valores_pixeles_principales):
        print(f"Cluster {idx}: R={r}, G={g}, B={b}")

    # Actualizar los centroides para la próxima iteración
    valores_pixeles_principales = nuevos_valores_pixeles_principales

# ✅ Crear imagen final usando los clusters de la última iteración
imagen_final = Image.new("RGB", (w, h))
pixels_final = imagen_final.load()

# Usamos los clusters finales y pintamos cada píxel de su color correspondiente
for cluster_idx, cluster in enumerate(clusters):
    r, g, b = valores_pixeles_principales[cluster_idx]
    for (i, j) in cluster:
        pixels_final[j, i] = (r, g, b)

# Mostrar la imagen final
imagen_final.show()

# También podés guardarla si querés:
# imagen_final.save("resultado_kmeans.png")
