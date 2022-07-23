from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

# ========== Single 2D Object ============
def draw_point(x, y):
    glColor3f(1.0,0.0,0.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_line(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINES)
    for i in range(n):
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

def draw_polyline(pnt, n, col):
    glColor3f(col[0], col[1], col[2])
    glBegin(GL_LINE_STRIP)
    for i in range(n):
        glVertex2f(pnt[i][0], pnt[i][1])
    glEnd()

def draw_polygon(pnt, n, col):
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

def bintang_koordinat(x, y, col):
    bintang = [[80-x, 146-y], [99-x,90-y], [157-x,90-y], [110-x,55-y], [128-x,1-y],
               [80-x,34-y], [32-x,1-y], [54-x,55-y], [3-x,90-y], [63-x,90-y]]
    draw_polygon(bintang, 10, col)

# ========== Multiple 2D Object ============
def buat_titik():
    draw_point(100, 50)
    draw_point(100, 150)
    draw_point(100, 100)

def sumbu_koordinat():
    sumbuX = [[-200.0, 0.0], [200.0, 0.0]]
    sumbuY = [[0.0, -200.0], [0.0, 200.0]]
    col = [0.0, 0.0, 1.0]

    draw_line(sumbuX, 2, col)
    draw_line(sumbuY, 2, col)

def tv_rusak():
    glColor3f(random.random(), random.random(), random.random())
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(220):
        a = round(random.random(), 2) * 750
        b = round(random.random(), 2) * 750
        glVertex2f(a, b)
        glVertex2f(-a, b)
        glVertex2f(a, -b)
        glVertex2f(-a, -b)
    glEnd()

def segitiga():
    segitiga01 = [[-20.0, 60.0], [20.0, 60.0], [0.0, 100.0]]
    segitiga02 = [[-20.0, -60.0], [20.0, -60.0], [0.0, -100.0]]
    segitiga03 = [[60.0, 20.0], [60.0, -20.0], [100.0, 0.0]]
    segitiga04 = [[-60.0, 20.0], [-60.0, -20.0], [-100.0, 0.0]]
    col = [0.0, 1.0, 0.0]
    draw_fillpolygon(segitiga01, 3, col)
    draw_fillpolygon(segitiga02, 3, col)
    draw_fillpolygon(segitiga03, 3, col)
    draw_fillpolygon(segitiga04, 3, col)

    segitiga05 = [[40.0, 40.0], [60.0, 100.0], [80.0, 40.0]]
    segitiga06 = [[-40.0, 40.0], [-60.0, 100.0], [-80.0, 40.0]]
    segitiga07 = [[-40.0, -40.0], [-60.0, -100.0], [-80.0, -40.0]]
    segitiga08 = [[40.0, -40.0], [60.0, -100.0], [80.0, -40.0]]
    col1 = [1.0, 0.0, 0.0]
    draw_polygon(segitiga05, 3, col1)
    draw_polygon(segitiga06, 3, col1)
    draw_polygon(segitiga07, 3, col1)
    draw_polygon(segitiga08, 3, col1)

def persegi():
    persegi01 = [[100.0, 40.0], [140.0, 40.0], [140.0, 80.0], [100.0, 80.0]]
    persegi02 = [[100.0, -40.0], [140.0, -40.0], [140.0, -80.0], [100.0, -80.0]]
    persegi03 = [[-100.0, 40.0], [-140.0, 40.0], [-140.0, 80.0], [-100.0, 80.0]]
    persegi04 = [[-100.0, -40.0], [-140.0, -40.0], [-140.0, -80.0], [-100.0, -80.0]]
    col = [0.0, 0.0, 1.0]
    draw_fillpolygon(persegi01, 4, col)
    draw_fillpolygon(persegi02, 4, col)
    draw_fillpolygon(persegi03, 4, col)
    draw_fillpolygon(persegi04, 4, col)

def bintang():
    red_color = [1.0, 0.0, 0.0]
    blue_color = [0.0, 0.0, 1.0]
    bintang_koordinat(80, 65, red_color)
    bintang_koordinat(190, 65, blue_color)
    bintang_koordinat(-20, 65, blue_color)
    bintang_koordinat(80, 170, blue_color)
    bintang_koordinat(80, -40, blue_color)

# ========== Drawing Function =============
def draw0():
    # ===== Pertemuan 2 =====
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
    # tv_rusak()

    # ===== Pertemuan 3 =====
    # sumbu_koordinat()
    # segitiga()
    # persegi()
    bintang()

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