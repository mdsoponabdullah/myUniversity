import matplotlib.pyplot as plt

# ---------------- DIRECT EQUATION METHOD ----------------
def direct_line(x1, y1, x2, y2):
    x = []
    y = []
    m = (y2 - y1) / (x2 - x1) if x2 != x1 else None
    
    if m is None:  # Vertical Line
        for yi in range(y1, y2 + 1):
            x.append(x1)
            y.append(yi)
    else:
        c = y1 - m * x1
        for xi in range(x1, x2 + 1):
            yi = m * xi + c
            x.append(xi)
            y.append(round(yi))
    return x, y


# ----------------- DDA ALGORITHM -----------------------
def dda_line(x1, y1, x2, y2):
    x = []
    y = []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    Xinc = dx / steps
    Yinc = dy / steps

    X = x1
    Y = y1
    for i in range(steps + 1):
        x.append(round(X))
        y.append(round(Y))
        X += Xinc
        Y += Yinc
    return x, y


# ------- SIMPLIFIED BRESENHAM LINE ALGORITHM (0 ≤ m ≤ 1) -------
def bresenham_simple(x1, y1, x2, y2):
    x = []
    y = []

    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx   # initial decision parameter

    X = x1
    Y = y1

    while X <= x2:
        x.append(X)
        y.append(Y)

        if p < 0:
            p = p + 2 * dy   # Move East
        else:
            Y = Y + 1        # Move North-East
            p = p + 2 * (dy - dx)

        X = X + 1

    return x, y


# --------------------- MAIN ----------------------------
# Use coordinates that satisfy slope 0 ≤ m ≤ 1
x1, y1 = 2, 3
x2, y2 = 15, 9

dx, dy = direct_line(x1, y1, x2, y2)
xd, yd = dda_line(x1, y1, x2, y2)
xb, yb = bresenham_simple(x1, y1, x2, y2)

plt.figure(figsize=(12, 4))

# Subplot 1: Direct Method
plt.subplot(1, 3, 1)
plt.plot(dx, dy, marker='o')
plt.title("Direct Method")
plt.grid(True)

# Subplot 2: DDA Method
plt.subplot(1, 3, 2)
plt.plot(xd, yd, marker='o')
plt.title("DDA Algorithm")
plt.grid(True)

# Subplot 3: Simplified Bresenham Method
plt.subplot(1, 3, 3)
plt.plot(xb, yb, marker='o')
plt.title("Simplified Bresenham Algorithm")
plt.grid(True)

plt.tight_layout()
plt.show()
