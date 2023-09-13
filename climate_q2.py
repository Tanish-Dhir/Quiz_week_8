import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv(r"climate.csv")


years = []
co2 = []
temp = []

for b in df["Year"]:
    years.append(b)

for a in df["CO2"]:
    co2.append(a)

for c in df["Temperature"]:
    temp.append(c)



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
plt.savefig("co2_temp_2.png") 

