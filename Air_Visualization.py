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

# Show Bar Graphs representing the Source City & Destination City
print(" Show Bar Graphs representing the Source City & Destination City")
print(df['source_city'].value_counts())
print()

print("-------------------")

# Show the Source City & Destination City 
plt.figure(figsize=(16,4))

plt.subplot(1,2,1)
plt.bar(df['source_city'].value_counts().index,
        df ['source_city'].value_counts().values ,color=['r' , 'b'])

plt.title("Source City with No. of Flights ")
plt.ylabel("Cities")
plt.xlabel("No. of flights")

plt.subplot(1,2,2)

plt.bar(df['destination_city'].value_counts().index,
        df['destination_city'].value_counts().values , color=['m' , 'g'])

plt.title("Destination_city with No. of Flights ")
plt.ylabel("Cities")
plt.xlabel("No. of flights")

plt.show()



# Grouping the Price varies with airlines 
print("Price varies with airlines ")
df_Pricegrouped = df.groupby('airline')['price'].mean()
print(df_Pricegrouped)
print()

print("-------------------")


# Drawing a Categorical Plot showing the Mean Ticket Price for each Airline

sns.catplot( x = 'airline', y = 'price', kind = 'bar', palette = 'rocket', data = df, hue = 'class')

plt.show()

# Grouping the Mean Ticket Price based on the Departure times
print("Mean Ticket Price based on the Departure times")
df_Deptgrouped = df.groupby('departure_time')['price'].mean()
print(df_Deptgrouped)
print()

print("-------------------")

# Grouping the Mean Ticket Price based on the  Arrival Times
print("Mean Ticket Price based on the Departure times")
df_Arivagrouped = df.groupby('arrival_time')['price'].mean()
print(df_Arivagrouped)
print()

print("-------------------")

# Drawing a Categorical Plot showing the Mean Ticket Price  for each Departure time 
sns.catplot(x='departure_time', y ='price', kind= 'bar',  data= df)
plt.show()

# Drawing a Categorical Plot showing the Mean Ticket Price  for each Arriaval time 
sns.catplot(x='arrival_time', y ='price', kind= 'bar',  data= df)
plt.show()