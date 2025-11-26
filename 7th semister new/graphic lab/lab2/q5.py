import matplotlib.pyplot as plt

# Define the clipping window (rectangle)
xmin, ymin = 2, 2
xmax, ymax = 8, 6

# Define a list of test points
points = [(1, 1), (3, 3), (5, 2), (9, 5), (4, 7), (6, 4)]

# Function to check if a point is inside the clipping window
def is_inside(x, y):
    return xmin <= x <= xmax and ymin <= y <= ymax

# Separate points into inside and outside lists
inside_points = []
outside_points = []

for (x, y) in points:
    if is_inside(x, y):
        inside_points.append((x, y))
    else:
        outside_points.append((x, y))

# Print results
print("Inside Points:", inside_points)
print("Outside Points:", outside_points)

# ---------------- Plot ----------------
# Draw clipping window
rect_x = [xmin, xmax, xmax, xmin, xmin]
rect_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(rect_x, rect_y, 'b-', label='Clipping Window')

# Plot inside points (green)
for (x, y) in inside_points:
    plt.scatter(x, y, color='green', label='Inside')

# Plot outside points (red)
for (x, y) in outside_points:
    plt.scatter(x, y, color='red', label='Outside' )

plt.title("Point Clipping in a Rectangular Window")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
