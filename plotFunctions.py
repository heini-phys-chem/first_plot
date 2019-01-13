import numpy as np
import matplotlib.pyplot as plt

def scatter(data,plot_args):
	plt.scatter(data[0], data[1], marker=plot_args['marker'], s=plot_args['s'], color=plot_args['col'])

	plt.xlabel(plot_args['xlabel'], fontsize=plot_args['fs'])
	plt.ylabel(plot_args['ylabel'], fontsize=plot_args['fs'])

	plt.tick_params(axis='both', labelsize=plot_args['ls'])

	plt.show()

def plot(data,plot_args):
	plt.plot(data[0], data[1], marker=plot_args['marker'], markersize=plot_args['ms'], color=plot_args['col'])

	plt.xlabel(plot_args['xlabel'], fontsize=plot_args['fs'])
	plt.ylabel(plot_args['ylabel'], fontsize=plot_args['fs'])

	plt.tick_params(axis='both', labelsize=plot_args['ls'])

	plt.show()

def histo(data,plot_args):
	plt.hist(data[0], density=plot_args['kde'], bins=plot_args['bins'])

	plt.xlabel(plot_args['xlabel'], fontsize=plot_args['fs'])
	plt.ylabel(plot_args['ylabel'], fontsize=plot_args['fs'])

	plt.tick_params(axis='both', labelsize=plot_args['ls'])

	plt.show()

def learning_curves(data,plot_args):
	plt.plot(data[0], data[1], marker=plot_args['marker'], markersize=plot_args['ms'], color=plot_args['col'])

	plt.xlabel(plot_args['xlabel'], fontsize=plot_args['fs'])
	plt.ylabel(plot_args['ylabel'], fontsize=plot_args['fs'])

	plt.xscale("log")
	plt.yscale("log")

	plt.tick_params(axis='both', labelsize=plot_args['ls'])

	plt.show()

def subplots(data):
	return 1.0

