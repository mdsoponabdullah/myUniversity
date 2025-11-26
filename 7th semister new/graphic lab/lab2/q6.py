import matplotlib.pyplot as plt

# ---- COHEN–SUTHERLAND LINE CLIPPING ALGORITHM ---- #

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """
    Clips a line (x1,y1)-(x2,y2) to the rectangular window (xmin,ymin)-(xmax,ymax)
    using the Cohen–Sutherland algorithm.
    """

    # Bit codes for each region
    INSIDE = 0   # 0000
    LEFT   = 1   # 0001
    RIGHT  = 2   # 0010
    BOTTOM = 4   # 0100
    TOP    = 8   # 1000

    # -----------------------------
    # Function to compute region code
    # -----------------------------
    def compute_code(x, y):
        code = INSIDE
        if x < xmin: code |= LEFT
        if x > xmax: code |= RIGHT
        if y < ymin: code |= BOTTOM
        if y > ymax: code |= TOP
        return code

    # Compute region codes for both points
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    accept = False  # initially assume line is not accepted

    while True:
        # Case 1: both endpoints are inside
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Case 2: both endpoints share an outside zone → reject
        elif (code1 & code2) != 0:
            break

        # Case 3: line needs clipping
        else:
            # Pick one point that is outside
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            if code_out & TOP:
                # point above the clip window
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                # point below the clip window
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                # point to the right of clip window
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                # point to the left of clip window
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Replace the outside point with intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1) #0000
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    # Return result
    if accept:
        return (x1, y1, x2, y2)
    else:
        return None


# ---- TESTING AND VISUALIZATION ---- #

# Define clipping window
xmin, ymin, xmax, ymax = 2, 2, 8, 6

# Define some test lines
lines = [
    (1, 1, 9, 7),  # crosses window
    (3, 3, 7, 5),  # inside window
    (0, 4, 10, 4), # passes through window
    (0, 6, 2, 8),
]

plt.figure(figsize=(10, 4))

# ---- Before clipping ----
plt.subplot(1, 2, 1)
plt.title("Before Clipping")
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'g-')  # clipping window
for (x1, y1, x2, y2) in lines:
    plt.plot([x1, x2], [y1, y2], 'bo-')
plt.grid(True)
plt.axis("equal")

# ---- After clipping ----
plt.subplot(1, 2, 2)
plt.title("After Clipping")
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r-')
for (x1, y1, x2, y2) in lines:
    clipped = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    if clipped:
        plt.plot([clipped[0], clipped[2]], [clipped[1], clipped[3]], 'go-', linewidth=2)
plt.grid(True)
plt.axis("equal")

plt.show()
