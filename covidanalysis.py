# ===============================
# COVID DATA ANALYSIS PROJECT
# ===============================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset
# Download from:
# https://www.kaggle.com/sudalairajkumar/covid19-in-india

df = pd.read_csv("covid_vaccine_statewise.csv")

# 3. Basic Info
print("First 5 rows:\n", df.head())
print("\nColumns:\n", df.columns)
print("\nShape:", df.shape)

# 4. Data Preprocessing

# Convert date column
df['Updated On'] = pd.to_datetime(df['Updated On'], dayfirst=True)

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# 5. Data Understanding
print("\nDataset Description:\n", df.describe())

# 6. State-wise First Dose
state_first_dose = df.groupby('State')['First Dose Administered'].max().sort_values(ascending=False)

# 7. State-wise Second Dose
state_second_dose = df.groupby('State')['Second Dose Administered'].max().sort_values(ascending=False)

# 8. Gender-wise Vaccination
male = df['Male (Doses Administered)'].sum()
female = df['Female (Doses Administered)'].sum()

print("\nTotal Male Vaccinated:", male)
print("Total Female Vaccinated:", female)

# ===============================
# 📊 VISUALIZATION
# ===============================

# 1. Top 10 States - First Dose
plt.figure()
state_first_dose.head(10).plot(kind='bar')
plt.title("Top 10 States by First Dose")
plt.xlabel("State")
plt.ylabel("Vaccinations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Top 10 States - Second Dose
plt.figure()
state_second_dose.head(10).plot(kind='bar', color='orange')
plt.title("Top 10 States by Second Dose")
plt.xlabel("State")
plt.ylabel("Vaccinations")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Gender Distribution
plt.figure()
plt.bar(['Male', 'Female'], [male, female])
plt.title("Gender-wise Vaccination")
plt.ylabel("Total Doses")
plt.show()

# 4. Time Series (Total Vaccination Over Time)
df['Total'] = df['Total Doses Administered']

time_series = df.groupby('Updated On')['Total'].sum()

plt.figure()
time_series.plot()
plt.title("Total Vaccination Over Time")
plt.xlabel("Date")
plt.ylabel("Doses")
plt.grid()
plt.show()

# 5. Histogram
plt.figure()
df['Total Doses Administered'].plot(kind='hist', bins=30)
plt.title("Distribution of Total Doses")
plt.xlabel("Doses")
plt.show()

# ===============================
# 📌 INSIGHTS (PRINT)
# ===============================

print("\nTop State (First Dose):", state_first_dose.idxmax())
print("Top State (Second Dose):", state_second_dose.idxmax())

if male > female:
    print("More males vaccinated than females")
else:
    print("More females vaccinated than males")

print("\nProject Completed Successfully ✅")