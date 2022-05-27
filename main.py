import streamlit as st
import pandas as pd
import numpy as np
import functions as ft


st.set_page_config(layout='wide')

pagina = st.sidebar.selectbox("Página", ('Home', 'Datos'))
df = None

if pagina == 'Home':
    ft.home()
elif pagina == 'Datos':
    df= ft.datos()

col1, col2, col3 = st.columns(3)

with col1:
    st.map(df)
with col2:
    df_bar = df.groupby('DISTRITO')['Nº CARGADORES'].sum()
    st.bar_chart(df_bar)

with col3:
    df_bar = df.groupby('OPERADOR')['Nº CARGADORES'].sum()
    st.bar_chart(df_bar)