import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and high and low temperatures from this file.
    dates, rainfalls = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[3])
        dates.append(current_date)
        rainfalls.append(rainfall)

# Plot the high and low temperature.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='blue')

# Formate plot.
plt.title("Daily rainfall - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall(inch)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
