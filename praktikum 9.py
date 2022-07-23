from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# kubus
kubus_vertices = [
    [-100, -100, 100],
    [ 100, -100, 100],
    [ 100, 100, 100],
    [-100, 100, 100],
    [-100, -100, -100],
    [ 100, -100, -100],
    [ 100, 100, -100],
    [-100, 100, -100]
]

# limas
limas_vertices = [
    [0,150,0],
    [100,0,0],
    [0,0,100],
    [-100,0,0],
    [0,0,-100]
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
    global kubus_vertices
    faces = [
        [0, 1, 2, 3],
        [1, 5, 6, 2],
        [4, 7, 6, 5],
        [0, 3, 7, 4],
        [4, 5, 1, 0],
        [2, 3, 7, 6],
    ]

    sudut_rotasi = 10
    matrix3DX, matrix3DY, matrix3DZ = initRot3DMatrix(sudut_rotasi)

    for i in range(len(kubus_vertices)):
        kubus_vertices[i] = operatorBintangVector3D_t(matrix3DZ, kubus_vertices[i])
        kubus_vertices[i] = operatorBintangVector3D_t(matrix3DY, kubus_vertices[i])
        kubus_vertices[i] = operatorBintangVector3D_t(matrix3DX, kubus_vertices[i])

    for i in range(len(faces)):
        sisi_kubus = []        
        for j in range(len(faces[i])):
            sisi_kubus.append(kubus_vertices[faces[i][j]])            
        draw_polygon(sisi_kubus, len(faces[i]), [1, 0, 0])

def draw_limas():
    global limas_vertices
    faces = [
        [0,2,1],
        [0,3,2],
        [0,4,3],
        [0,1,4],
        [1,2,3,4]
    ]

    sudut_rotasi = 10
    matrix3DX, matrix3DY, matrix3DZ = initRot3DMatrix(sudut_rotasi)

    for i in range(len(limas_vertices)):
        limas_vertices[i] = operatorBintangVector3D_t(matrix3DZ, limas_vertices[i])
        limas_vertices[i] = operatorBintangVector3D_t(matrix3DY, limas_vertices[i])
        limas_vertices[i] = operatorBintangVector3D_t(matrix3DX, limas_vertices[i])

    for i in range(len(faces)):
        sisi_limas = []        
        for j in range(len(faces[i])):
            sisi_limas.append(limas_vertices[faces[i][j]])            
        draw_polygon(sisi_limas, len(faces[i]), [1, 0, 0])
    
# ========== Call Drawing Function =============
def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1, 1, 1, 0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-200, 200, -200, 200) # Set window ortho
    # draw_cube() # Call Drawing Function
    draw_limas()
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
# glutTimerFunc(1000//10, timer, 10)
glutMainLoop()  # Keeps the above created window displaying/running in a loop