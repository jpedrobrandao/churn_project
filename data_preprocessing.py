from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

def preprocess_data(df):
    label_encoder = LabelEncoder()
    df['Churn'] = label_encoder.fit_transform(df['Churn'])
    df.drop(['customerID'], axis=1, inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    return df

def split_data(df):
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test, scaler