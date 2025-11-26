import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to generate circle points
def circle_points(xc, yc, r, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    x = xc + r * np.cos(angles)
    y = yc + r * np.sin(angles)
    return x, y

# Canvas setup
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.set_title("Bouncing Circle Animation")

# Circle parameters
r = 10
xc, yc = 50, 50
vx, vy = 1.5, 1.0  # velocity (x, y)

# Draw initial circle
x, y = circle_points(xc, yc, r)
circle_plot, = ax.plot(x, y, 'b')

# Update function for animation
def update(frame):
    global xc, yc, vx, vy
    xc += vx
    yc += vy

    # Bounce from walls
    if xc + r > 100 or xc - r < 0:
        vx = -vx
    if yc + r > 100 or yc - r < 0:
        vy = -vy

    # Update circle coordinates
    x, y = circle_points(xc, yc, r)
    circle_plot.set_data(x, y)
    return circle_plot,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=30, blit=True)

plt.show()
