from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# limas
limas_vertices = [
    [0,150,0],
    [100,0,0],
    [0,0,100],
    [-100,0,0],
    [0,0,-100]
]

# ========== Draw Single 2D Object ============
def draw_fillpolygon(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_POLYGON)
    for i in range(n):
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

# ========== Operator Function =============
def operatorPengurangan(a , b):
    c = [0.0, 0.0, 0.0]   
    for i in range(3):
       c[i] = a[i] - b[i]
    return c

def operatorPerkalian(a, b):
    c = [0.0, 0.0, 0.0]   
    for i in range(3):        
        for j in range(3):
            c[i] += a[i][j] * b[j]                 
    return c

def operatorCrossProduct(a, b):
    c = [0.0, 0.0, 0.0]   
    c[0] = a[1]*b[2] - b[2]*b[1];
    c[1] = a[2]*b[0] - b[0]*b[2];
    c[2] = a[0]*b[1] - b[1]*b[0];
    return c

# ========== Init 3D Rotation Matrix ============
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

# ========== Drawing Function ============
def draw_limas():
    global limas_vertices
    faces = [
        [0,2,1],
        [0,3,2],
        [0,4,3],
        [0,1,4],
        [1,2,3,4]
    ]

    faces_color = [[0.42, 0.19, 0.75], [2.17, 0.36, 2.17], [0.75, 0.74, 0.43], [1.41, 1.84, 0.88], [0.88, 2.25, 1.03]]

    sudut_rotasi = 10
    matrix3DX, matrix3DY, matrix3DZ = initRot3DMatrix(sudut_rotasi)

    for i in range(len(limas_vertices)):
        limas_vertices[i] = operatorPerkalian(matrix3DZ, limas_vertices[i])
        limas_vertices[i] = operatorPerkalian(matrix3DY, limas_vertices[i])
        limas_vertices[i] = operatorPerkalian(matrix3DX, limas_vertices[i])

    for i in range(len(faces)):
        sisi_limas = []
        for j in range(len(faces[i])):
            sisi_limas.append(limas_vertices[faces[i][j]])

        normalVector = operatorCrossProduct(operatorPengurangan(sisi_limas[1], sisi_limas[0]),
            operatorPengurangan(sisi_limas[2], sisi_limas[0]))

        if(normalVector[2]>0):
            draw_fillpolygon(sisi_limas, len(faces[i]), faces_color[i])      
    
# ========== Call Drawing Function =============
def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1, 1, 1, 0)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)
    draw_limas()
    glutSwapBuffers()

# ========== Timer Function ============
def timer(fps):
    glutTimerFunc(1000//fps, timer, fps)
    glutPostRedisplay()

# ========== Main Fuction ============
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(500, 500)
glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046")
glutDisplayFunc(showScreen)
# glutTimerFunc(1000//60, timer, 60)
glutMainLoop()