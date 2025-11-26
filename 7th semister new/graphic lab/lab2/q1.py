import matplotlib.pyplot as plt
import numpy as np

# Function to draw a polygon
def draw_shape(points, color='blue', label=''):
    x = points[:, 0]
    y = points[:, 1]
    plt.fill(x, y, color=color, alpha=1, label=label)

# Translation matrix function
def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    
# Creates a column of ones (for homogeneous coordinates).
# If there are 4 points, it makes a 4×1 matrix of ones like:
# [[1],
#  [1],
#  [1],
#  [1]]
    ones = np.ones((points.shape[0], 1))

# Combines (horizontally stacks) the original 2D points with this extra column of ones →
# converts them into homogeneous coordinates (x, y, 1).
# Example:
# Original → [[1, 2], [3, 4]]
# Becomes → [[1, 2, 1], [3, 4, 1]]
    homogeneous = np.hstack((points, ones))
    translated = homogeneous.dot(translation_matrix.T)
    return translated[:, :2]  

# Define the chair shape (a simple seat + backrest)
seat = np.array([[1, 9], [4.5, 9], [4.5, 5], [1, 5]])       # seat
back = np.array([[1, 13], [2, 13], [2, 9], [1, 9]])   # backrest
legs = np.array([[1, 5], [1.5, 5], [1.5, 2], [1, 2]])   # front leg
legs2 = np.array([[4, 5], [4.5, 5], [4.5, 2], [4, 2]])   # front leg


# Combine shapes for visualization
draw_shape(seat, 'skyblue', 'Original Seat ')
draw_shape(back, 'orange', 'Original Back')
draw_shape(legs, 'green', 'Original Leg')
draw_shape(legs2, 'green', 'Original Leg')


# Translation values (move chair)
tx, ty = 5, 3
seat_t = translate(seat, tx, ty)
back_t = translate(back, tx, ty)
legs_t = translate(legs, tx, ty)
legs_t2 = translate(legs2, tx, ty)



# Draw translated shapes
draw_shape(seat_t, 'deepskyblue', 'Translated Seat')
draw_shape(back_t, 'darkorange', 'Translated Back')
draw_shape(legs_t, 'limegreen', 'Translated Leg')
draw_shape(legs_t2, 'limegreen', 'Translated Leg')


# Plot settings
plt.title("2D Translation of a Chair")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
