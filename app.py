import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Anúncios de carros', page_icon='🚗')


@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')


car_data = load_data()

numeric_cols = ['price', 'odometer', 'model_year', 'days_listed']

st.header('Anúncios de venda de carros')
st.write(
    'Explore um conjunto de dados de anúncios de carros usados. '
    'Marque as caixas abaixo para ver uma amostra dos dados e criar os gráficos.'
)

# Amostra dos dados
if st.checkbox('Mostrar amostra dos dados'):
    st.dataframe(car_data.head(100))

# Histograma
build_histogram = st.checkbox('Criar histograma')
if build_histogram:
    hist_col = st.selectbox('Coluna do histograma', numeric_cols)
    st.write(f'Histograma da coluna {hist_col}')
    fig = px.histogram(car_data, x=hist_col)
    st.plotly_chart(fig, width='stretch')

# Gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')
if build_scatter:
    x_col = st.selectbox('Eixo x', numeric_cols, index=1)
    y_col = st.selectbox('Eixo y', numeric_cols, index=0)
    color_by_condition = st.checkbox('Colorir pela condição do carro')
    st.write(f'Gráfico de dispersão: {y_col} x {x_col}')
    fig = px.scatter(
        car_data,
        x=x_col,
        y=y_col,
        color='condition' if color_by_condition else None,
    )
    st.plotly_chart(fig, width='stretch')
