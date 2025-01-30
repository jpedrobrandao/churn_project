markdown
Copy
# Previsão de Churn em Telecomunicações

Este projeto tem como objetivo prever o churn (cancelamento de serviços) de clientes de uma empresa de telecomunicações utilizando técnicas de ciência de dados e machine learning. O modelo desenvolvido ajuda a identificar clientes com alta probabilidade de churn, permitindo que a empresa tome ações preventivas para retê-los.

---

## 📋 Sobre o Projeto

O churn é uma métrica crítica para empresas de telecomunicações, pois a retenção de clientes é mais econômica do que a aquisição de novos. Neste projeto, utilizamos um dataset público disponível no Kaggle para:

1. Realizar uma **análise exploratória dos dados** (EDA).
2. Pré-processar os dados para treinamento de modelos.
3. Treinar e avaliar um modelo de **Random Forest** para prever churn.
4. Criar um **dashboard interativo** usando Streamlit para visualizar previsões.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (Linguagem de programação)
- **Pandas** (Manipulação de dados)
- **NumPy** (Cálculos numéricos)
- **Matplotlib** e **Seaborn** (Visualização de dados)
- **Scikit-learn** (Machine Learning)
- **Streamlit** (Dashboard interativo)

---

## 📂 Estrutura do Projeto
churn_project/
│
├── app.py # Código do dashboard Streamlit
├── churn_analysis.py # Análise exploratória e pré-processamento
├── model_training.py # Treinamento e avaliação do modelo
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto
