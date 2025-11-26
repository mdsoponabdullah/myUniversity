import matplotlib.pyplot as plt

product=[1,2,3,4,5]
price =[10,15,8,18,10]
profit =[5,3,6,8,9]

plt.bar(product,price,label="product vs price")
plt.bar(product,profit,label="profit")



plt.xlabel("x axis")
plt.ylabel("y axis")
# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
