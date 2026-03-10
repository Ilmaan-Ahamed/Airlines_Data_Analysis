import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

                        # Data Visualization
# Showing All the Airlines with their Number of Fights in Horzontal Bar Graph
df=pd.read_csv(r"E:\Projects\25'24'23\Data Science\Data Analytics & Visualization\Air Lines Data Analytics\airlines_flights_data.csv")
print("--------- The All Dataset list ---------")
print(df)
print("-------------------")

df['airline'].value_counts(ascending=True).plot.barh( color = ['lightgreen' , 'lightblue'])

plt.title("Airlines with Frequencies")

plt.xlabel(" Number of Flights ")

plt.ylabel(" Airlines ")

plt.show()

# Show Bar Graphs representing the Departure Time & Arrival Time
print("Representing the Departure Time & Arrival Time")
print(df.head())
print()

print("-------------------")

# Show Bar Graphs representing the Departure Time & Arrival Time
print("Representing the Departure Time & Arrival Time")
print(df.head())
print()

print("-------------------")