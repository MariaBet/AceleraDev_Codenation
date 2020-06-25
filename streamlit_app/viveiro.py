# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from os import system


st.markdown(" ## ** Viveiro Florestal em Unidades de Conservação ** ")
st.image("image1.png", width=700)

if st.checkbox("Saber Mais"):
    st.markdown(''' ### O que é uma unidade de conservação?
    É uma área de proteção ambiental. As unidades de conservação
    (UCs) são legalmente instituídas pelo poder público, nas suas três
    esferas (municipal, estadual e federal). Elas são reguladas pela
    Lei no. 9.985, de 2000, que institui
    o Sistema Nacional de Unidades de Conservação (SNUC)''')

st.markdown(" ### ** Ánalise de Dados sobre a produção de mudas florestais ** ")

def main():

    name_file = 'viveiro.csv'
    df = pd.read_csv(name_file, sep=';')
    if st.checkbox("Deseja saber as quais mudas são desenvolvidas neste espaço? Clique "):
        st.dataframe(df.especie)

    st.markdown('## **Ánalise dos Dados do presentes no Dataset ** ')

    add_selectbox = st.sidebar.selectbox(
    "Selecione sua ánalise",
    ("Índice", "Visualização do Arquivo CSV", "Número de linhas",
    "Número de colunas", "Contagem de dados em branco" )
    )

    if add_selectbox == "Visualização do Arquivo CSV":
        slider = st.slider('Selecione o número de linhas', 1, 50)
        st.dataframe(df.head(slider))


    if add_selectbox == "Número de linhas":
        st.markdown(' ### ** Informação presente no Dataset **')
        st.markdown(df.shape[0])

    if add_selectbox == 'Número de colunas':
        st.markdown(' ### ** Informação presente no Dataset **')
        st.markdown(df.shape[1])

    if add_selectbox == "Contagem de dados em branco":
        st.markdown(' ### ** Informação presente no Dataset **')
        st.dataframe(df.isna().sum())

    aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})
    colunas_numericas = list(aux[aux['tipos'] != 'object']['colunas'])
    colunas_object = list(aux[aux['tipos'] == 'object']['colunas'])
    colunas = list(df.columns)

    add_selectbox2 = st.sidebar.selectbox(
    "Selecione a estatítica descritiva",
    ("Índice", "Média", "Mediana",
    "Desvio Padrão")
    )

    if add_selectbox2 == "Média":
        col = st.selectbox('Selecione a coluna :', colunas_numericas)
        st.text('Média')
        st.markdown(df[col].mean())

    if add_selectbox2 == "Mediana":
        col = st.selectbox('Selecione a coluna :', colunas_numericas)
        st.text('Mediana')
        st.markdown(df[col].median())

    if add_selectbox2 == "Desvio Padrão":
        col = st.selectbox('Selecione a coluna :', colunas_numericas)
        st.markdown(df[col].std())

    add_selectbox3 = st.sidebar.selectbox(
        " Especies do viveiro",
        ("Índice" , "Espécie mais cultivada", "Qualquer coisa",
        "escola")
        )

    if add_selectbox3 == "Espécie mais cultivada":
        st.dataframe(df.groupby('especie')['germinacao'].median().reset_index().sort_values('germinacao', ascending = False))






if __name__ == '__main__':
    main()
