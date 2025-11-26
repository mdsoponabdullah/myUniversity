import matplotlib.pyplot as plt

# ---------- Function to check position of point ----------
def point_position(A, B, P):
    # A, B, P are tuples (x, y)
    x1, y1 = A
    x2, y2 = B
    x, y = P

    # Compute cross product value
    val = (x2 - x1)*(y - y1) - (y2 - y1)*(x - x1)

    if val > 0:
        return "Left of the line"
    elif val < 0:
        return "Right of the line"
    else:
        return "On the line"

# ---------- Define line and point ----------
A = (1, 1)
B = (5, 4)

P = (5, 2)   # Test point

# ---------- Check position ----------
result = point_position(A, B, P)
print(f"Point {P} is {result} AB")

# ---------- Visualization ----------
x_line = [A[0], B[0]]
y_line = [A[1], B[1]]

plt.plot(x_line, y_line, 'red', label='Line AB')
plt.scatter(*A, color='blue', label='A')
plt.scatter(*B, color='blue', label='B')
plt.scatter(*P, color='red', label=f'P {result}')

plt.title(f"Point Test: {result}")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
