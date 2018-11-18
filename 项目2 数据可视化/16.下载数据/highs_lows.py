import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)

  # for index, column_header in enumerate(header_row):
    # print(index, column_header)

  dates, highs, lows = [], [], []
  for row in reader:
    try:
      current_date = datetime.strptime(row[0], "%Y-%m-%d")
      high = int(row[1])
      low = int(row[3])
    except ValueError:
      print(current_date, 'Missing date')
    else:
      highs.append(high)
      lows.append(low)
      dates.append(current_date)
  
  # print(highs)
  fig = plt.figure(dpi=128, figsize=(10, 6))
  plt.plot(dates, highs, c='red', alpha=0.5)
  plt.plot(dates, lows, c='blue', alpha=0.5)
  plt.fill_between(dates,highs, lows, facecolor='blue', alpha=0.1)

  plt.title('Daily high and low temperatures, 2014\nDeath Valley, CA', fontsize=24)
  plt.xlabel('', fontsize=16)
  plt.ylabel('Temperature(F)', fontsize=16)
  plt.tick_params(axis='bold', which='major', labelsize=16)
  fig.autofmt_xdate()

  plt.show()