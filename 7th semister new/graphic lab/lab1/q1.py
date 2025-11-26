import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Set up the figure with 2x2 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Matplotlib Shapes and Animation', fontsize=16)

# 1. Chair
def draw_chair(ax):
    # Chair seat
    ax.plot([1,1,5,5,1], [5,10,10,5,5], 'b-', linewidth=2)
    
    # Chair back
    ax.plot([1, 1], [10, 15], 'b-', linewidth=2)
   
    
    # Chair legs
    ax.plot([1, 1], [1, 5], 'b-', linewidth=1.5)
    ax.plot([5, 5], [1, 5], 'b-', linewidth=1.5)
   
    
    ax.set_title('Chair')
    ax.set_aspect('equal')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 20)

# 2. Table
def draw_table(ax):
    # Table top
    ax.plot([1, 5, 5, 1, 1], [1, 1, 3, 3, 1], 'brown', linewidth=3)
    
    # Table legs
    ax.plot([1.5, 1.5], [1, 0.2], 'brown', linewidth=2)
    ax.plot([4.5, 4.5], [1, 0.2], 'brown', linewidth=2)
    ax.plot([1.5, 1.3], [0.2, 0], 'brown', linewidth=2)
    ax.plot([4.5, 4.7], [0.2, 0], 'brown', linewidth=2)
    
    ax.set_title('Table')
    ax.set_aspect('equal')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4)

# 3. House
def draw_house(ax):
    # House base
    ax.plot([1, 5, 5, 1, 1], [1, 1, 4, 4, 1], 'red', linewidth=2)
    
    # Roof
    ax.plot([1, 3, 5], [4, 6, 4], 'darkred', linewidth=2)
    
    # Door
    ax.plot([2.5, 3.5, 3.5, 2.5, 2.5], [1, 1, 2.5, 2.5, 1], 'brown', linewidth=2)
    
    # Window
    ax.plot([4, 4.8, 4.8, 4, 4], [2, 2, 2.8, 2.8, 2], 'blue', linewidth=2)
    # Window cross
    ax.plot([4.4, 4.4], [2, 2.8], 'blue', linewidth=1)
    ax.plot([4, 4.8], [2.4, 2.4], 'blue', linewidth=1)
    
    ax.set_title('House')
    ax.set_aspect('equal')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 7)

# 4. Animation - Bouncing Ball
def init_animation():
    ball_line.set_data([], [])
    return ball_line,

def animate(frame):
    x = 2 + 1.5 * np.sin(frame * 0.2)
    y = 2 + 1.5 * np.abs(np.cos(frame * 0.3))
    ball_line.set_data([x], [y])
    return ball_line,

# Set up animation subplot
ax4.set_xlim(0, 5)
ax4.set_ylim(0, 5)
ax4.set_title('Bouncing Ball Animation')
ax4.set_aspect('equal')
ax4.grid(True, alpha=0.3)

# Create ball for animation
ball_line, = ax4.plot([], [], 'ro', markersize=15)

# Draw all static shapes
draw_chair(ax1)
draw_table(ax2)
draw_house(ax3)

# Create the animation
anim = animation.FuncAnimation(
    fig, animate, init_func=init_animation,
    frames=100, interval=50, blit=True, repeat=True
)

plt.tight_layout()
plt.show()