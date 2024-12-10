import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Cargar modelos


# Título de la aplicación
st.title('Predicción de Gastos y Cantidad de Tarjetas de Crédito de Clientes en el Banco Durmammus')

# Descripción
st.write("""
Esta aplicación predice cuánto gasta un cliente mensualmente con sus tarjetas de crédito y en qué rango de cuántas tarjetas de crédito puede tener dicho cliente.
""")

# Funciones para predecir


# Formulario de entrada de datos
def user_input_features():
    st.sidebar.header('Parámetros de entrada del cliente')
    variable1 = st.sidebar.slider('Variable 1', min_value=0, max_value=100, value=50)
    variable2 = st.sidebar.slider('Variable 2', min_value=0, max_value=100, value=50)
    variable3 = st.sidebar.slider('Variable 3', min_value=0, max_value=100, value=50)
    variable4 = st.sidebar.slider('Variable 4', min_value=0, max_value=100, value=50)
    variable5 = st.sidebar.slider('Variable 5', min_value=0, max_value=100, value=50)
    variable6 = st.sidebar.slider('Variable 6', min_value=0, max_value=100, value=50)
    variable7 = st.sidebar.slider('Variable 7', min_value=0, max_value=100, value=50)
    variable8 = st.sidebar.slider('Variable 8', min_value=0, max_value=100, value=50)
    variable9 = st.sidebar.slider('Variable 9', min_value=0, max_value=100, value=50)
    variable10 = st.sidebar.slider('Variable 10', min_value=0, max_value=100, value=50)
    # ...
    data = {'Variable1': variable1,
            'Variable2': variable2,
            'Variable3': variable3,
            'Variable4': variable4,
            'Variable5': variable5,
            'Variable6': variable6,
            'Variable7': variable7,
            'Variable8': variable8,
            'Variable9': variable9,
            'Variable10': variable10
            }
    features = pd.DataFrame(data, index=[0])
    return features

# Obtener datos de entrada del usuario
input_df = user_input_features()

# Mostrar datos de entrada
st.subheader('Datos de entrada del cliente')
st.write(input_df)

# Realizar predicciones


# Mostrar predicciones
st.subheader('Predicción de gasto mensual')

