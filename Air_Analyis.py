import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"E:\Projects\25'24'23\Data Science\Data Analytics & Visualization\Air Lines Data Analytics\airlines_flights_data.csv")
print("--------- The All Dataset list ---------")
print(df)
print("-------------------")

                    # Cleaning the data 

df.drop( columns= 'index' , inplace=True)
print(df.drop)
print("-------------------")

# Get Statistical summary about the dataset
print("--------- Get Statistical summary about the dataset ---------")
print(df.describe)
print("-------------------")

# A List By Duration
print(" --------- A List By Duration ---------")
print(df[df ['duration'] == 49.830000])
print()

print(df[df ['duration'] == 0.830000])
print()

print("-------------------")

# A List By Pirce
print(" --------- A List By Price ---------")
print(df[df['price'] == 123071.000000])
print()

print(df[df['price'] == 1105.000000])
print()
print("-------------------")

# Check Missing Values in any Column 
print("--------- Check Missing Values in any Column ---------")
print(df.isnull().sum())
print()

print("-------------------")

# Get frist 5 datas
print(" --------- Get frist 5 datas ---------")
print(df.head())
print()

print("-------------------")

# Checking how many Airlines are in the dataset
print(" --------- Checking how many Airlines are in the dataset ---------")
print(df['airline'].nunique())
print()

print("-------------------")

# Show how many Airlines Names are in the dataset
print("--------- Show how many Airlines Names are  in the dataset ---------")
print(df['airline'].unique())
print()

print("-------------------")

# Showing All the Airlines with their Frequencies
print("--------- Showing All the Airlines with their Frequencies ---------")
print(df['airline'].value_counts())
print()

print("--------- The Data Cleaning work is Done  ----------")
