✈️ Airlines Flights Data Analytics
📌 Project Overview

This project performs data cleaning, exploration, and visualization on an airline flights dataset using Python Data Analytics libraries.
The goal is to analyze flight data to understand airline frequencies, pricing trends, and relationships between flight timings and ticket prices.

The analysis helps identify patterns such as:

Which airlines operate the most flights

Average ticket prices by airline

Price differences based on departure and arrival times

Flight distribution across source and destination cities

📊 Dataset

The dataset used in this project contains airline flight information such as:

Column	Description
airline	Name of the airline
source_city	Departure city
destination_city	Arrival city
departure_time	Flight departure time
arrival_time	Flight arrival time
duration	Flight duration
price	Ticket price
class	Travel class

Dataset file:

airlines_flights_data.csv
🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook / Python Script

Libraries used in the project:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
🧹 Data Cleaning

The following preprocessing steps were performed:

Removed unnecessary column index

Checked dataset structure using .info()

Generated statistical summary using .describe()

Checked missing values using .isnull().sum()

Verified dataset records using .head()

Example:

df.drop(columns='index', inplace=True)
df.info()
df.describe()
🔍 Exploratory Data Analysis (EDA)
Airline Analysis

Counted number of airlines in the dataset

Displayed airline names

Calculated frequency of flights per airline

df['airline'].value_counts()
df['airline'].unique()
df['airline'].nunique()
Price Analysis

The project identifies:

Highest ticket prices

Lowest ticket prices

Average ticket prices by airline

Example:

df.groupby('airline')['price'].mean()
Duration Analysis

Flights were filtered based on duration to identify special cases:

df[df['duration'] == 49.83]
df[df['duration'] == 0.83]
📈 Data Visualization

Several visualizations were created to better understand the data.

1️⃣ Airline Flight Frequency

Horizontal bar chart showing the number of flights operated by each airline.

df['airline'].value_counts().plot.barh()
2️⃣ Source City vs Destination City

Bar charts comparing flight frequencies across cities.

plt.subplot(1,2,1)
plt.bar(df['source_city'].value_counts().index,
        df['source_city'].value_counts().values)

plt.subplot(1,2,2)
plt.bar(df['destination_city'].value_counts().index,
        df['destination_city'].value_counts().values)
3️⃣ Ticket Price by Airline

A categorical plot showing the average ticket price for each airline.

sns.catplot(
    x='airline',
    y='price',
    kind='bar',
    data=df,
    hue='class'
)
4️⃣ Ticket Price vs Departure Time

Visualizing how ticket prices vary depending on departure time.

sns.catplot(x='departure_time', y='price', kind='bar', data=df)
5️⃣ Ticket Price vs Arrival Time

Shows how arrival time impacts ticket prices.

sns.catplot(x='arrival_time', y='price', kind='bar', data=df)
📊 Key Insights

From the analysis:

Certain airlines operate significantly more flights than others.

Ticket prices vary significantly based on airline and travel class.

Departure and arrival times influence ticket pricing.

Major cities dominate flight traffic.

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/airlines-data-analytics.git
2️⃣ Install Required Libraries
pip install pandas numpy matplotlib seaborn
3️⃣ Run the Script
python airline_analysis.py
📁 Project Structure
Airlines-Data-Analytics
│
├── airlines_flights_data.csv
├── airline_analysis.py
├── README.md
└── images
      ├── airline_frequency.png
      ├── city_distribution.png
      └── price_analysis.png
🚀 Future Improvements

Add machine learning models to predict ticket prices

Build an interactive dashboard using Power BI / Tableau

Create a web dashboard using Streamlit

👨‍💻 Author

Ilmaan Ahamed
Software Engineering Undergraduate
SLTC Research University
