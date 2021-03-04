import random
import time
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('default')

x_values = []
y_values = []

index = count()

def animate(i):

    data = pd.read_csv('rpidaq-results.csv', delimiter=';',skiprows=1)
    data.columns = ['Timestamp title','Timestamp','CH0 title','CH0','CH1 title','CH1','CH2 title','CH2','CH3 title','CH3','CH4 title','CH4','CH5 title','CH5','CH6 title','CH6','CH7 title','CH7','empty']
    
    max_outlier = 150
    # Removing outliers
    data=data[data['CH0'] <= max_outlier]
    data=data[data['CH1'] <= max_outlier]
    data=data[data['CH2'] <= max_outlier]
    data=data[data['CH3'] <= max_outlier]
    data=data[data['CH4'] <= max_outlier]
    data=data[data['CH5'] <= max_outlier]
    data=data[data['CH6'] <= max_outlier]
    data=data[data['CH7'] <= max_outlier]

    x_values = data['Timestamp']
    plt.cla()
    plt.plot(x_values, data['CH0'], label='CH0', ms=1)
    plt.plot(x_values, data['CH1'], label='CH1', ms=1)
    plt.plot(x_values, data['CH2'], label='CH2', ms=1)
    plt.plot(x_values, data['CH3'], label='CH3', ms=1)
    plt.plot(x_values, data['CH4'], label='CH4', ms=1)
    plt.plot(x_values, data['CH5'], label='CH5', ms=1)
    plt.plot(x_values, data['CH6'], label='CH6', ms=1)
    plt.plot(x_values, data['CH7'], label='CH7', ms=1)
    
    plt.xlabel('Timestamp (epoch)')
    plt.ylabel('Temperature (°C)')
    plt.title('Thermocouple readout')
    plt.legend(loc='upper left')
    plt.grid('on')
    
    
    # time.sleep(10)

ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()