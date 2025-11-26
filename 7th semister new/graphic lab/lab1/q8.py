import matplotlib.pyplot as plt
import numpy as np
import sys

# Increase recursion limit for large fill operations
sys.setrecursionlimit(100000)

def boundary_fill(canvas, x, y, fill_color, boundary_color):
    """
    Boundary Fill Algorithm - 8-connected version
    
    Parameters:
    - canvas: numpy array representing the image
    - x, y: seed point coordinates
    - fill_color: tuple (R, G, B) or single value for the fill color
    - boundary_color: tuple (R, G, B) or single value for boundary color
    """
    # Check if coordinates are within bounds
    height, width = canvas.shape[:2]
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    
    # Get current pixel color
    current_color = tuple(canvas[y, x])
    
    # Check if current pixel is not fill color and not boundary color
    if current_color != fill_color and current_color != boundary_color:
        # Fill the current pixel
        canvas[y, x] = fill_color
        
        # Recursively fill 8-connected neighbors
        boundary_fill(canvas, x+1, y, fill_color, boundary_color)    # Right
        boundary_fill(canvas, x-1, y, fill_color, boundary_color)    # Left
        boundary_fill(canvas, x, y-1, fill_color, boundary_color)    # Up
        boundary_fill(canvas, x, y+1, fill_color, boundary_color)    # Down
        boundary_fill(canvas, x+1, y-1, fill_color, boundary_color)  # Right-Up
        boundary_fill(canvas, x+1, y+1, fill_color, boundary_color)  # Right-Down
        boundary_fill(canvas, x-1, y-1, fill_color, boundary_color)  # Left-Up
        boundary_fill(canvas, x-1, y+1, fill_color, boundary_color)  # Left-Down


def main():
    # Get user input
    print("Boundary Fill Algorithm - Python Implementation")
    print("=" * 50)
    
    # Get seed point
    print("\nEnter the seed point (x y):")
    try:
        x, y = map(int, input().split())
    except:
        print("Invalid input. Using default seed point (250, 200)")
        x, y = 250, 200
    
    # Create a canvas (white background)
    width, height = 500, 400
    canvas = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    # Define colors
    boundary_color = (0, 0, 0)      # Black boundary
    fill_color = (100, 150, 255)    # Blue fill
    
    # Draw a rectangle boundary (similar to C code)
    # rectangle(100, 100, 400, 300) in C
    # Drawing boundary in black
    canvas[100:301, 100] = boundary_color    # Left edge
    canvas[100:301, 400] = boundary_color    # Right edge
    canvas[100, 100:401] = boundary_color    # Top edge
    canvas[300, 100:401] = boundary_color    # Bottom edge
    
    # Optional: Draw additional shapes for more complex boundaries
    # You can add circles, lines, or other shapes here
    
    print(f"\nConfiguration:")
    print(f"Canvas size: {width}x{height}")
    print(f"Seed point: ({x}, {y})")
    print(f"Boundary color: RGB{boundary_color}")
    print(f"Fill color: RGB{fill_color}")
    print(f"\nStarting boundary fill...")
    
    # Perform boundary fill
    try:
        boundary_fill(canvas, x, y, fill_color, boundary_color)
        print("Boundary fill completed successfully!")
    except RecursionError:
        print("Warning: Recursion limit reached. Try a smaller region or iterative approach.")
    
    # Display the result
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Before filling (recreate original)
    canvas_before = np.ones((height, width, 3), dtype=np.uint8) * 255
    canvas_before[100:301, 100] = boundary_color
    canvas_before[100:301, 400] = boundary_color
    canvas_before[100, 100:401] = boundary_color
    canvas_before[300, 100:401] = boundary_color
    
    ax1.imshow(canvas_before)
    ax1.set_title('Before Boundary Fill', fontsize=14, fontweight='bold')
    ax1.plot(x, y, 'ro', markersize=10, label=f'Seed Point ({x}, {y})')
    ax1.legend()
    ax1.axis('off')
    
    # After filling
    ax2.imshow(canvas)
    ax2.set_title('After Boundary Fill', fontsize=14, fontweight='bold')
    ax2.axis('off')
    
    plt.suptitle('Boundary Fill Algorithm - Python Implementation', 
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()