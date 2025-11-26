import matplotlib.pyplot as plt
import numpy as np

# Function to draw a polygon
def draw_shape(points, color='blue', label=''):
    x = points[:, 0]
    y = points[:, 1]
    plt.fill(x, y, color=color, alpha=1, label=label)

# Translation function
def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    ones = np.ones((points.shape[0], 1))
    homogeneous = np.hstack((points, ones))
    translated = homogeneous.dot(translation_matrix.T)
    return translated[:, :2]

# Define the chair shape (seat, backrest, legs)
seat = np.array([[1, 9], [4.5, 9], [4.5, 5], [1, 5]])   # seat
back = np.array([[1, 13], [2, 13], [2, 9], [1, 9]])     # backrest
legs = np.array([[1, 5], [1.5, 5], [1.5, 2], [1, 2]])   # leg
legs2 = np.array([[4, 5], [4.5, 5], [4.5, 2], [4, 2]])  # leg

# Draw original chair (at default position)
draw_shape(seat, 'skyblue', 'Original Seat')
draw_shape(back, 'orange', 'Original Back')
draw_shape(legs, 'green', 'Original Leg')
draw_shape(legs2, 'green', 'Original Leg')

# Ask user for quadrant number
quad = int(input("Enter the quadrant number (1, 2, 3, or 4): "))

# Translation logic based on quadrant
if quad == 1:
    tx, ty = 5, 5        # +x, +y
elif quad == 2:
    tx, ty = -10, 5       # -x, +y
elif quad == 3:
    tx, ty = -10, -10     # -x, -y
elif quad == 4:
    tx, ty = 5, -10       # +x, -y
else:
    print("Invalid quadrant! Showing default position.")
    tx, ty = 0, 0

# Translate all parts of the chair
seat_t = translate(seat, tx, ty)
back_t = translate(back, tx, ty)
legs_t = translate(legs, tx, ty)
legs_t2 = translate(legs2, tx, ty)

# Draw translated chair
draw_shape(seat_t, 'deepskyblue', 'Translated Seat')
draw_shape(back_t, 'darkorange', 'Translated Back')
draw_shape(legs_t, 'limegreen', 'Translated Leg')
draw_shape(legs_t2, 'limegreen', 'Translated Leg')

# Set up axes for all 4 quadrants
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.grid(True)
plt.title("Chair Translation in Different Quadrants")
plt.legend()
plt.axis('equal')
plt.show()
