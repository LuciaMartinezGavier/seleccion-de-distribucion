import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, gamma
from parse_sample import parse_sample
from estimations import estimate_gamma, estimate_log_normal


def plot_histogram_with_overlay(sample, density_func, distr):
    # Plotting the histogram of the input array
    hist, bins, _ = plt.hist(sample, density=True, bins='auto', alpha=0.7,color='magenta', label='muestra', edgecolor='white')

    # Generating x values for the density function
    x = np.linspace(min(sample), max(sample), 100)

    # Calculating y values using the density function
    y = density_func(x)

    # Scaling the y values to match the histogram
    hist_max = np.max(hist)
    y_max = np.max(y)
    y = y * hist_max / y_max

    # Overlaying the histogram of the density function
    plt.hist(x, bins=bins, density=True, alpha=0.3, color='cyan', edgecolor='white', label=distr, weights=y)

    # Plot settings
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.savefig('../plots/compared_frecuency_'+ distr)
    plt.clf()

sample = parse_sample('../sample23.dat')
alpha, beta = estimate_gamma(sample)
normal_density = lambda x: gamma.pdf(x, alpha, loc=0, scale=beta)
plot_histogram_with_overlay(sample, normal_density, 'gamma')

mu, sigma = estimate_log_normal(sample)
normal_density = lambda x: lognorm.pdf(x, s=sigma, loc=0, scale=np.exp(mu))
plot_histogram_with_overlay(sample, normal_density, 'lognomal')

