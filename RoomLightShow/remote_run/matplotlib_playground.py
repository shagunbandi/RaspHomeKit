# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2 ,3,4,5,6]
y = [1,2 ,3,4,5,6]

plt.clf()

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

plt.grid()

# function to show the plot
plt.show()
