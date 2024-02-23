import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

# Directory containing text files
directory = "C:/Users/vijay/Downloads/data (2)/data"

# List of major cities
cities_list = ['Pune', 'Srinagar', 'Chennai', 'Shillong', 'Howrah', 'Bhubaneswar', 'Bengaluru', 'Delhi', 'Shimla',
               'Lucknow', 'Bhopal', 'Kolkata', 'Nagpur', 'Guwahati', 'Jaipur', 'Ahmedabad', 'Hyderabad', 'Mumbai',
               'Bangalore']

# Display options for cities
print("Select a city to plot:")
for i, city in enumerate(cities_list):
    print(f"{i + 1}. {city}")

# Get user input for city selection
selected_city_index = int(input("Enter the number corresponding to the city: "))
if selected_city_index < 1 or selected_city_index > len(cities_list):
    print("Invalid input! Please enter a number within the provided range.")
    exit()

selected_city = cities_list[selected_city_index - 1]


# Function to extract city temperatures from a text file
def extract_city_temperatures(file_path, city):
    with open(file_path, "r") as file:
        sample_data = file.read()

    city_temperature = None
    for match in re.finditer(rf'{city}.*?(\d+).*?degrees Celsius', sample_data):
        temperature = int(match.group(1))
        if temperature != 0:
            city_temperature = temperature
        elif city_temperature is not None:
            break  # If zero temperature encountered, break and use the previous valid temperature
    return city_temperature


# Initialize lists to store dates and temperatures for the selected city
dates = []
city_temperatures = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Extract date from file name
        date_str = filename.split('.')[0]  # Remove the '.txt' extension
        day, month, year = map(int, date_str.split('-'))
        date = datetime(year, month, day).date()
        dates.append(date)

        file_path = os.path.join(directory, filename)
        temperature = extract_city_temperatures(file_path, selected_city)
        city_temperatures.append(temperature)

# Plot temperatures for the selected city
plt.plot(dates, city_temperatures, marker='o')
plt.title(f'Temperatures in {selected_city}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
