import matplotlib.pyplot as plt

def midpoint_circle_book(xc, yc, r):
    x = 0
    y = r
    p = 1 - r  # initial decision parameter
    points = []

    def plot_circle_points(xc, yc, x, y):
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:  # midpoint inside the circle
            p = p + 2 * x + 3
        else:      # midpoint outside or on the circle
            y -= 1
            p = p + 2 * (x - y) + 5
        plot_circle_points(xc, yc, x, y)

    return points


# Example: draw a circle
xc, yc, r = 50, 50, 30
pts = midpoint_circle_book(xc, yc, r)

x_vals = [p[0] for p in pts]
y_vals = [p[1] for p in pts]

plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, marker='s', s=10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Midpoint Circle Algorithm (Book Version)\ncenter=({xc},{yc}), radius={r}")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()
