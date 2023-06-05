import matplotlib.pyplot as plt
from scipy.stats import gamma, lognorm, weibull_min, chi
import numpy as np
from parse_sample import parse_sample

def plot_histogram_with_distr(values):
    # Create the histogram
    n, bins, patches = plt.hist(values, bins=20, edgecolor='white')

    # Calculate the bin widths
    bin_widths = bins[1:] - bins[:-1]

    # Calculate the area under the histogram bars
    histogram_area = np.sum(n * bin_widths)

    # Overlay gamma distribution
    shape, loc, scale = gamma.fit(values, floc=0)
    x = np.linspace(0, max(values), 100)
    pdf = gamma.pdf(x, shape, loc=loc, scale=scale)
    pdf_scaled = pdf * histogram_area  # Scale the PDF to match histogram frequency
    plt.plot(x, pdf_scaled, lw=2, label='Gamma')


    # Overlay log-normal distribution
    shape, loc, scale = lognorm.fit(values)
    x = np.linspace(min(values), max(values), 100)
    pdf = lognorm.pdf(x, shape, loc=loc, scale=scale) * histogram_area
    plt.plot(x, pdf, lw=2, label='Log-Normal', color='pink')

    # Overlay weibull distribution
    shape, loc, scale = weibull_min.fit(values, floc=0)
    x = np.linspace(min(values), max(values), 100)
    pdf = weibull_min.pdf(x, shape, loc=loc, scale=scale) * histogram_area
    plt.plot(x, pdf, lw=2, label='Weibull', color='yellow')

    # Overlay chi distribution
    df, loc, scale = chi.fit(values)
    x = np.linspace(min(values), max(values), 100)
    pdf = chi.pdf(x, df, loc=loc, scale=scale) * histogram_area
    plt.plot(x, pdf, lw=2, label='Chi', color='lightgreen')

    # Set plot properties
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma y distribuciones Gamma y Log Normal')
    plt.legend()



    # Show the plot
    plt.savefig("../plots/histogram_with_distributions")
    plt.clf()

def plot_histogram(values):
    # Create the histogram
    plt.hist(values, bins=20, edgecolor='white')

    # Set plot properties
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')

    # Show the plot
    plt.savefig("../plots/histogram")
    plt.clf()

# Usage example
values = parse_sample('../sample23.dat')
plot_histogram_with_distr(values)
plot_histogram(values)
