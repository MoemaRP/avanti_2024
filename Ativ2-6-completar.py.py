import matplotlib.pyplot as plt  ##matplotlib
import numpy as np  ##np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
                        layout="constrained")
for row in range(2): ##row
    for col in range(2): ##col
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18, ##frontzize
                               color='darkgrey')
fig.suptitle('plt.subplots()') ##plt