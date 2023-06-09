import matplotlib.pyplot as plt
import numpy as np
from parse_sample import parse_sample
from scipy.stats import lognorm, gamma
from scipy.special import digamma, polygamma
from math import log, sqrt


# Return the log normal maximum likelihood estimators
def estimate_log_normal(data):
    n = len(data)
    mu = sum(np.log(data))/n
    sigma = sum(list(map(lambda x: (log(x) - mu)**2, data)))
    return mu, sqrt(sigma/n)

# Return an approximation of the Gamma maximum likelihood estimators
# Note: scale and shape parametrization is used
def estimate_gamma(data):
    n = len(data)
    x_bar = sum(data)/n
    lnx_bar = sum(np.log(data))/n
    a_i = 0.5/(log(x_bar) - lnx_bar)
    x_i = 1/a_i + (lnx_bar - log(x_bar) + log(a_i) - digamma(a_i))/(a_i**2 * (1/a_i - polygamma(1,a_i)))

    for i in range(4):
        a_i = 1/x_i
        x_i = 1/a_i + (lnx_bar - log(x_bar) + log(a_i) - digamma(a_i))/(a_i**2 * (1/a_i - polygamma(1,a_i)))

    beta = x_bar/a_i
    return  1/x_i,beta

def plot_histogram_with_distr(values):
    # Create the histogram
    n, bins, patches = plt.hist(values, bins='auto', edgecolor='white')

    # Calculate the bin widths
    bin_widths = bins[1:] - bins[:-1]

    # Calculate the area under the histogram bars
    histogram_area = np.sum(n * bin_widths)

    # Overlay gamma distribution
    a, b = estimate_gamma(values)
    x = np.linspace(0, max(values), 100)
    pdf = gamma.pdf(x, a, loc=0, scale=b)
    pdf_scaled = pdf * histogram_area  # Scale the PDF to match histogram frequency
    plt.plot(x, pdf_scaled, lw=2, label='Gamma')

    # Overlay lognormal distribution
    u, sigma = estimate_log_normal(values)
    x = np.linspace(0, max(values), 100)
    pdf = lognorm.pdf(x, s=sigma, loc=0, scale=np.exp(u))
    pdf_scaled = pdf * histogram_area  # Scale the PDF to match histogram frequency
    plt.plot(x, pdf_scaled, lw=2, label='Lognormal')

    # Set plot properties
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma y distribuciones Gamma y Log Normal')
    plt.legend()

    plt.savefig("../plots/histogram_with_estimated_distributions")
    plt.clf()

plot_histogram_with_distr(parse_sample("../sample23.dat"))
