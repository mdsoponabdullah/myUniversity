from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 1000, 1000

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)     # Red
    glVertex2f(0, 0)
    glVertex2f(0.5, -0.5)
    glVertex2f(0, 0.5)
    glEnd()

def draw_square():
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)     # Green
    glVertex2f(0.1,0.1)
    glVertex2f(0.4, 0.1)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.1, 0.4)
    glEnd()

def draw_circle():
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 0, 1)     # Blue
    glVertex2f(0, 0)       # Center
    for angle in range(0, 361, 5):
        x = 0.5 * math.cos(math.radians(angle))
        y = 0.5 * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw Triangle
    glPushMatrix()
    glTranslatef(-0.7, 0.5, 0)
    draw_triangle()
    glPopMatrix()

    # Draw Square
    glPushMatrix()
    glTranslatef(0.7, 0.5, 0)
    draw_square()
    glPopMatrix()

    # Draw Circle
    glPushMatrix()
    glTranslatef(0, -0.5, 0)
    draw_circle()
    glPopMatrix()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"OpenGL Shapes Example")
    glClearColor(1, 1, 1, 1)    # Background white
    gluOrtho2D(-1, 1, -1, 1)    # 2D coordinate system
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
