from numpy import histogram_bin_edges, exp
from parse_sample import parse_sample
from scipy.stats import lognorm, gamma, chi2
from estimations import estimate_log_normal, estimate_gamma
import matplotlib.pyplot as plt


def p_value_gamma(data):
    # frequency, and interval edges
    N, bins, _ = plt.hist(parse_sample("../sample23.dat"), bins=9)
    k = len(bins) - 1
    n = len(data)
    a, theta = estimate_gamma(data)

    t = gamma.cdf(bins[0], a, scale=theta)
    for i in range(k):
        F_a = gamma.cdf(bins[i], a, scale=theta)
        F_b = gamma.cdf(bins[i+1], a, scale=theta)
        p_i = F_b - F_a
        t += ((N[i] - n*p_i))**2 / (n*p_i)
    t += 1 - gamma.cdf(bins[k], a, scale=theta)

    return 1 - chi2.cdf(t,k-1)

def p_value_lognormal(data):
    # frequency, and interval edges
    N, bins, _ = plt.hist(parse_sample("../sample23.dat"), bins=9)
    k = len(bins) - 1
    n = len(data)
    mu, sigma = estimate_log_normal(data)

    t = lognorm.cdf(bins[0], s=sigma, scale=exp(mu))
    for i in range(k):
        F_a = lognorm.cdf(bins[i], s=sigma, scale=exp(mu))
        F_b = lognorm.cdf(bins[i+1], s=sigma, scale=exp(mu))
        p_i = F_b - F_a
        t += ((N[i] - n*p_i))**2 / (n*p_i)
    t += lognorm.cdf(bins[k], s=sigma, scale=exp(mu))

    return 1 - chi2.cdf(t,k-1)

print (p_value_lognormal(parse_sample("../sample23.dat")))
print (p_value_gamma(parse_sample("../sample23.dat")))
print (p_value_gamma(parse_sample("../sample23.dat")) -p_value_lognormal(parse_sample("../sample23.dat")) )
