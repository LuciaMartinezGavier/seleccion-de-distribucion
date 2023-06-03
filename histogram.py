import matplotlib.pyplot as plt
data = 'sample23.dat'
with open(data, 'r') as file:
        lines = file.readlines()

values = []
for i in range(len(lines) - 1):
    values.append(float(lines[i]))

# Create the histogram
plt.hist(values)

# Set plot properties
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Plot')

# Show the plot
plt.show()