# Ejercicio 1: Función de saludo simple
def saludar(nombre):
    return f"Hola, {nombre}! esto es un programa interactivo :)"

# Ejercicio 2: Suma de dos números
def sumar(a, b):
    return a + b

# Ejercicio 3: Área de un triángulo
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

# Ejercicio 4: Calculadora de descuento
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final

# Ejercicio 5: Suma de una lista de números utilizando un bucle
def sumar_lista(numeros):
    suma_total = 0
    for numero in numeros:
        suma_total += numero
    return suma_total

# Ejercicio 6: Funciones con valores predeterminados
def producto(nombre, cantidad=1, precio_unitario=10):
    return f"Total a pagar por {cantidad} unidad(es) de {nombre}s: {cantidad * precio_unitario}"

# Ejercicio 7: Números pares e impares
def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

# Ejercicio 8: Multiplicación con *args
def multiplicar_todos(*args):
    # Si no se pasan argumentos, devolver 1
    if not args:
        return 1
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

# Ejercicio 9: Información de una persona con **kwargs
def informacion_personal(**kwargs):
    return kwargs

# Ejercicio 10: Calculadora flexible
def calculadora_flexible(a, b, operacion='suma'):
    operaciones = {
        'suma': a + b,
        'resta': a - b,
        'multiplicación': a * b,
        'división': a / b if b != 0 else 'División por cero no permitida'
    }
    return operaciones.get(operacion, 'Operación no válida')
