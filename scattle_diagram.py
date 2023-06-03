import matplotlib.pyplot as plt

def plot_points(data):
    x_values = []
    y_values = []

    # Read data from .dat file
    with open(data, 'r') as file:
        lines = file.readlines()
    [5.66, 11.55, ...]
    # Extract X_i values
    for i in range(len(lines) - 1):
        x_values.append(float(lines[i]))
        y_values.append(float(lines[i+1]))

    
    # Plot the graph
    plt.scatter(x_values, y_values)
    plt.plot(x_values, y_values, "*")
    plt.xlabel('X_i')
    plt.ylabel('X_i+1')
    plt.title('Plot of X_i and X_i+1')
    plt.show()

# Replace 'data.dat' with the actual path to your .dat file
plot_points('sample23.dat')
