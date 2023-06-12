import matplotlib.pyplot as plt
from parse_sample import parse_sample

def plot_points(data):
    x = data[:-1]
    y = data[1:]

    # Plot the graph
    plt.scatter(x, y, alpha=0.3, color='magenta')
    plt.xlabel('Xi')
    plt.ylabel('Xi+1')
    plt.title('Diagrama de dispersión')
    plt.savefig('../plots/scattle_diagram')
    plt.clf()

data = parse_sample('../sample23.dat')
plot_points(data)

