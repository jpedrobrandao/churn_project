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

---

## 📊 Dataset

O dataset utilizado é o [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn), disponível no Kaggle. Ele contém informações sobre clientes de uma empresa de telecomunicações, incluindo:

- **Variáveis demográficas**: Gênero, idade, etc.
- **Serviços contratados**: Tipo de contrato, serviços adicionais, etc.
- **Churn**: Indica se o cliente cancelou o serviço (Yes/No).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. **Python 3.8 ou superior** instalado.
2. **Git** instalado (opcional, para clonar o repositório).

### Passos para Execução

1. Clone o repositório:

```bash
   git clone https://github.com/seu-usuario/churn_project.git
   cd churn_project
   
Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv churn_env
source churn_env/bin/activate  # No Windows: churn_env\Scripts\activate

Instale as dependências:

```bash
pip install -r requirements.txt

Execute o dashboard:

```bash
streamlit run app.py
Acesse o dashboard no navegador:

O Streamlit abrirá automaticamente o dashboard em http://localhost:8501.

📈 Resultados
O modelo de Random Forest alcançou as seguintes métricas:

Acurácia: 0.81

Precisão: 0.68

Recall: 0.53

AUC-ROC: 0.85

O dashboard permite:

Visualizar a distribuição de churn.

Fazer previsões em tempo real para novos clientes.

📝 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

✉️ Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: João Pedro Brandão

Email: jpedro.brandao@hotmail.com

LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/f1joaopedrobrandao/)

---

### Como Usar:
1. Copie o conteúdo acima.
2. Crie um arquivo chamado `README.md` no seu repositório do GitHub.
3. Cole o conteúdo no arquivo.
4. Substitua os placeholders (como `[Seu Nome]`, `[seu-email@example.com]`, etc.) pelas suas informações.

Pronto! Agora seu projeto está bem documentado e pronto para ser compartilhado. 😊
