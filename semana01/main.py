# ENTRADA DE DATOS

# INGRESOS
# Primero comenzamos con los ingresos.
pedir_ingresos = input("Ingrese sus Ingresos: ").strip()
if pedir_ingresos.isdigit():
    ingresos = float(pedir_ingresos)
    print(f"Su ingreso es de {ingresos:.2f} $")
else:
    print("Ingrese un número válido (De 0 para arriba)")
    
# GASTOS
# Luego, dividiendo los gastos por categoría. Vamos a pedir al usuario que ingrese los gastos de su respectiva categoría.
pedir_gasto_transporte = input("Ingrese su gasto de transporte: ").strip()
if pedir_gasto_transporte.isdigit():
    gasto_transporte = float(pedir_gasto_transporte)
    print(f"Su gasto en transporte es de {gasto_transporte:.2f} $")
else:
    print("Ingrese un número válido (De 0 para arriba)")
# Deberíamos reutilizar una función para evitar repetición y modulizar código, pero no esta en la teoría. Avanzamos con lo presente en ella.
pedir_gasto_hogar = input("Ingrese su gasto de transporte: ").strip()
if pedir_gasto_hogar.isdigit():
    gasto_hogar = float(pedir_gasto_hogar)
    print(f"Su gasto en el hogar es de {gasto_hogar:.2f} $")
else:
    print("Ingrese un número válido (De 0 para arriba)")
    
pedir_gasto_comida = input("Ingrese su gasto de transporte: ").strip()
if pedir_gasto_comida.isdigit():
    gasto_comida = float(pedir_gasto_hogar)
    print(f"Su gasto en comida es de {gasto_comida:.2f} $")
else:
    print("Ingrese un número válido (De 0 para arriba)")
    
# PROCESAMIENTO

total_gastos = gasto_comida + gasto_hogar + gasto_transporte
print(f"Su gasto total es de {total_gastos} $")

balance = round(ingresos - total_gastos,2)
if balance > 0:
    print("Felicidades estas ahorrando")  
elif balance == 0:
    print("Hay que mejorar, pero estas en equilibrio")
else:
    print("Estas en deficit")
print(f"Su balance es de {balance} $")

if ingresos == 0:
    print("Si no ganas nada, nunca vas a tener ahorro")
elif balance < 0 or balance > ingresos:
    print("Hay que bajar los gastos, o aumentar los ingresos")
else:
    porcentaje_de_ahorro = (balance / ingresos) * 100
    print(f"Su porcentaje de ahorro es de {porcentaje_de_ahorro} %")

