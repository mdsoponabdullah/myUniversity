import matplotlib.pyplot as plt

def get_region_code(x, y, xmin, ymin, xmax, ymax):
    """Get 4-bit region code for a point"""
    code = 0
    if x < xmin: code |= 1    # Left
    if x > xmax: code |= 2    # Right  
    if y < ymin: code |= 4    # Bottom
    if y > ymax: code |= 8    # Top
    return code

# Simple visualization
xmin, ymin, xmax, ymax = 2, 2, 8, 6
x1, y1, x2, y2 = 1, 1, 9, 7

code1 = get_region_code(x1, y1, xmin, ymin, xmax, ymax)
code2 = get_region_code(x2, y2, xmin, ymin, xmax, ymax)

plt.figure(figsize=(8, 6))
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], 'r-', linewidth=2)
plt.plot([x1, x2], [y1, y2], 'bo-', linewidth=2)

# Annotate points
plt.text(x1, y1, f' P1\n ({x1},{y1})\n Code: {code1:04b}', 
         bbox=dict(boxstyle='round', facecolor='lightblue'))
plt.text(x2, y2, f' P2\n ({x2},{y2})\n Code: {code2:04b}', 
         bbox=dict(boxstyle='round', facecolor='lightgreen'))

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True)
plt.title('Cohen-Sutherland Region Codes')
plt.show()

print(f"Point 1 ({x1},{y1}): Region Code = {code1:04b}")
print(f"Point 2 ({x2},{y2}): Region Code = {code2:04b}")
print(f"Bitwise AND: {code1 & code2:04b}")
print("Line needs clipping" if code1 & code2 == 0 and (code1 != 0 or code2 != 0) else "Line accepted/rejected")