import sqlite3
import matplotlib.pyplot as plt

weatherdata = """SELECT Year, CO2, Temperature FROM ClimateData"""

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Fetch data from the database and populate Python lists
years = []
co2 = []
temp = []

# Year, CO2, and Temperature
cursor.execute(weatherdata)
rows = cursor.fetchall()

for row in rows:
    year, co2_value, temp_value = row
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

# Close the database connection
conn.close()

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

# Saving the figure
plt.savefig("co2_temp_1.png")

# Displaying the plot
plt.show()
