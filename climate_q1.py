import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

sqlCommand = "SELECT * FROM ClimateData"

cursor.execute(sqlCommand)
rows = cursor.fetchall()


years = []
co2 = []
temp = []

for row in rows:
    year, amountOfCO2, temperature = row
    years.append(year)
    co2.append(amountOfCO2)
    temp.append(temperature)


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

connection.commit()
connection.close()