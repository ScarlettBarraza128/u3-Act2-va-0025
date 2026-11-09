import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Emily Barraza NC = 0025

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de lenguajes de programación con 4 elementos por lista
pyt = ['Python', 1991, True, 1]
jva = ['Java', 1995, True, 3]
js  = ['JavaScript', 1995, False, 2]
cpp = ['C++', 1985, True, 4]
php = ['PHP', 1995, False, 8]

# Creamos una lista de listas
lista_lenguajes = [pyt, jva, js, cpp, php]
print(lista_lenguajes)

# Utilizar pandas para crear la tabla (DataFrame o marco de datos)
# A cada columna le ponemos nombre
df_lenguajes = pd.DataFrame(lista_lenguajes, columns=["Nombre", "Año", "Es_Tipado_Fuerte", "Ranking"])
print(df_lenguajes)

# creamos el archivo CSV y lo guardamos
df_lenguajes.to_csv("lenguajes.csv", index=False)

# crear grafica de lineas 
# donde x es Nombre es el eje horizontal
# donde y es Ranking es el eje vertical
plt.plot(df_lenguajes["Nombre"], df_lenguajes["Ranking"])
plt.title("Grafica lenguajes 0025")
plt.xlabel("Nombre de los lenguajes")
plt.ylabel("Ranking de popularidad")
plt.show()

# creamos una grafica de puntos 
plt.scatter(df_lenguajes["Nombre"], df_lenguajes["Ranking"])
plt.title("Lenguajes 0025")
plt.xlabel("Los lenguajes")
plt.ylabel("Ranking de popularidad")
plt.show()

# Grafica de barras
plt.bar(df_lenguajes["Nombre"], df_lenguajes["Ranking"])
plt.title("Lenguajes 0025")
plt.xlabel("Los lenguajes")
plt.ylabel("Ranking de popularidad")
plt.show()

# Ordenar la grafica de manera descendente
# De la más grande a la más pequeña (por Ranking)
df_leng_ordenar = df_lenguajes.sort_values("Ranking", ascending=False)
plt.bar(df_leng_ordenar["Nombre"], df_leng_ordenar["Ranking"])
plt.show()

# coloreando grafica (5 barras)
df_leng_ordenar = df_lenguajes.sort_values("Ranking", ascending=False)
plt.bar(df_leng_ordenar["Nombre"], df_leng_ordenar["Ranking"],
        color=["b", "g", "c", "m", "y"]
)
plt.show()

# Grafica de pastel 
plt.pie(df_lenguajes["Ranking"], labels=df_lenguajes["Nombre"])
plt.show()