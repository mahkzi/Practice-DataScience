# Crear una lista de 10 productos con precios.
#productos = [
#    ["Monitor", "Mouse", "Teclado", "Televisión", "Celular", "Cama", "Sillón", "Mesa", "Lavarropas", "Remera"],
#    [300, 100, 200, 175, 250, 500, 435, 390, 450, 23]
#]
# Calcular el producto más caro, más barato y el promedio.
#print(max(productos[1]))
#print(min(productos[1]))
#print(sum(productos[1]) / len(productos[1]))
# Contar la frecuencia de palabras en un texto.
# frecuencia = {}
# texto = """
# Python es un lenguaje de programación versátil y fácil de aprender.
# Se utiliza para desarrollar aplicaciones, automatizar tareas, analizar datos
# y crear inteligencia artificial.

# El análisis de texto permite identificar cuántas palabras contiene un párrafo.
# También podemos contar caracteres, eliminar espacios innecesarios y separar
# las palabras utilizando diferentes métodos de Python.

# Aprender a manipular cadenas de texto es fundamental para cualquier
# programador que quiera trabajar con datos.
# """
# # Primero limpiamos el texto, para igualar los formatos de las palabras
# texto_limpio = texto.lower().split()

# for palabra in texto_limpio:
#     frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
# print(frecuencia)

# Eliminar duplicados de una lista manteniendo el orden.

# lista_duplicada = [1,3,2,1,3,5,6,4,3,2,1,4,5,3,2,5,7,8,534,2,4,5]
# vistos = set()
# resultado = []
# for x in lista_duplicada:
#     if x not in vistos:
#         vistos.add(x)
#         resultado.append(x)
# print(resultado)

# Crear un diccionario de estudiantes con notas y calcular promedios.
# estudiantes = {"Agus": 10, "Benito": 8, "Carlos": 4, "Dumas": 2, "Eren": 3, "Facundo": 5, "Gerardo": 6}
# print(sum(estudiantes.values())/len(estudiantes))

# Filtrar productos con precio mayor a un valor dado usando comprensión de listas.

productos = [300, 100, 200, 175, 250, 500, 435, 390, 450, 23]
productos_filtrados = [p for p in productos if p > 200]
print(productos_filtrados)