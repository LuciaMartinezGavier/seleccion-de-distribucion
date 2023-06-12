from numpy import histogram_bin_edges, exp
from parse_sample import parse_sample
from scipy.stats import lognorm, gamma, chi2
from estimations import estimate_log_normal, estimate_gamma
import matplotlib.pyplot as plt
from math import sqrt

def p_value_gamma(data):
    # frequency, and interval edges
    N, bins, _ = plt.hist(parse_sample("../sample23.dat"), bins=16)
    k = len(bins) - 1
    n = len(data)
    a, theta = estimate_gamma(data)

    p_i = gamma.cdf(bins[1], a, scale=theta)
    t = ((N[0] - n*p_i))**2 / (n*p_i)
    for i in range(1, k):
        F_a = gamma.cdf(bins[i], a, scale=theta)
        F_b = gamma.cdf(bins[i+1], a, scale=theta)
        p_i = F_b - F_a
        t += ((N[i] - n*p_i))**2 / (n*p_i)
    p_i = 1 - gamma.cdf(bins[k-1], a, scale=theta)
    t += ((N[k-1] - n*p_i))**2 / (n*p_i)
    return 1 - chi2.cdf(t,k-1)

def p_value_lognormal(data):
    # frequency, and interval edges
    N, bins, _ = plt.hist(parse_sample("../sample23.dat"), bins=16)
    k = len(bins) - 1
    n = len(data)
    mu, sigma = estimate_log_normal(data)

    p_i = lognorm.cdf(bins[1], s=sigma, scale=exp(mu))
    t = ((N[0] - n*p_i))**2 / (n*p_i)
    for i in range(1,k):
        F_a = lognorm.cdf(bins[i], s=sigma, scale=exp(mu))
        F_b = lognorm.cdf(bins[i+1], s=sigma, scale=exp(mu))
        p_i = F_b - F_a
        t += ((N[i] - n*p_i))**2 / (n*p_i)
    p_i = 1 - lognorm.cdf(bins[k-1], s=sigma, scale=exp(mu))
    t += ((N[k-1] - n*p_i))**2 / (n*p_i)

    return 1 - chi2.cdf(t,k-1)

print ("lognormal: ", p_value_lognormal(parse_sample("../sample23.dat")))
print ("gamma: ", p_value_gamma(parse_sample("../sample23.dat")))
