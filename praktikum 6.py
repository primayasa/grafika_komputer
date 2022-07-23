from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

# ========== Object ============
sudut = -2.0
bintangRotasi = [
    [0, 76, 0.0], [19, 20, 0.0], [77, 20, 0.0], [30, -15, 0.0], [48, -69, 0.0], [0, -36, 0.0],
    [-48, -69, 0.0], [-26, -15, 0.0], [-77, 20, 0.0], [-17, 20, 0.0]
]

segitigaRotasi = [
    [-50.0, 0.0, 0.0],
    [50.0, 0.0, 0.0],
    [0.0, 100.0, 0.0]
]

segitigaRotasi2 = [
    [[-20.0, 60.0, 0.0], [20.0, 60.0, 0.0], [0.0, 100.0, 0.0]],
    [[-20.0, -60.0, 0.0], [20.0, -60.0, 0.0], [0.0, -100.0, 0.0]],
    [[60.0, 20.0, 0.0], [60.0, -20.0, 0.0], [100.0, 0.0, 0.0]],
    [[-60.0, 20.0, 0.0], [-60.0, -20.0, 0.0], [-100.0, 0.0, 0.0]]
]

segitigaVertikal = [
    [[-180.0, -160.0, 0.0], [-140.0, -160.0, 0.0], [-160.0, -120.0, 0.0]],
    [[-120.0, -160.0, 0.0], [-80.0, -160.0, 0.0], [-100.0, -120.0, 0.0]],
    [[-60.0, -160.0, 0.0], [-20.0, -160.0, 0.0], [-40.0, -120.0, 0.0]],
    [[0.0, -160.0, 0.0], [40.0, -160.0, 0.0], [20.0, -120.0, 0.0]],
    [[60.0, -160.0, 0.0], [100.0, -160.0, 0.0], [80.0, -120.0, 0.0]],
    [[120.0, -160.0, 0.0], [160.0, -160.0, 0.0], [140.0, -120.0, 0.0]]
]

segitigaHorizontal = [
    [[-60.0, -90.0, 0.0], [-20.0, -90.0, 0.0], [-40.0, -50.0, 0.0]],
    [[-60.0, -40.0, 0.0], [-20.0, -40.0, 0.0], [-40.0, 0.0, 0.0]],
    [[-60.0, 10.0, 0.0], [-20.0, 10.0, 0.0], [-40.0, 50.0, 0.0]],
    [[-60.0, 60.0, 0.0], [-20.0, 60.0, 0.0], [-40.0, 100.0, 0.0]]
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

def bintang_rotasi():    
    n = 10
    col = [1.0, 0.0, 0.0]    
    
    # Rotation matrix
    matrix3DZ = [
        [math.cos(sudut/57.3), -1 * math.sin(sudut/57.3), 0.0],
        [math.sin(sudut/57.3), math.cos(sudut/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]
    
    # Draw star
    draw_polyline(bintangRotasi, n, col)

    # Rotate the star
    for i in range(n):
        bintangRotasi[i] = operatorBintangVector3D_t(matrix3DZ, bintangRotasi[i])

def bintang_scale():    
    n = 10
    col = [1.0, 0.0, 0.0]    
    
    # Scale matrix
    matrixScale = [
        [1.02, 0.0, 0.0],
        [0.0, 1.02, 0.0],
        [0.0, 0.0, 1.0]
    ]
    
    # Draw star
    draw_polyline(bintangRotasi, n, col)

    # Scale the star
    for i in range(n):
        bintangRotasi[i] = operatorBintangVector3D_t(matrixScale, bintangRotasi[i])

    # Make the star small again
    if (bintangRotasi[4][0] > 200.0):
        bintangRotasi[0] = [0, 76, 0.0]
        bintangRotasi[1] = [19, 20, 0.0]
        bintangRotasi[2] = [77, 20, 0.0]
        bintangRotasi[3] = [30, -15, 0.0]
        bintangRotasi[4] = [48, -69, 0.0]
        bintangRotasi[5] = [0, -36, 0.0]
        bintangRotasi[6] = [-48, -69, 0.0]
        bintangRotasi[7] = [-26, -15, 0.0]
        bintangRotasi[8] = [-77, 20, 0.0]
        bintangRotasi[9] = [-17, 20, 0.0]            

def segitiga_rotasi2():    
    n = 3
    col = [1.0, 0.0, 0.0]    
    
    for i in range(4):
        # Rotation matrix
        matrix3DZ = [
            [math.cos(sudut/57.3), -1 * math.sin(sudut/57.3), 0.0],
            [math.sin(sudut/57.3), math.cos(sudut/57.3), 0.0],
            [0.0, 0.0, 0.0]
        ]
        
        # Draw segitiga
        draw_fillpolygon(segitigaRotasi2[i], n, col)

        # Rotate segitiga
        for j in range(n):
            segitigaRotasi2[i][j] = operatorBintangVector3D_t(matrix3DZ, segitigaRotasi2[i][j])             

def segitiga_rotasi():    
    n = 3
    col = [0.0, 0.0, 1.0]    
    
    # Rotation matrix
    matrix3DZ = [
        [math.cos(sudut/57.3), -1 * math.sin(sudut/57.3), 0.0],
        [math.sin(sudut/57.3), math.cos(sudut/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]
    
    # Draw segitiga
    draw_polyline(segitigaRotasi, n, col)

    # Rotate segitiga
    for i in range(n):
        segitigaRotasi[i] = operatorBintangVector3D_t(matrix3DZ, segitigaRotasi[i])

def segitiga_vertikal():
    n = 3
    col = [1.0, 0.0, 0.0]

    for i in range(6):
        # Vertikal Translation matrix
        matrixVertikalTranslation = [0.0, 2.0, 0.0]

        # Draw segitiga
        draw_polyline(segitigaVertikal[i], n, col)

        # Move segitiga
        for j in range(n):
            segitigaVertikal[i][j] = operatorTambahVector3D_t(matrixVertikalTranslation, segitigaVertikal[i][j])

def segitiga_horizontal():
    n = 3
    col = [1.0, 0.0, 0.0]

    for i in range(4):
        # Horizontal Translation matrix
        matrixVertikalTranslation = [2.0, 0.0, 0.0]

        # Draw segitiga
        draw_fillpolygon(segitigaHorizontal[i], n, col)

        # Move segitiga
        for j in range(n):
            segitigaHorizontal[i][j] = operatorTambahVector3D_t(matrixVertikalTranslation, segitigaHorizontal[i][j])

# ========== Drawing Function =============
def draw0():
    sumbu_koordinat()
    # bintang_rotasi()
    # bintang_scale()
    # segitiga_rotasi()
    # segitiga_rotasi2()
    # segitiga_vertikal()
    # segitiga_horizontal()          

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
glutTimerFunc(1000//1, timer, 1)
glutMainLoop()  # Keeps the above created window displaying/running in a loop