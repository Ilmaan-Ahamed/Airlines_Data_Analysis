import numpy as np 
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# load DataSet
df=pd.read_csv(r"E:\Projects\25'24'23\Data Science\Data Analytics & Visualization\Air Lines Data Analytics\airlines_flights_data.csv")
print("--------- The All Dataset list ---------")

# Check Data info
print(df.info)