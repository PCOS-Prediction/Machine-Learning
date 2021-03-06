# -*- coding: utf-8 -*-
"""Copy of Copy of PCOS_DataCleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tv0oEBigTE2sb41Dzga8aNjDmKXnmPkT
"""

from google.colab import files
import numpy as np
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')


path = "/content/drive/My Drive/SEM 4 - PCOS Prediction Research Project/Codes/allData.csv"
data = pd.read_csv(path)

data.head()


def label5(row):
    if row['Hair growth on Chin'] == 'normal':
        return 0
    elif row['Hair growth on Chin'] == 'moderate':
        return 1
    else:
        return 2


data['Hair growth on Chin'] = data.apply(lambda row: label5(row), axis=1)
data.head()


def label16(row):
    if row['relocated city'] == 'Yes':
        return 1
    else:
        return 0


data['relocated city'] = data.apply(lambda row: label16(row), axis=1)
data.head()

data.to_csv('data.csv')
files.download("data.csv")


def label17(row):
    if row['Period Length'] == '2-3 days':
        return 3
    elif row['Period Length'] == '4-5 days':
        return 5
    elif row['Period Length'] == '6-7 days':
        return 7
    else:
        return 9


data['Period Length'] = data.apply(lambda row: label17(row), axis=1)
data.head()


def label18(row):
    if row['Cycle Length'] == '20-24 days':
        return 22
    elif row['Cycle Length'] == '20-28 days':
        return 25
    elif row['Cycle Length'] == '25-28':
        return 27
    elif row['Cycle Length'] == '29-35 days':
        return 32
    elif row['Cycle Length'] == '36+ days':
        return 37
    else:
        return 'NaN'


data['Cycle Length'] = data.apply(lambda row: label18(row), axis=1)
data.head()

del data['PCOS_from']

data

data.to_csv('data_final.csv')
files.download("data_final.csv")

path = "/content/drive/My Drive/SEM 4 - PCOS Prediction Research Project/Codes/Decesion Tree/data (1).csv"
data1 = pd.read_csv(path)
data1.head()


def label17(row):
    if row['Period Length'] == '2-3 days':
        return 3
    elif row['Period Length'] == '4-5 days':
        return 5
    elif row['Period Length'] == '6-7 days':
        return 7
    else:
        return 9


data1['Period Length'] = data.apply(lambda row: label17(row), axis=1)
data1.head()


def label18(row):
    if row['Cycle Length'] == '20-24 days':
        return 1
    elif row['Cycle Length'] == '20-28 days':
        return 2
    elif row['Cycle Length'] == '25-28':
        return 3
    elif row['Cycle Length'] == '29-35 days':
        return 4
    elif row['Cycle Length'] == '36+ days':
        return 5
    else:
        return 6


data1['Cycle Length'] = data.apply(lambda row: label18(row), axis=1)
data1.head()


def label19(row):
    if row['Age'] == 'Below 18':
        return 1
    elif row['Age'] == '18-25':
        return 2
    elif row['Age'] == '26-30':
        return 3
    elif row['Age'] == '31-35':
        return 4
    elif row['Age'] == '36-40':
        return 5
    elif row['Age'] == '41-45':
        return 6
    else:
        return 7


data1['Age'] = data.apply(lambda row: label19(row), axis=1)
data1.head()

data1.to_csv('data_cleaned.csv')
files.download("data_cleaned.csv")
