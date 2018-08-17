# http://matplotlib.1069221.n5.nabble.com/drawing-secondary-x-axis-for-months-a-better-way-td39330.html
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as m_dates
import matplotlib.ticker as ticker

def make_month_axis(dates, y, ax, fig):

    newax = fig.add_axes(ax.get_position())
    newax.spines['bottom'].set_position(('outward', 25))
    newax.patch.set_visible(False)
    newax.yaxis.set_visible(False)
    newax.plot_date(dates, y, visible=False)

    newax.xaxis.set_major_locator(m_dates.MonthLocator())
    newax.xaxis.set_minor_locator(m_dates.MonthLocator(bymonthday=15))

    newax.xaxis.set_major_formatter(ticker.NullFormatter())
    newax.xaxis.set_minor_formatter(m_dates.DateFormatter('%b'))

    for tick in newax.xaxis.get_minor_ticks():
        tick.tick1line.set_markersize(0)
        tick.tick2line.set_markersize(0)
        tick.label1.set_horizontalalignment('center')


start = datetime.datetime(2012, 8, 26)
dates = [start]
for i in range(1,10):
    dates.append(dates[-1] + datetime.timedelta(days=7))
y = np.random.normal(10, 5, len(dates))
fig = plt.figure()
fig.subplots_adjust(bottom=0.2, right=0.85, wspace=.8, hspace=.8)
ax = fig.add_subplot(1,1,1)
ax.plot(dates, y)
ax.xaxis.set_major_formatter( matplotlib.dates.DateFormatter('%W'))
make_month_axis(dates = dates, y = y, ax = ax, fig = fig)

plt.show()
