import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get indexes
    DATE_INDEX = header_row.index('DATE')
    HIGH_INDEX = header_row.index('TMAX')
    LOW_INDEX = header_row.index('TMIN')

    # Get date and high and low temperatures from this file.
    dates, highs, lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[DATE_INDEX], '%Y-%m-%d')
        high = int(row[HIGH_INDEX])
        low = int(row[LOW_INDEX])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperature.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formate plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

    
