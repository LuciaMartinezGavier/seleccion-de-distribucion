from numpy import histogram_bin_edges, exp
from parse_sample import parse_sample
from scipy.stats import lognorm, gamma, chi2
from estimations import estimate_log_normal, estimate_gamma
import matplotlib.pyplot as plt
from math import sqrt
from numpy import loadtxt

def p_value_gamma(sample):
    # frequency, and interval edges
    N, bins, _ = plt.hist(sample, bins=16)
    n = len(sample)
    k = len(bins) - 1
    a, theta = estimate_gamma(sample)

    rv = gamma(a = a, scale = theta)
    t = (N[0] - rv.cdf(bins[1])*n )**2 / (rv.cdf(bins[1]) * n)
    for i in range(1,k - 1):
        p_i = rv.cdf(bins[i+1]) - rv.cdf(bins[i])
        t = t + (N[i] - n*p_i)**2 / (n * p_i)
    p_j = 1 - rv.cdf(bins[-2])
    t = t + (N[len(N) - 1] - n*p_j)**2 / (n*p_j)
    print("Estadistico Gamma: ", t)
    print(f"p-valor Gamma : {1 - chi2.cdf(t, k - 3)}")

def p_value_lognormal(sample):
    # frequency, and interval edges
    N, bins, _ = plt.hist(sample, bins=16)
    n = len(sample)
    k = len(bins) -1
    mu, sigma = estimate_log_normal(sample)

    rv = lognorm(s=sigma, scale=exp(mu))
    t = (N[0] - rv.cdf(bins[1])*n )**2 / (rv.cdf(bins[1]) * n)
    for i in range(1,k - 1):
        p_i = rv.cdf(bins[i+1]) - rv.cdf(bins[i])
        t = t + (N[i] - n*p_i)**2 / (n * p_i)
    p_j = 1 - rv.cdf(bins[-2])
    t = t + (N[len(N) - 1] - n*p_j)**2 / (n*p_j)

    print("Estadistico Lognormal ", t)
    print(f"p-valor Lognormal : {1 - chi2.cdf(t, 13)}")


sample = parse_sample("../sample23.dat")
p_value_gamma(sample)
p_value_lognormal(sample)

