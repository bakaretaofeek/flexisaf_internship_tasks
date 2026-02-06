import numpy as np
import pandas as pd
# importing data
df = pd.read_csv("C:/Users/USER/Downloads/Bike_Sales_2021.csv")
print(df)
# data cleaning
df['Revenue'] = df['Revenue'].str.replace('[$,]', '', regex = True).astype(float)
df['Unit_Cost'] = df['Unit_Cost'].str.replace('[$,]', '', regex = True).astype(float)
df['Unit_Price'] = df['Unit_Price'].str.replace('[$,]', '', regex = True).astype(float)
df['Profit'] = df['Profit'].str.replace('[$,]', '', regex = True).astype(float)
df['Cost'] = df['Cost'].str.replace('[$,]', '', regex = True).astype(float)
print(df)
print(df.info())

# Exploratory Data Analysis
print(df.head(5))

print(df.info())

print(df.describe())

print(df['Revenue'].corr(df['Order_Quantity']))

print(df['Profit'].corr(df['Order_Quantity']))

print(df['Customer_Age'].corr(df['Order_Quantity']))