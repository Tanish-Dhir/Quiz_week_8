import matplotlib.pyplot as plt
import sqlite3
connection=sqlite3.connect("climate.db")
cursor=connection.cursor()



resultco2=cursor.fetchall()

new=[]
years = []
co2 = []
temp = []

cursor.execute("SELECT Year FROM ClimateData")
resultyear=cursor.fetchall()
for d in resultyear:
    years.append(d)
print(years)

cursor.execute("SELECT CO2 FROM ClimateData")
resultco2=cursor.fetchall()
for e in resultco2:
    co2.append(e)
print(resultco2)

cursor.execute("SELECT Temperature FROM ClimateData")
resulttemp=cursor.fetchall()
for f in resulttemp:
    temp.append(f)
print(resulttemp)



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

connection.close()