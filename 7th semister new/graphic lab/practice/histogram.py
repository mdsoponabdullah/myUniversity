import matplotlib.pyplot as plt

makrks=[100,70,56,56,34,100,45,36,45,12,23,45,88,88,70,70,34]



plt.hist(makrks,label="Marks")



plt.xlabel("x axis")
plt.ylabel("y axis")
# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
