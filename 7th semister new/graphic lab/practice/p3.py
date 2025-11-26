import matplotlib.pyplot as plt

x=[2,14,15,22,29]
y=[10,10,5,5,10]
y2=[12,14,45,35,20]
y4=[16,17,15,25,13]


plt.plot(x,y,label="y")
plt.plot(x,y2,label="y4")
plt.plot(x,y4,label="y4")




plt.xlabel("x axis")
plt.ylabel("y axis")
# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
