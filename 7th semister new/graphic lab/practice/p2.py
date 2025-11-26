import matplotlib.pyplot as plt

x=[2,10,10,2,2]
y=[10,10,5,5,10]
plt.scatter(x,y)


plt.xlabel("x axis")
plt.ylabel("y axis")
# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
