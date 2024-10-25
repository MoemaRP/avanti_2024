import numpy as np
import matplotlib as mpl ## matplotlib
import matplotlib.pyplot as plt ##atplotlib.pyplot
x = np.linspace(-2 * np.pi, 2 * np.pi, 100) #linspace
y = np.sin(x) #sin
fig, ax = plt.subplots() #fig, ax
ax.plot(x, y) #x, y