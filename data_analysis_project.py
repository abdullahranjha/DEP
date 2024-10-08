# -*- coding: utf-8 -*-
"""Data Analysis Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jq1GpUceyDRWxVrAVHyxTomsEmz_Egtq
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('train.csv')

df.head()

print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop(columns=['Cabin'], inplace=True)

survival_rate_embarked = df.groupby('Embarked')['Survived'].mean()

plt.figure(figsize=(10, 5))
survival_rate_embarked.plot(kind='bar', color='orange')
plt.title('Survival Rate by Port of Embarkation')
plt.xlabel('Port of Embarkation')
plt.ylabel('Survival Rate')
plt.show()

df.info()

df.describe()

df.drop("Name",axis=1,inplace=True)

df

df.drop("Ticket",axis=1,inplace=True)
df.drop("PassengerId",axis=1,inplace=True)
df.drop("Embarked",axis=1,inplace=True)

df

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Sex']=le.fit_transform(df['Sex'])
df1=df
df1

df1=df1.dropna(axis='columns')
df1=df1.dropna(axis='rows')
df1

df_mean=df1.fillna(df1.mean())
df_mean

df_mean.isnull().sum()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df1.drop('Survived',axis=1),df1['Survived'],test_size=0.2,random_state=42)