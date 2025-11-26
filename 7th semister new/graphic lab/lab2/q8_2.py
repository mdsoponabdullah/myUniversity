import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Your provided code
MAX_POINTS = 20

def x_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

def y_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
    den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
    return num/den

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

def suthHodgClip(poly_points, poly_size, clipper_points, clipper_size):
    clipped_poly = poly_points.copy()
    clipped_size = poly_size
    
    for i in range(clipper_size):
        k = (i+1) % clipper_size
        clipped_poly, clipped_size = clip(clipped_poly, clipped_size, 
                                         clipper_points[i][0], clipper_points[i][1], 
                                         clipper_points[k][0], clipper_points[k][1])
    
    return clipped_poly, clipped_size

# Visualization function
def visualize_clipping(poly_points, clipper_points, clipped_poly):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Before Clipping
    ax1.set_title('Before Clipping', fontsize=14, fontweight='bold')
    
    # Draw the clipper window
    clipper_poly = Polygon(clipper_points, alpha=0.3, color='lightblue', label='Clipping Window')
    ax1.add_patch(clipper_poly)
    
    # Draw the original polygon
    original_poly = Polygon(poly_points, alpha=0.7, color='red', label='Original Polygon')
    ax1.add_patch(original_poly)
    
    # Set limits and labels
    ax1.set_xlim(0, 350)
    ax1.set_ylim(0, 350)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    
    # Plot 2: After Clipping
    ax2.set_title('After Clipping', fontsize=14, fontweight='bold')
    
    # Draw the clipper window
    clipper_poly2 = Polygon(clipper_points, alpha=0.3, color='lightblue', label='Clipping Window')
    ax2.add_patch(clipper_poly2)
    
    # Draw the clipped polygon
    if len(clipped_poly) > 2:
        clipped_poly_patch = Polygon(clipped_poly, alpha=0.7, color='green', label='Clipped Polygon')
        ax2.add_patch(clipped_poly_patch)
    
    # Set limits and labels
    ax2.set_xlim(0, 350)
    ax2.set_ylim(0, 350)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # Example 1: Triangle polygon with square clipper
    print("Example 1: Triangle with Square Clipper")
    poly_size = 3
    poly_points = np.array([[100, 150], [200, 250], [300, 200]], dtype=float)
    
    clipper_size = 4
    clipper_points = np.array([[150, 150], [150, 200], [200, 200], [200, 150]], dtype=float)
    
    # Perform clipping
    clipped_poly, clipped_size = suthHodgClip(poly_points, poly_size, clipper_points, clipper_size)
    
    # Print results
    print("Original polygon vertices:")
    for i in range(poly_size):
        print(f'({poly_points[i][0]}, {poly_points[i][1]})')
    
    print("\nClipped polygon vertices:")
    for i in range(clipped_size):
        print(f'({clipped_poly[i][0]:.2f}, {clipped_poly[i][1]:.2f})')
    
    # Visualize
    visualize_clipping(poly_points, clipper_points, clipped_poly)
    
    # Example 2: Different polygon
    print("\n" + "="*50)
    print("Example 2: Complex Polygon with Square Clipper")
    
    # Define a more complex polygon
    poly_size2 = 5
    poly_points2 = np.array([[50, 100], [150, 250], [250, 300], [300, 150], [200, 50]], dtype=float)
    
    # Use the same square clipper
    clipped_poly2, clipped_size2 = suthHodgClip(poly_points2, poly_size2, clipper_points, clipper_size)
    
    print("Original polygon vertices:")
    for i in range(poly_size2):
        print(f'({poly_points2[i][0]}, {poly_points2[i][1]})')
    
    print("\nClipped polygon vertices:")
    for i in range(clipped_size2):
        print(f'({clipped_poly2[i][0]:.2f}, {clipped_poly2[i][1]:.2f})')
    
    # Visualize second example
    visualize_clipping(poly_points2, clipper_points, clipped_poly2)