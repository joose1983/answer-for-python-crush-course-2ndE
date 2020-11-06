import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_sitka = 'sitka_weather_2018_simple.csv'
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and high and low temperatures from this file.
    dates_sitka, highs_sitka, lows_sitka = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates_sitka.append(current_date)
        highs_sitka.append(high)
        lows_sitka.append(low)

filename_deathvalley = 'death_valley_2018_simple.csv'
with open(filename_deathvalley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and high and low temperatures from this file.
    dates_deathvalley, highs_deathvalley, lows_deathvalley = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_deathvalley.append(current_date)
            highs_deathvalley.append(high)
            lows_deathvalley.append(low)

# Plot the high and low temperature.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, c='red', alpha=0.5)
ax.plot(dates_sitka, lows_sitka, c='blue', alpha=0.5)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

ax.plot(dates_deathvalley, highs_deathvalley, c='purple', alpha=0.5)
ax.plot(dates_deathvalley, lows_deathvalley, c='green', alpha=0.5)
plt.fill_between(dates_deathvalley, highs_deathvalley, lows_deathvalley, facecolor='green', alpha=0.1)

# Formate plot.
plt.legend(('Stika high', 'Stika low', 'Death Valley high', 'Death Valley low'), loc='upper right') 
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

    
