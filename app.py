import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de Ventas de Coches')

hist_chckbx = st.checkbox('Crear histograma')  # Casilla para crear histograma
# Casilla para crear gráfico de dispersión
scat_chckbx = st.checkbox('Crear gráfico de dispersión')


run_button = st.button('Crear gráfico(s)')
if run_button:

    if hist_chckbx:
        st.write('Creación de histograma sobre los anuncios de venta de coches')

        hist = px.histogram(car_data, x='odometer')

        st.plotly_chart(hist, use_container_width=True)
        hist.show()

    if scat_chckbx:
        st.write(
            'Creación de gráfico de dispersión sobre los anuncios de venta de coches')

        scat = px.scatter(car_data, x='odometer', y='price')

        st.plotly_chart(scat, use_container_width=True)
        scat.show()
