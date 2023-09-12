import matplotlib.pyplot as plt
import pandas as pd

# Load data from a CSV file into a Pandas DataFrame
data = pd.read_csv('climate.csv')

# Extract data into separate lists
years = data['Year']
co2 = data['CO2']
temp = data['Temperature']

# Create subplots and plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

# Show the plot
plt.show()

# Saving the figure after showing
plt.savefig("co2_temp_2.png")

