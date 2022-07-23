from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# ========== Single 2D Object ============
def draw_point(x, y):
    glColor3f(0.0,0.0,1.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# ========== Multiple 2D Object ============
def buat_titik():
    draw_point(100, 50)
    draw_point(100, 150)
    draw_point(100, 100)

def tv_rusak():
    glColor3f(random.random(), random.random(), random.random())
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(220):
        a = round(random.random(), 2) * 200
        b = round(random.random(), 2) * 200
        glVertex2f(a, b)
        glVertex2f(-a, b)
        glVertex2f(a, -b)
        glVertex2f(-a, -b)
    glEnd()

# ========== Drawing Function =============
def draw0():
    # # Draw points
    # glColor3f(1.0, 0.0, 0.0)
    # glPointSize(4)
    # glBegin(GL_POINTS)
    # glVertex3f(15.0, 15.0, 0.0)
    # glVertex3f(-15.0, 15.0, 0.0)
    # glVertex3f(-15.0, -15.0, 0.0)
    # glVertex3f(15.0, -15.0, 0.0)
    # glEnd()

    # # Draw line
    # glColor3f(0.0, 1.0, 0.0)
    # glBegin(GL_LINES)
    # glVertex3f(25.0, 25.0, 0.0)
    # glVertex3f(175.0, 175.0, 0.0)
    # glEnd()

    # draw_point(-150, 150)
    # buat_titik()
    tv_rusak()

def showScreen():
    glClearColor(1.0,1.0,1.0,0.0) # Window background color        
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-200.0, 200.0,-200.0,200.0) # Set window ortho
    draw0()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(400, 400)   # Set the w and h of your window
glutInitWindowPosition(200, 200)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046") # Set a window title
glutDisplayFunc(showScreen)
glutMainLoop()  # Keeps the above created window displaying/running in a loop