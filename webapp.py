# A primeira coisa que precisamos fazer é instalar as bibliotecas que vamos utilizar
# repare que estou no pycharm já utilizando um ambiente virtual chamado webappacoes
# o proprio pycharm se encarrega de fazer isso para nós.

# Agora um maneira rápida de instalar as bibliotecas e usando o requeirements.txt
# Com ele é possível instalar todas as bibliotecas que serão usadas no projeto de uma vez só

# para isso vamos fgazer o seguinte

# Abra o terminal
# digite o comando: pip freeze > requirements.txt
# Clicque com botão direito em cima da pasta e clique em reload
# o arquivo requirements vai aparacer e provavalemente vai estar vazio
# agora vamos colocar dentro dentro dele as bibliotecas que vamos usar

# streamlit

# O pandas não precisa pois como estamos usando o ambiente do anaconda ele já vem instalado.


# importando as libraries

import streamlit as st
import pandas as pd
from datetime import date

# Nome da aplicação
st.write(
    """
    **Ações Web App**
    """
)

# Criando uma side bar

st.sidebar.header('Escolha as ações')


# Lendo arquivo de ações

def get_data():
    path = 'C:/Users/fabri/Google Drive/codifike/23 - WebAppAcoes/all_bovespa.csv'
    return pd.read_csv(path)


df = get_data()



df_data = pd.to_datetime(df['data_pregao']).dt.date.drop_duplicates()

min_data = min(df_data)
max_data = max(df_data)

stock = df['sigla_acao'].drop_duplicates()
stock_choice = st.sidebar.selectbox("Escolha a ação", stock)

start_date = st.sidebar.text_input("Digite uma data de inicio:", min_data)

end_date = st.sidebar.text_input("Digite uma data final:", max_data)

start = pd.to_datetime(start_date)
end = pd.to_datetime(end_date)

if start > end:
    st.error('Data Final deve ser **MAIOR** que data inicial')

df = df[(df['sigla_acao'] == stock_choice) & (pd.to_datetime(df['data_pregao']) >= start) & (pd.to_datetime(df['data_pregao']) <= end)]

df = df.set_index(pd.DatetimeIndex(df['data_pregao'].values))

#Criar grafico
st.header('AÇÃO: ' + stock_choice.upper())
st.write('Preço de Fechamento')
st.line_chart(df['preco_fechamento'])

st.write('Volume Negociado')
st.line_chart(df['volume_negocios'])

