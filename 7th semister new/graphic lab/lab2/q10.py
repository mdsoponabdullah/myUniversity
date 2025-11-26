import matplotlib.pyplot as plt

# Function to check if point is inside rectangle
def inside(x, y, xmin, ymin, xmax, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

# Mid-Point Subdivision line clipping
def midpoint_subdivision(x1, y1, x2, y2, xmin, ymin, xmax, ymax, tol=0.01):
    # If line completely inside
    if inside(x1, y1, xmin, ymin, xmax, ymax) and inside(x2, y2, xmin, ymin, xmax, ymax):
        return [(x1, y1, x2, y2)]
    
    # If line completely outside (trivial rejection)
    if (x1 < xmin and x2 < xmin) or (x1 > xmax and x2 > xmax) or (y1 < ymin and y2 < ymin) or (y1 > ymax and y2 > ymax):
        return []

    # If line segment is very small
    if abs(x2 - x1) < tol and abs(y2 - y1) < tol:
        return []

    # Subdivide at midpoint
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    # Recursively clip both halves
    first_half = midpoint_subdivision(x1, y1, mx, my, xmin, ymin, xmax, ymax, tol)
    second_half = midpoint_subdivision(mx, my, x2, y2, xmin, ymin, xmax, ymax, tol)

    return first_half + second_half

# ===============================
# Example Usage
# ===============================
xmin, ymin, xmax, ymax = 2, 2, 8, 6  # Clipping window
lines = [(1,1, 9,7), (3,3, 7,5), (0,4, 10,4)]

# Plot original lines
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title("Before Clipping")
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'r-')  # clipping window
for x1, y1, x2, y2 in lines:
    plt.plot([x1,x2], [y1,y2], 'bo-')
plt.axis('equal')
plt.grid(True)

# Plot after midpoint subdivision clipping
plt.subplot(1,2,2)
plt.title("After Mid-Point Subdivision Clipping")
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], 'r-')  # clipping window
for x1, y1, x2, y2 in lines:
    segments = midpoint_subdivision(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    for sx1, sy1, sx2, sy2 in segments:
        plt.plot([sx1, sx2], [sy1, sy2], 'go-', linewidth=2)
plt.axis('equal')
plt.grid(True)

plt.show()
