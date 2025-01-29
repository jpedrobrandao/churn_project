import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    df = pd.read_csv(url)
    return df

def explore_data(df):
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df.describe())

    sns.countplot(x='Churn', data=df)
    plt.title('Distribuição de Churn')
    plt.show()

    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlação')
    plt.show()