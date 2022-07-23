from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# tabung vertices
radius = 50
height = 250

circle = []
for i in range(32):
    titik = []
    titik.append(radius * math.cos(i * 3.14/8))
    titik.append(radius * math.sin(i * 3.14/8))
    if(i<16):        
        titik.append(20)
    else:        
        titik.append(-1 * height)
    circle.append(titik)

# ========== Draw Single 2D Object ============
def draw_polygon(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINE_LOOP)    
    for i in range(n):        
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

def draw_line(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINES)
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

def rotateVertices():
    sudut_rotasi = 1
    matrix3DX, matrix3DY, matrix3DZ = initRot3DMatrix(sudut_rotasi)

    for i in range(len(circle)):
        circle[i] = operatorBintangVector3D_t(matrix3DZ, circle[i])
        circle[i] = operatorBintangVector3D_t(matrix3DY, circle[i])
        circle[i] = operatorBintangVector3D_t(matrix3DX, circle[i])

def draw_tabung():
    global vertices
    faces = []
    for i in range(16):
        if(i!=15):
            faces.append([i, 16+i, 17+i, i+1])
        else:
            faces.append([15, 31, 16, 0])

    rotateVertices()

    for i in range(len(faces)):
        sisi = []        
        for j in range(len(faces[i])):
            sisi.append(circle[faces[i][j]])            
        draw_polygon(sisi, len(faces[i]), [1, 0, 0])

def draw_roda():
    global circle
    rotateVertices()

    # draw jari jari
    for i in range(len(circle)//2):
        if(i<8):
            draw_line([circle[i], circle[i+8]], 2, [0, 0, 1])
        else:
            draw_line([circle[i+8], circle[i+16]], 2, [0, 0, 1])

    # draw busur roda
    for i in range(2):
        busur = []
        for j in range(16):
            busur.append(circle[j+i*16])            
        draw_polygon(busur, len(busur), [1, 0, 0])

def draw_tabungroda():    
    draw_tabung()
    draw_roda()    

# ========== Call Drawing Function =============
def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1, 1, 1, 0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-300, 300, -300, 300) # Set window ortho
    # draw_tabung() # Call Drawing Function
    draw_roda()
    # draw_tabungroda()
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
glutTimerFunc(1000//1, timer, 1)
glutMainLoop()  # Keeps the above created window displaying/running in a loop