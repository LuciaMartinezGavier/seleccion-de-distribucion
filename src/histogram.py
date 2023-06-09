import matplotlib.pyplot as plt
from scipy.stats import gamma, lognorm, weibull_min, chi
import numpy as np
from parse_sample import parse_sample

def plot_histogram(values):
    # Create the histogram
    plt.hist(values, bins='auto',  density=True, edgecolor='white')

    # Set plot properties
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')

    # Show the plot
    plt.savefig("../plots/histogram")
    plt.clf()

# Usage example
values = parse_sample('../sample23.dat')
plot_histogram(values)
