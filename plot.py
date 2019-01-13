import sys
import numpy as np
import matplotlib.pyplot as plt

from plotFunctions import scatter, plot, histo, learning_curves

filename = sys.argv[1]
plt.grid(True)

plot_args = {'xlabel' : 'x-axis',
					'ylabel' : 'y-axis',
					'fs' : 35,
					'ls' : 25,
					'ms' : 15,
					's' : 75,
					'lw' : 2,
					'col' : 'red',
					'linestyle' : 'dashed',
					'marker' : 'o',
					'kde' : False,
					'bins' : None,
					'numSubplots_x' : 2,
					'numSubplots_y' : 2}

def get_data(filename):
	lines = open(filename).readlines()

	col1 = np.array([])
	col2 = np.array([])
	col3 = np.array([])

	for line in lines:
		col1 = np.append(col1, float(line.split()[0]))

		try: col2 = np.append(col2, float(line.split()[1]))
		except: continue 

		try: col3 = np.append(col3, float(line.split()[2]))
		except: continue

	return [col1, col2, col3]


if __name__ == "__main__":

	data = get_data(filename)

	#scatter(data,plot_args)
	#plot(data,plot_args)
	#histo(data,plot_args)
	learning_curves(data,plot_args)

