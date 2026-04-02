import numpy as np 
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split

# load DataSet
df=pd.read_csv(r"E:\Projects\25'24'23\Data Science\Data Analytics & Visualization\Air Lines Data Analytics\airlines_flights_data.csv")
print("--------- The All Dataset list ---------")

# Check Data info
print(df.info)

# identify categorical colunms
categorical_cols  = ['airline', 'flight', 'source_city', 'destination_city', 'class', 'price']

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
#  Flight Speed feature  
df['price_per_hour'] = df['price'] / df['duration']

# days Category
df['urgency'] = df['days_left'].apply(lambda x: 1 if x < 5 else 0)

# 4 Separate Features & Target
x = df.drop('price', axis=1)
y = df['price']

# test for ml model 
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2) 

