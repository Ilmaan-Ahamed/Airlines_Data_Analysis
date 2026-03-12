# ✈️ Airlines Flights Data Analytics

## 📌 Project Overview
This project performs **data cleaning, exploratory data analysis (EDA), and visualization**
on an airline flights dataset using Python.

The goal of the analysis is to understand:

- Airline flight frequencies
- Ticket price trends
- Flight timing vs price relationships
- Flight traffic between cities

---

## 📊 Dataset

Dataset file:

`airlines_flights_data.csv`

### Dataset Columns

| Column | Description |
|------|-------------|
| airline | Airline name |
| source_city | Departure city |
| destination_city | Arrival city |
| departure_time | Flight departure time |
| arrival_time | Flight arrival time |
| duration | Flight duration |
| price | Ticket price |
| class | Travel class |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 🧹 Data Cleaning

Data preprocessing steps performed:

1. Removed unnecessary column `index`
2. Checked dataset structure
3. Generated statistical summary
4. Checked missing values
5. Verified dataset records

### Example

```python
df.drop(columns='index', inplace=True)
df.info()
df.describe()
df.isnull().sum()
df.head()
```

---

## 🔍 Exploratory Data Analysis

### Airline Analysis

- Count number of airlines
- Display airline names
- Calculate flight frequency

```python
df['airline'].value_counts()
df['airline'].unique()
df['airline'].nunique()
```

---

### 💰 Price Analysis

Identify:

- Highest ticket prices
- Lowest ticket prices
- Average ticket prices by airline

```python
df.groupby('airline')['price'].mean()
```

---

### ⏱ Duration Analysis

Filter flights based on duration:

```python
df[df['duration'] == 49.83]

df[df['duration'] == 0.83]
```

---

## 📈 Data Visualization

### 1️⃣ Airline Flight Frequency

```python
df['airline'].value_counts().plot.barh()
```

### 2️⃣ Source vs Destination Cities

```python
plt.subplot(1,2,1)
plt.bar(df['source_city'].value_counts().index,
        df['source_city'].value_counts().values)

plt.subplot(1,2,2)
plt.bar(df['destination_city'].value_counts().index,
        df['destination_city'].value_counts().values)
```

### 3️⃣ Ticket Price by Airline

```python
sns.catplot(
    x='airline',
    y='price',
    kind='bar',
    data=df,
    hue='class'
)
```

### 4️⃣ Ticket Price vs Departure Time

```python
sns.catplot(
    x='departure_time',
    y='price',
    kind='bar',
    data=df
)
```

### 5️⃣ Ticket Price vs Arrival Time

```python
sns.catplot(
    x='arrival_time',
    y='price',
    kind='bar',
    data=df
)
```

---

## 📊 Key Insights

- Some airlines operate **more flights than others**
- Ticket prices vary by **airline and class**
- **Departure and arrival time influence pricing**
- Major cities dominate airline traffic

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/Ilmaan-Ahamed/Airlines_Data_Analysis.git
```

### 2. Install Libraries

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
```

### 3. Run Script

```bash
python Air_Analysis.py
python Air_Visualization.py
```

---

## 📁 Project Structure

```
Airlines-Data-Analytics
│
├── airlines_flights_data.csv
├── Air_Analysis.py
├── Air_Visualization.py
├── README.md
│
└── images
    ├── Air_Arrival time.png
    ├── Air_Class.png
    └── Air_Departure time.png
    ├── Air_Source City & Destination City.png
    ├── Air_Class.png
    └── Air_Departure time.png
```

---

## 🚀 Future Improvements

- Add **Machine Learning model for ticket price prediction**
- Build **Streamlit web dashboard**

---

## 👨‍💻 Author

**Ilmaan Ahamed**  
Software Engineering Undergraduate  
SLTC Research University
