import matplotlib.pyplot as plt
import numpy as np

def clip_line_with_circle(x1, y1, x2, y2, cx, cy, r):
    # Shift coordinates so that the circle is centered at the origin
    x1 -= cx
    y1 -= cy
    x2 -= cx
    y2 -= cy

    dx = x2 - x1
    dy = y2 - y1

    a = dx**2 + dy**2
    b = 2 * (x1 * dx + y1 * dy)
    c = x1**2 + y1**2 - r**2

    disc = b**2 - 4 * a * c
    if disc < 0:
        # No intersection
        return None

    sqrt_disc = np.sqrt(disc)
    t1 = (-b + sqrt_disc) / (2 * a)
    t2 = (-b - sqrt_disc) / (2 * a)

    # Intersection points (may or may not be within segment)
    points = []
    for t in [t1, t2]:
        if 0 <= t <= 1:  # Only inside the segment
            x = x1 + t * dx + cx
            y = y1 + t * dy + cy
            points.append((x, y))

    return points if points else None


# Circle parameters
circle_center_x, circle_center_y, radius = 5, 5, 3
lines = [
    (2, 2, 9, 9),   # diagonal
    (1, 5, 9, 5),   # horizontal
    (5, 1, 5, 9)    # vertical
]

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# -------- BEFORE CLIPPING --------
ax[0].set_title("Before Clipping")
ax[0].add_patch(plt.Circle((circle_center_x, circle_center_y), radius, color='r', fill=False))

for (x1, y1, x2, y2) in lines:
    ax[0].plot([x1, x2], [y1, y2], 'bo-', label='Original Line')

ax[0].set_xlim(0, 10)
ax[0].set_ylim(0, 10)
ax[0].set_aspect('equal')

# -------- AFTER CLIPPING --------
ax[1].set_title("After Clipping")
ax[1].add_patch(plt.Circle((circle_center_x, circle_center_y), radius, color='r', fill=False))

for (x1, y1, x2, y2) in lines:
    clipped = clip_line_with_circle(x1, y1, x2, y2, circle_center_x, circle_center_y, radius)
    print(f"Clipped points for line ({x1},{y1})-({x2},{y2}):", clipped)
    if clipped and len(clipped) == 2:
        (x11, y11), (x12, y12) = clipped
        ax[1].plot([x11, x12], [y11, y12], 'go-', linewidth=2)
    else:
        # If fully inside or no intersection, draw accordingly
        ax[1].plot([x1, x2], [y1, y2], 'bo--', alpha=0.3)

ax[1].set_xlim(0, 10)
ax[1].set_ylim(0, 10)
ax[1].set_aspect('equal')

plt.show()
