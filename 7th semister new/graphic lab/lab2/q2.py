import matplotlib.pyplot as plt
import numpy as np

# ---------- Function to Draw a Polygon ----------
def draw_shape(points, color='blue', label=''):
    x = points[:, 0]
    y = points[:, 1]
    plt.fill(x, y, color=color, alpha=0.5, label=label)

# ---------- Rotation Function ----------
def rotate(points, angle_deg, pivot):
    # Convert degree → radians
    theta = np.radians(angle_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    

    # Translate points so that pivot → origin
    tx, ty = pivot[0], pivot[1]
    translate_to_origin = np.array([
        [1, 0, -tx],
        [0, 1, -ty],
        [0, 0, 1]
    ])

    # Rotation matrix (3x3 homogeneous)
    rotation_matrix = np.array([
        [cos_t, -sin_t, 0],
        [sin_t,  cos_t, 0],
        [0,      0,     1]
    ])


    # Translate back to pivot position
    translate_back = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    # Combine all transforms: T_back * R * T_origin
    transform = translate_back.dot(rotation_matrix).dot(translate_to_origin)

    # Add homogeneous coordinate 1 for each point
    ones = np.ones((points.shape[0], 1))
    homogeneous = np.hstack((points, ones))

    # Apply transformation
    rotated = homogeneous.dot(transform.T)
    return rotated[:, :2]

# ---------- Define Chair (Seat + Back + Leg) ----------
seat = np.array([[1, 9], [4.5, 9], [4.5, 5], [1, 5]])       # seat
back = np.array([[1, 13], [2, 13], [2, 9], [1, 9]])   # backrest
leg = np.array([[1, 5], [1.5, 5], [1.5, 2], [1, 2]])   # front leg
leg2 = np.array([[4, 5], [4.5, 5], [4.5, 2], [4, 2]])   # front leg

# ---------- Draw Original Chair ----------
draw_shape(seat, 'skyblue', 'Original Seat')
draw_shape(back, 'orange', 'Original Back')
draw_shape(leg, 'green', 'Original Leg')
draw_shape(leg2, 'blue', 'front Leg')


# ---------- Rotation ----------
pivot = (1, 9)      # rotate around this point (e.g., bottom-left corner)
angle = 45           # rotation angle in degrees

seat_r = rotate(seat, angle, pivot)
back_r = rotate(back, angle, pivot)
leg_r = rotate(leg, angle, pivot)
leg_r2 = rotate(leg2, angle, pivot)

# ---------- Draw Rotated Chair ----------
draw_shape(seat_r, 'deepskyblue', 'Rotated Seat')
draw_shape(back_r, 'darkorange', 'Rotated Back')
draw_shape(leg_r, 'limegreen', 'Rotated Leg')
draw_shape(leg_r2, 'blue', 'Rotated Leg')

# ---------- Plot Settings ----------
plt.title(f"Rotation of Chair by {angle}° about point {pivot}")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
