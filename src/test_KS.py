from parse_sample import parse_sample
from estimations import estimate_gamma, estimate_log_normal
from scipy.stats import lognorm, gamma
from numpy import exp, random

from math import exp

# Simulate p-value
def simulate_pvalue(Nsim, n, D_KS):
    pvalue = 0
    for _ in range(Nsim):
        uniforms = random.uniform(low=0,high=1,size=n)
        uniforms.sort()
        d_j = 0
        for j in range(n):
            u_j = uniforms[j]
            d_j = max(d_j, (j+1)/n - u_j  , u_j - j/n)

        if d_j >= D_KS:
            pvalue += 1
    return pvalue/Nsim

def estimator_KS(Y, F):
    if (len(Y) != len(set(Y))):
        print("El test de KS requiere que todos los\
               datos de la muestra sean distintos.")
        return None

    # Calculate the Kolmogorov Smirnov estimator D_gamma
    n = len(Y)
    D = max([max(j/n - F[j-1], F[j-1] - (j-1)/n) for j in range(1,n+1)])

    return D

sample = parse_sample('../sample23.dat')
Y = sorted(sample)
n = len(Y)

# Calculate F_gamma(Yi)
alfa, beta = estimate_gamma(Y)
F_gamma = gamma.cdf(Y, alfa, loc=0, scale=beta)
D_gamma = estimator_KS(Y, F_gamma)

mu, sigma = estimate_log_normal(Y)
F_lognormal = lognorm.cdf(Y, s=sigma, loc=0, scale=exp(mu))
D_lognomal = estimator_KS(Y, F_lognormal)

print("Estádisticos D:")
print("- Gamma     =", D_gamma)
print("- Lognormal =", D_lognomal)

Nsim = 10000
pvalue_Gamma = simulate_pvalue(Nsim, n, D_gamma)
pvalue_Lognormal = simulate_pvalue(Nsim, n, D_lognomal)

print("p valor de la hipótesis de que los datos provienen de una distribución:")
print("- Gamma     =", pvalue_Gamma)
print("- Lognormal =", pvalue_Lognormal)