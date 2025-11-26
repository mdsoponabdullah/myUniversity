import matplotlib.pyplot as plt

x=[2,10,10,2,2]
y=[10,10,5,5,10]
plt.plot(x,y)

lx=[1,10]
ly=[2,20]
plt.plot(lx,ly,color="green",linewidth=2,linestyle="dotted")
plt.xlabel("x axis")
plt.ylabel("y axis")
# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
