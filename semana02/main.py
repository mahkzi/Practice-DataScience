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

# productos = [300, 100, 200, 175, 250, 500, 435, 390, 450, 23]
# productos_filtrados = [p for p in productos if p > 200]
# print(productos_filtrados)

#Simular un carrito de compras con alta, baja y total.


carrito = []

catalogo = [
    ["Remera", 50],
    ["Pantalon", 70],
    ["Buzo", 100],
    ["Medias", 30],
    ["Gorra", 40]
]

salir = False

while not salir:

    print("\n===== CARRITO DE COMPRAS =====")
    print("1. Agregar producto (ALTA)")
    print("2. Eliminar producto (BAJA)")
    print("3. Mostrar carrito")
    print("4. Calcular total")
    print("5. Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))

        # ALTA
        if opcion == 1:

            print("\n===== CATÁLOGO =====")

            for item in catalogo:
                print(f"{item[0]} - ${item[1]}")

            producto = input("\nIngrese el producto: ").capitalize()

            producto_encontrado = False

            for item in catalogo:

                if producto == item[0]:

                    producto_encontrado = True

                    try:
                        cantidad = int(input("Ingrese la cantidad: "))

                        if cantidad > 0:

                            carrito.append([item[0], item[1], cantidad])

                            print("Producto agregado correctamente")

                        else:
                            print("Ingrese una cantidad mayor a 0")

                    except ValueError:
                        print("Debe ingresar una cantidad válida")

                    break

            if not producto_encontrado:
                print("Ese producto no existe")

        # BAJA
        elif opcion == 2:

            if len(carrito) == 0:
                print("\nEl carrito está vacío")

            else:

                print("\n===== MI CARRITO =====")

                for item in carrito:
                    print(f"{item[0]} - ${item[1]} - Cantidad: {item[2]}")

                producto = input("\nIngrese el producto que desea eliminar: ").capitalize()

                producto_eliminado = False

                for item in carrito:

                    if producto == item[0]:

                        carrito.remove(item)
                        producto_eliminado = True

                        print("Producto eliminado correctamente")
                        break

                if not producto_eliminado:
                    print("El producto no se encuentra en el carrito")

        # MOSTRAR CARRITO
        elif opcion == 3:

            print("\n===== MI CARRITO =====")

            if len(carrito) == 0:
                print("El carrito está vacío")

            else:

                for item in carrito:
                    subtotal = item[1] * item[2]

                    print(f"""
Producto: {item[0]}
Precio unitario: ${item[1]}
Cantidad: {item[2]}
Subtotal: ${subtotal}
""")

        # TOTAL
        elif opcion == 4:

            total = 0

            for item in carrito:

                subtotal = item[1] * item[2]
                total += subtotal

            print(f"\nEl total de la compra es: ${total}")

        # SALIR
        elif opcion == 5:

            salir = True
            print("\nGracias por su compra")

        else:
            print("Opción inválida")

    except ValueError:
        print("Ingrese una opción numérica válida")

    