from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

# ========== Object ============
sudut = -2.0
kotakRotasi = [
        [-50, -50, 0.0],
        [-50, 50, 0.0],
        [50, 50, 0.0],
        [50, -50, 0.0],
    ]

kotakScale = [
       [-15.0, 15.0, 0.0],
       [15.0, 15.0, 0.0],
       [15.0, -15.0, 0.0],
       [-15.0, -15.0, 0.0]
    ]

kotakVertikal = [
    [-200.0, -200.0, 0.0],
    [-200.0, -150.0, 0.0],
    [-150.0, -150.0, 0.0],
    [-150.0, -200.0, 0.0]
]

kotakHorizontal = [
    [-200.0, 140.0, 0.0],
    [-200.0, 100.0, 0.0],
    [-160.0, 100.0, 0.0],
    [-160.0, 140.0, 0.0]
]

# ========== Draw Single 2D Object ============
def draw_line(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINES)
    for i in range(n):
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

def draw_polyline(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINE_LOOP)    
    for i in range(n):        
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

def draw_fillpolygon(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_POLYGON)
    for i in range(n):
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

# ========== Object Transformation =============
def operatorBintangVector3D_t(a, b):
    c = [0.0, 0.0, 0.0]   
    for i in range(3):        
        for j in range(3):
            c[i] += a[i][j] * b[j]                 
    return c

def operatorTambahVector3D_t(a, b):
    c = [0.0, 0.0, 0.0]   
    for i in range(3):        
         c[i] = a[i] + b[i]           
    return c

# ========== Drawing Function ============
def sumbu_koordinat():
    sumbuX = [[-200.0, 0.0], [200.0, 0.0]]
    sumbuY = [[0.0, -200.0], [0.0, 200.0]]
    col = [0.0, 0.0, 1.0]

    draw_line(sumbuX, 2, col)
    draw_line(sumbuY, 2, col)

def segiempat_rotasi():    
    n = 4
    col = [1.0, 0.0, 0.0]    
    
    # Rotation matrix
    matrix3DZ = [
        [math.cos(sudut/57.3), -1 * math.sin(sudut/57.3), 0.0],
        [math.sin(sudut/57.3), math.cos(sudut/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]
    
    # Draw rectangle
    draw_polyline(kotakRotasi, n, col)

    # Rotate the rectangle
    for i in range(n):
        kotakRotasi[i] = operatorBintangVector3D_t(matrix3DZ, kotakRotasi[i])             

def segiempat_scale():
    n = 4
    col = [0.0, 0.0, 1.0]

    # Scale matrix
    matrixScale = [
        [1.01, 0.0, 0.0],
        [0.0, 1.01, 0.0],
        [0.0, 0.0, 1.0]
    ]

    # Draw rectangle
    draw_polyline(kotakScale, n, col)

    # Scale the rectangle
    for i in range(n):
        kotakScale[i] = operatorBintangVector3D_t(matrixScale, kotakScale[i])

    if (kotakScale[0][1] > 200.0):
        kotakScale[0] = [-15.0, 15.0, 0.0]
        kotakScale[1] = [15.0, 15.0, 0.0]
        kotakScale[2] = [15.0, -15.0, 0.0]
        kotakScale[3] = [-15.0, -15.0, 0.0]

def segiempat_vertikal():
    n = 4
    col = [0.0, 1.0, 0.0]

    # Vertikal Translation matrix
    matrixVertikalTranslation = [0.0, 2.0, 0.0]

    # Draw rectangle
    draw_fillpolygon(kotakVertikal, n, col)

    # Move the rectangle
    for i in range(n):
        kotakVertikal[i] = operatorTambahVector3D_t(matrixVertikalTranslation, kotakVertikal[i])

    # Spawn kotakVertikal on the starting point
    if (kotakVertikal[0][1] > 200.0):
        kotakVertikal[0] = [ -200.0, -200.0, 0.0 ]
        kotakVertikal[1] = [ -200.0, -150.0, 0.0 ]
        kotakVertikal[2] = [ -150.0, -150.0, 0.0 ]
        kotakVertikal[3] = [ -150.0, -200.0, 0.0 ]

def segiempat_horizontal():
    n = 4
    col = [0.0, 1.0, 0.0]

    # Horizontal Translation matrix
    matrixHorizontalTranslation = [2.0, 0.0, 0.0]

    # Draw rectangle
    draw_polyline(kotakHorizontal, n, col)

    # Move the rectangle
    for i in range(n):
        kotakHorizontal[i] = operatorTambahVector3D_t(matrixHorizontalTranslation, kotakHorizontal[i])

    # Spawn kotakHorizontal to the starting point
    if (kotakHorizontal[0][0] > 200.0):
        kotakHorizontal[0] = [-200.0, 140.0, 0.0]
        kotakHorizontal[1] = [-200.0, 100.0, 0.0]
        kotakHorizontal[2] = [-160.0, 100.0, 0.0]
        kotakHorizontal[3] = [-160.0, 140.0, 0.0]

# ========== Call Drawing Function =============
def draw0():
    sumbu_koordinat()
    segiempat_rotasi()
    segiempat_scale()
    segiempat_vertikal()
    segiempat_horizontal()      

def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1.0,1.0,1.0,0.0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0) # Set window ortho
    draw0() # Call Drawing Function
    glutSwapBuffers()

# ========== Timer Function ============
def timer(fps):
    glutTimerFunc(1000//fps, timer, fps)
    glutPostRedisplay()

# ========== Main Fuction ============
glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of the window
glutInitWindowPosition(100, 100)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046") # Set a window title
glutDisplayFunc(showScreen)
glutTimerFunc(1000//60, timer, 60)
glutMainLoop()  # Keeps the above created window displaying/running in a loop