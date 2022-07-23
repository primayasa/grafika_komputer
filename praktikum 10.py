from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

vertices = [
        [-100, -100, 100],
        [100, -100, 100],
        [100, 100, 100],
        [-100, 100, 100],
        [-100, -100, -100],
        [100, -100, -100],
        [100, 100, -100],
        [-100, 100, -100],
    ]

# ========== Draw Single 2D Object ============
def draw_polygon(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINE_LOOP)    
    for i in range(n):        
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

# ========== Transformation Function =============
def operatorBintangVector3D_t(a, b):
    c = [0.0, 0.0, 0.0]   
    for i in range(3):        
        for j in range(3):
            c[i] += a[i][j] * b[j]                 
    return c

# ========== Drawing Function ============
def initRot3DMatrix(sudut_rotasi):
    cos = math.cos(sudut_rotasi/57.3)
    sin = math.sin(sudut_rotasi/57.3)

    matrix3DX = [
        [1.0, 0.0, 0.0],
        [0.0, cos, -1 * sin],
        [0.0, sin, cos]
    ]

    matrix3DY = [
        [cos, 0.0, sin],
        [0.0, 1.0, 0.0],
        [-1 * sin, 0.0, cos]
    ]

    matrix3DZ = [
        [cos, -1 * sin, 0.0],
        [sin, cos, 0.0],
        [0.0, 0.0, 1.0]
    ]

    return matrix3DX, matrix3DY, matrix3DZ

def draw_cube():
    global vertices
    faces = [
        [0, 3, 2],
        [0, 2, 1],
        [1, 6, 2],
        [1, 5, 6],
        [4, 5, 6],
        [4, 6, 7],
        [3, 0, 7],        
        [0, 4, 7],
        [3, 2, 6],
        [3, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
    ]

    sudut_rotasi = 1
    matrix3DX, matrix3DY, matrix3DZ = initRot3DMatrix(sudut_rotasi)

    for i in range(len(vertices)):
        vertices[i] = operatorBintangVector3D_t(matrix3DZ, vertices[i])
        vertices[i] = operatorBintangVector3D_t(matrix3DY, vertices[i])
        vertices[i] = operatorBintangVector3D_t(matrix3DX, vertices[i])

    for i in range(len(faces)):
        sisi_kubus = []        
        for j in range(len(faces[i])):
            sisi_kubus.append(vertices[faces[i][j]])            
        draw_polygon(sisi_kubus, len(faces[i]), [1, 0, 0])
    
# ========== Call Drawing Function =============
def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1, 1, 1, 0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-200, 200, -200, 200) # Set window ortho
    draw_cube() # Call Drawing Function
    glutSwapBuffers()

# ========== Timer Function ============
def timer(fps):
    glutTimerFunc(1000//fps, timer, fps)
    glutPostRedisplay()

# ========== Main Fuction ============
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of the window
glutInitWindowPosition(100, 100)   # Set the position at which this windows should appear
glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046") # Set a window title
glutDisplayFunc(showScreen)
glutTimerFunc(1000//60, timer, 60)
glutMainLoop()  # Keeps the above created window displaying/running in a loop