from parse_sample import parse_sample
import matplotlib.pyplot as plt
import numpy as np

def calculate_sample_estimates(data):
    n = len(data)
    
    # Maximum and minimum values
    maxi = max(data)
    mini = min(data)

    # Mean
    mean = sum(data) / n

    # Variance
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)

    # Skewness
    skewness = sum((x - mean) ** 3 for x in data) / (n * variance ** (3/2))

    return maxi, mini, mean, variance, skewness


def calculate_sample_quantiles(data):
    # Sort the data in ascending order
    sorted_data = sorted(data)
    
    # Calculate the quartiles
    q1 = np.percentile(sorted_data, 25)
    q2 = np.percentile(sorted_data, 50)
    q3 = np.percentile(sorted_data, 75)
    
    return q1, q2, q3

def create_box_plot(data):
    # Calculate the quartiles and sample estimates
    q1, q2, q3 = calculate_sample_quantiles(data)
    maxx, minn, mean, variance, skewness = calculate_sample_estimates(data)

    # Create the box plot
    plt.boxplot(data)
    plt.scatter(np.random.normal(1, 0.01, len(data)), data, alpha=0.05, color='magenta')
    
    # Set plot properties
    plt.ylabel('Valor')
    plt.title('Box Plot')
    plt.xticks([1], ['Muestra'])

    plt.text(1.1, q2-0.5, f'Mediana: {q2:.2f}', va='center', fontweight='bold')
    plt.text(1.1, mean + 0.5, f'Media: {mean:.2f}', va='center', fontweight='bold')
    plt.text(1.1, q1, f'Q1: {q1:.2f}', va='center', fontweight='bold')
    plt.text(1.1, q3, f'Q3: {q3:.2f}', va='center', fontweight='bold')
    plt.text(1.1, minn, f'Mín: {minn:.2f}', va='center', fontweight='bold')
    plt.text(1.1, maxx, f'Máx: {maxx:.2f}', va='center', fontweight='bold')
    plt.text(1.1, variance, f'Varianza: {variance:.2f}', va='center', fontweight='bold')
    plt.text(1.1, (q3 + variance)/2, f'Asimetría: {skewness:.2f}', va='center', fontweight='bold')
    
    # Show the plot
    plt.savefig('../plots/box_plot')

data = parse_sample('../sample23.dat')
maxx, minn, mean, variance, skewness = calculate_sample_estimates(data)
q1, q2, q3 = calculate_sample_quantiles(data)
create_box_plot(data)

print("Valor máximo:\t", maxx)
print("Valor mínimo:\t", minn)
print("Media:\t\t", mean)
print("Varianza:\t", variance)
print("Skewness:\t", skewness)
print("Mediana:\t", q2)
print("Cuantil 1:\t", q1)
print("Cuantil 3:\t", q3)
