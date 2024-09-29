import streamlit as st
from funciones import (
    saludar, sumar, calcular_area_triangulo, calcular_precio_final, 
    sumar_lista, producto, numeros_pares_e_impares, multiplicar_todos, 
    informacion_personal, calculadora_flexible
)

# Configurar la página con un título inicial
st.set_page_config(page_title="Aplicación de Ejercicios Interactivos", layout="wide")

# Diccionario de títulos dinámicos para cada sección
titulos = {
    "Función de saludo": "👋 Saludo Personalizado",
    "Suma de dos números": "➕ Suma de Dos Números",
    "Área de un triángulo": "📐 Área de un Triángulo",
    "Calculadora de descuento": "💸 Calculadora de Descuento",
    "Suma de una lista de números": "🧮 Suma de una Lista de Números",
    "Cálculo de productos": "📦 Cálculo de Productos",
    "Números pares e impares": "🔢 Pares e Impares",
    "Multiplicación con *args": "✖️ Multiplicación con *args",
    "Información de una persona": "🧑 Información Personal",
    "Calculadora flexible": "🧮 Calculadora Flexible"
}

# Mostrar un título en la parte superior de la barra lateral
st.sidebar.title("PROGRAMA INTERACTIVO DE 10 FUNCIONES CON PYTHON")

# Sidebar para la selección de la sección
seleccion = st.sidebar.selectbox("Selecciona el ejercicio", list(titulos.keys()))

# Mostrar el título en la aplicación basado en la selección
st.title(titulos[seleccion])

# Secciones para cada ejercicio
if seleccion == "Función de saludo":
    nombre = st.text_input("Ingresa tu nombre:", "")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif seleccion == "Suma de dos números":
    a = st.number_input("Ingresa el primer número:", value=0.0)  # Cambiado a 0.0 para aceptar decimales
    b = st.number_input("Ingresa el segundo número:", value=0.0)  # Cambiado a 0.0 para aceptar decimales
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")

elif seleccion == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo:", value=0.0)
    altura = st.number_input("Ingresa la altura del triángulo:", value=0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

elif seleccion == "Calculadora de descuento":
    precio = st.number_input("Precio original del producto:", value=0.0)
    descuento = st.number_input("Porcentaje de descuento (opcional):", value=10.0)
    impuesto = st.number_input("Porcentaje de impuesto (opcional):", value=16.0)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")

elif seleccion == "Suma de una lista de números":
    numeros = st.text_area("Ingresa una lista de números separados por comas:", "")
    if st.button("Sumar lista"):
        lista_numeros = [float(num) for num in numeros.split(",") if num.strip()]
        st.write(f"La suma de la lista es: {sumar_lista(lista_numeros)}")

elif seleccion == "Cálculo de productos": #funciones con valores predeterminados
    nombre_producto = st.text_input("Nombre del producto:", "")
    cantidad = st.number_input("Cantidad:", value=1)
    precio_unitario = st.number_input("Precio por unidad:", value=10.0)
    if st.button("Calcular precio total"):
        st.write(producto(nombre_producto, cantidad, precio_unitario))

elif seleccion == "Números pares e impares":
    lista = st.text_area("Ingresa una lista de números separados por comas:", "")
    if st.button("Separar pares e impares"):
        lista_numeros = [int(num) for num in lista.split(",") if num.strip().isdigit()]
        pares, impares = numeros_pares_e_impares(lista_numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")

elif seleccion == "Multiplicación con *args":
    numeros = st.text_area("Ingresa los números separados por comas:", "")
    if st.button("Multiplicar"):
        try:
            # Convertir cada número a float, ignorando valores no numéricos
            lista_numeros = [float(num) for num in numeros.split(",") if num.strip()]
            
            # Pasar los números como argumentos individuales a la función con *lista_numeros
            resultado = multiplicar_todos(*lista_numeros)
            
            st.write(f"El resultado de la multiplicación es: {resultado}")
        except ValueError:
            st.write("Por favor, ingresa solo números separados por comas.")

elif seleccion == "Información de una persona":
    nombre = st.text_input("Nombre:", "")
    edad = st.number_input("Edad:", value=0)
    direccion = st.text_input("Dirección:", "")
    estado_civil = st.text_input("Estado civil: ", "")
    if st.button("Mostrar información"):
        info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion, estado_civil=estado_civil)
        st.write(info)

elif seleccion == "Calculadora flexible":
    a = st.number_input("Número 1:", value=0.0)
    b = st.number_input("Número 2:", value=0.0)
    operacion = st.selectbox("Operación:", ["suma", "resta", "multiplicación", "división"])
    if st.button("Calcular"):
        st.write(f"El resultado es: {calculadora_flexible(a, b, operacion)}")
