# Tijdreeksanalyse Temperatuur Amsterdam

Praktijkopdracht voor de NHA-opleiding Data Analist waarin historische dagtemperaturen van Amsterdam worden geanalyseerd met Python.

## Over het project
Het doel van dit script is om ruwe weerdata op te schonen en de opvallende weerdata te filteren.

### Wat het script doet
* Opschonen: Ontbrekende waarden (-99) verwijderen, omrekenen van Fahrenheit naar Celsius en een geldige datumindex aanmaken.
* Trendanalyse: Een 30-daags rollend gemiddelde (rolling mean) berekenen om dagelijkse ruis weg te filteren en de seizoenslijn te tonen.
* Uitschieters: Dagen markeren die meer dan 3 standaarddeviaties van het gemiddelde afwijken (zoals de koudegolf in 1996/1997 en de hittegolf van 2018/2019).
* Plot: Een grafiek genereren met de dagtemperaturen, trendlijn en uitschieters.

## Gebruikte tools
* Python 3
* Pandas
* Matplotlib

## Gebruik
1. Clone de repository:
   ```bash
   git clone [https://github.com/Archii1999/nha-data-analist-portfolio.git](https://github.com/Archii1999/nha-data-analist-portfolio.git)
