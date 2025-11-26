import matplotlib.pyplot as plt

price=[300,400,100,156,111,788]
item =['t-shirt','pant','underwire','water','panjabi','others']


plt.pie(price,labels=item)



# Plot settings
plt.title("prctice")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
