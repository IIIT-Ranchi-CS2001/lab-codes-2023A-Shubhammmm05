#Load the data set using pandas and perform following:
#a)display first 5 rows
#b)display the last 6 rows
#c)show the summary statistics for all numeric columns
#d)use numpy to compute the AQI,PM2.5 and PM10 values for each city.
#Make sure your code is well commented and use print statements to explain the output e.g
##Display first 5 rows
#print("First 5 rows of the datset")
#
#Filter and display all rows where PM2.5 level exceeds 100(unhealthy levels).
#Count how many such rows exist for each city.
#    [You are not allowed to use value_counts() method of pandas .You may however use dictionary and for loop though.]
# Importing necessary libraries
# Importing necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\PYTHON_LAB\lab-codes-2023A-Shubhammmm05\PYTHON\AQI_Data.csv"  # Update with the correct path if needed
data = pd.read_csv(file_path)

# a) Display the first 5 rows of the dataset
print("# Display the first 5 rows of the dataset")
print(data.head(5))

# b) Display the last 6 rows of the dataset
print("\n# Display the last 6 rows of the dataset")
print(data.tail(6))

# c) Show the summary statistics for all numeric columns
print("\n# Summary statistics for all numeric columns")
print(data.describe())

# d) Compute the AQI, PM2.5, and PM10 values for each city using numpy
print("\n# Compute the AQI, PM2.5, and PM10 values for each city using numpy")

# Get the unique cities
cities = data['City'].unique()

# Initialize dictionaries to store aggregated values
city_aqi = {}
city_pm25 = {}
city_pm10 = {}

# Use numpy to compute the mean for each city
for city in cities:
    city_data = data[data['City'] == city]  # Filter rows for the city
    city_aqi[city] = np.mean(city_data['AQI'].values)
    city_pm25[city] = np.mean(city_data['PM2.5'].values)
    city_pm10[city] = np.mean(city_data['PM10'].values)

# Display results
print("City-wise averages for AQI, PM2.5, and PM10:")
for city in cities:
    print(f"{city}: AQI={city_aqi[city]:.2f}, PM2.5={city_pm25[city]:.2f}, PM10={city_pm10[city]:.2f}")

# Filter and display all rows where PM2.5 level exceeds 100
print("\n# Filter rows where PM2.5 level exceeds 100 (unhealthy levels)")
unhealthy_pm25 = data[data['PM2.5'] > 100]
print(unhealthy_pm25)

# Count how many such rows exist for each city using dictionary and loop
print("\n# Count of rows where PM2.5 exceeds 100 for each city")
city_unhealthy_count = {}

for index, row in unhealthy_pm25.iterrows():
    city = row['City']
    if city in city_unhealthy_count:
        city_unhealthy_count[city] += 1
    else:
        city_unhealthy_count[city] = 1

# Display the counts for each city
for city, count in city_unhealthy_count.items():
    print(f"{city}: {count}")

# Count the number of cities where PM2.5 exceeds 100 at least once
print("\n# Count of cities where PM2.5 exceeds 100 at least once")
count_cities = len(city_unhealthy_count)
print(f"Number of cities with PM2.5 levels exceeding 100: {count_cities}")
