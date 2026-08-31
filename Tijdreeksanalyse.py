import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('city_temperature.csv', low_memory=False)


#Eerst filteren op 1 stad.
df_stad = df[df['City'] == 'Amsterdam'].copy()

#Hier zorg ik ervoor dat de fout metingen eruit gehaald worden.
df_stad = df_stad[df_stad['AvgTemperature'] > -99]

#Hier de berekening om van Fahrenheit naar Celsius te gaan.
df_stad['Temp_C'] = (df_stad['AvgTemperature'] - 32) * 5 / 9

#Hier maak ik van de datum een index zodat pandas optimaal kan werken.
df_stad['Datum'] = pd.to_datetime(df_stad[['Year', 'Month', 'Day']])
df_stad.set_index('Datum', inplace=True)
df_stad.sort_index(inplace=True)

#De trend over de tijd van 30 dagen.
df_stad['MA_30'] = df_stad['Temp_C'].rolling(window=30).mean()

gemiddelde = df_stad['Temp_C'].mean()
standaarddeviatie = df_stad['Temp_C'].std()

#Hier leg ik de grens
bovengrens = gemiddelde + (3 * standaarddeviatie)
ondergrens = gemiddelde - (3 * standaarddeviatie)

#Filter de rijen die buiten de grenzen vallen
uitschieters = df_stad[(df_stad['Temp_C'] > bovengrens) | (df_stad['Temp_C'] < ondergrens)]

#Het visualiseren van de data
plt.figure(figsize=(12, 6))


plt.plot(df_stad.index, df_stad['Temp_C'], alpha=0.3, label='Dagtemperatuur')
plt.plot(df_stad.index, df_stad['MA_30'], color='red', label='30-daags rollend gemiddelde')

#De uitschieters toevoegen als stippen in de grafiek.
plt.scatter(uitschieters.index, uitschieters['Temp_C'], color='black', s=20, label='Uitschieters')

plt.title('Tijdreeksanalyse Temperatuur Amsterdam')
plt.xlabel('Datum')
plt.ylabel('Temperatuur (°C)')
plt.legend()
plt.grid(True)
plt.show()
