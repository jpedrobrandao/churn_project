import streamlit as st
from data_analysis import load_data, explore_data
from data_preprocessing import preprocess_data, split_data
from model_training import train_model, evaluate_model

st.title("Previsão de Churn em Telecomunicações")

# Carregar e explorar os dados
df = load_data()
st.write("### Dados Brutos")
st.write(df.head())

# Pré-processar os dados
df_processed = preprocess_data(df)
X_train, X_test, y_train, y_test, scaler = split_data(df_processed)

# Treinar o modelo
model = train_model(X_train, y_train)

# Avaliar o modelo
st.write("### Avaliação do Modelo")
evaluate_model(model, X_test, y_test)