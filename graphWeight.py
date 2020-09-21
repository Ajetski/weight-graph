import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

df = pd.read_csv('Weight.csv')

fig, ax = plt.subplots()

dates = [datetime.strptime(date, '%m/%d/%y') for date in df["Date"].values]

weights = df["Weight"].values

plt.plot(dates, weights)

ax.set(xlabel='Time (date)', ylabel='Weight (lbs)',
       title='Weight vs Time')

fig.canvas.set_window_title('Weight Graph') 

ax.xaxis.set_major_formatter(mdates.DateFormatter('%D'))

fig.autofmt_xdate()

plt.show()