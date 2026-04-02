import numpy as np 
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# load DataSet
df=pd.read_csv(r"E:\Projects\25'24'23\Data Science\Data Analytics & Visualization\Air Lines Data Analytics\airlines_flights_data.csv")
print("--------- The All Dataset list ---------")

# Check Data info
print(df.info)

# identify categorical colunms
categorical_cols  = ['airline', 'flight', 'source_city', 'destination_city', 'class']

# Apply Lable Encoding 
le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# check Result
print("========= Label Encoding =========")
print(df.head)

# Feature Engineering 
# 1 Drop Unnecesary Columns
df.drop(columns=['index'], inplace=True)\

# 2. create new features 
df['price_per_hour'] = df['pirce'] / df['duration']

df['urgency'] = df['days_left'].apply(lambda x: 1 if x < 5 else 0)