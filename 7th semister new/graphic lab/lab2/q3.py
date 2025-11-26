import matplotlib.pyplot as plt
import numpy as np

# ---------- Function to draw a polygon ----------
def draw_shape(points, color='blue', label=''):
    x = points[:, 0]
    y = points[:, 1]
    plt.fill(x, y, color=color, alpha=0.5, label=label)

# ---------- Scaling Function ----------
def scale(points, sx, sy, ref_point=(0, 0)):
    # Translate object to origin (if scaling around a reference point)
    tx, ty = ref_point[0], ref_point[1]
    translate_to_origin = np.array([
        [1, 0, -tx],
        [0, 1, -ty],
        [0, 0, 1]
    ])

    # Scaling matrix
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    # Translate back
    translate_back = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    # Combine transformations
    transform = translate_back.dot(scaling_matrix).dot(translate_to_origin)

    # Apply to points (in homogeneous form)
    ones = np.ones((points.shape[0], 1))
    homogeneous = np.hstack((points, ones))
    
    scaled = homogeneous.dot(transform.T)

    return scaled[:, :2]

# ---------- Define a triangle ----------
triangle = np.array([
    [1, 1],
    [4, 1],
    [2.5, 3]
])

# ---------- Draw Original Triangle ----------
draw_shape(triangle, 'skyblue', 'Original Triangle')

# ---------- Scaling Parameters ----------
sx, sy = 2, 3          # scale 2× in X and Y
ref_point = (0, 0)     # scale about origin

# ---------- Apply Scaling ----------
triangle_scaled = scale(triangle, sx, sy, ref_point)

# ---------- Draw Scaled Triangle ----------
draw_shape(triangle_scaled, 'orange', 'Scaled Triangle')

# ---------- Plot Settings ----------
plt.title(f"Scaling a Triangle by (Sx={sx}, Sy={sy}) about point {ref_point}")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
