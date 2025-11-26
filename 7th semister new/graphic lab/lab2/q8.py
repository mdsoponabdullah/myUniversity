import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.patches as patches

# Defining maximum number of points in polygon
MAX_POINTS = 20

# Function to return x-value of point of intersection of two lines
def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

# Function to return y-value of point of intersection of two lines
def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

# Function to clip all the edges w.r.t one clip edge of clipping area
def clip(poly_points, poly_size, x1, y1, x2, y2):
    new_points = np.zeros((MAX_POINTS, 2), dtype=float)
    new_poly_size = 0

    for i in range(poly_size):
        k = (i+1) % poly_size
        ix, iy = poly_points[i]
        kx, ky = poly_points[k]

        i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
        k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)

        if i_pos < 0 and k_pos < 0:
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1
        elif i_pos >= 0 and k_pos < 0:
            new_points[new_poly_size] = [x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),
                                         y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)]
            new_poly_size += 1
            new_points[new_poly_size] = [kx, ky]
            new_poly_size += 1
        elif i_pos < 0 and k_pos >= 0:
            new_points[new_poly_size] = [x_intersect(x1, y1, x2, y2, ix, iy, kx, ky),
                                         y_intersect(x1, y1, x2, y2, ix, iy, kx, ky)]
            new_poly_size += 1
        else:
            pass

    clipped_poly_points = np.zeros((new_poly_size, 2), dtype=float)
    for i in range(new_poly_size):
        clipped_poly_points[i] = new_points[i]

    return clipped_poly_points, new_poly_size

def plot_step(step_num, title, poly_points, poly_size, clipper_points, clipper_size, 
              current_edge=None, show_intersections=False):
    """Plot a single step of the clipping process"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot original polygon (faint)
    if step_num == 0:
        poly_patch = Polygon(poly_points[:poly_size], alpha=0.2, color='blue', 
                           label='Original Polygon', linestyle='--')
    else:
        poly_patch = Polygon(poly_points[:poly_size], alpha=0.1, color='blue', 
                           linestyle='--')
    ax.add_patch(poly_patch)
    
    # Plot clipper polygon
    clipper_patch = Polygon(clipper_points[:clipper_size], alpha=0.3, color='red', 
                           label='Clipping Window', fill=False, linewidth=2)
    ax.add_patch(clipper_patch)
    
    # Highlight current clipping edge
    if current_edge is not None:
        i, k = current_edge
        edge_x = [clipper_points[i][0], clipper_points[k][0]]
        edge_y = [clipper_points[i][1], clipper_points[k][1]]
        ax.plot(edge_x, edge_y, 'g-', linewidth=4, alpha=0.7, 
                label='Current Clipping Edge')
        
        # Add arrow to show edge direction
        ax.arrow(clipper_points[i][0], clipper_points[i][1],
                (clipper_points[k][0] - clipper_points[i][0]) * 0.8,
                (clipper_points[k][1] - clipper_points[i][1]) * 0.8,
                head_width=5, head_length=5, fc='green', ec='green')
    
    # Plot current polygon state
    if poly_size > 0:
        current_patch = Polygon(poly_points[:poly_size], alpha=0.6, color='purple', 
                              linewidth=3, label='Current Polygon', fill=False)
        ax.add_patch(current_patch)
        
        # Plot vertices
        ax.plot(poly_points[:poly_size, 0], poly_points[:poly_size, 1], 'bo', 
               markersize=8, label='Vertices')
    
    # Set plot properties
    ax.set_xlim(50, 350)
    ax.set_ylim(50, 350)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(title)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Add vertex information
    info_text = f'Vertices: {poly_size}'
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

# Function to implement Sutherland–Hodgman algorithm with step-by-step visualization
def suthHodgClip_step_by_step(poly_points, poly_size, clipper_points, clipper_size):
    # Step 0: Show initial state
    print("Step 0: Initial State")
    plot_step(0, "Step 0: Initial State - Original Polygon and Clipping Window", 
              poly_points, poly_size, clipper_points, clipper_size)
    
    current_poly = poly_points.copy()
    current_size = poly_size
    
    # Perform clipping step by step
    for i in range(clipper_size):
        k = (i+1) % clipper_size
        
        print(f"\nStep {i+1}: Clipping against Edge {i+1}")
        print(f"Edge from ({clipper_points[i][0]}, {clipper_points[i][1]}) to ({clipper_points[k][0]}, {clipper_points[k][1]})")
        
        # Show state before clipping with this edge
        plot_step(i+1, f"Step {i+1}: Before Clipping with Edge {i+1}\n(From ({clipper_points[i][0]}, {clipper_points[i][1]}) to ({clipper_points[k][0]}, {clipper_points[k][1]}))", 
                  current_poly, current_size, clipper_points, clipper_size, 
                  current_edge=(i, k))
        
        # Perform clipping with this edge
        current_poly, current_size = clip(current_poly, current_size, 
                                         clipper_points[i][0], clipper_points[i][1],
                                         clipper_points[k][0], clipper_points[k][1])
        
        # Show state after clipping with this edge
        plot_step(i+1.5, f"Step {i+1}: After Clipping with Edge {i+1}\nResult: {current_size} vertices", 
                  current_poly, current_size, clipper_points, clipper_size)
    
    # Final result
    print(f"\nFinal Step: Clipped Polygon with {current_size} vertices")
    plot_step(clipper_size + 1, "Final Result: Clipped Polygon", 
              current_poly, current_size, clipper_points, clipper_size)
    
    # Print vertices of clipped polygon
    print("\nVertices of clipped polygon:")
    for i in range(current_size):
        print(f'({current_poly[i][0]:.2f}, {current_poly[i][1]:.2f})')
    
    return current_poly, current_size

# Driver code
if __name__ == "__main__":
    # Example with triangle polygon and square clipper
    print("Sutherland-Hodgman Polygon Clipping Algorithm")
    print("=" * 50)
    
    # Defining polygon vertices in clockwise order
    poly_size = 3
    poly_points = np.array([[100, 150], [200, 250], [300, 200]], dtype=float)
    
    # Defining clipper polygon vertices in clockwise order
    clipper_size = 4
    clipper_points = np.array([[150, 150], [150, 200], [200, 200], [200, 150]], dtype=float)
    
    print("Original Polygon vertices:")
    for i in range(poly_size):
        print(f'({poly_points[i][0]}, {poly_points[i][1]})')
    
    print("\nClipping Window vertices:")
    for i in range(clipper_size):
        print(f'({clipper_points[i][0]}, {clipper_points[i][1]})')
    
    # Run the algorithm with step-by-step visualization
    clipped_poly, clipped_size = suthHodgClip_step_by_step(poly_points, poly_size, 
                                                          clipper_points, clipper_size)