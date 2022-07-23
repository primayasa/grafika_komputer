from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

# ========== Object Global Variable============
# TATA SURYA
# sudut rotasi
sudut_rotasi = 2
sudut_tutup_atas = -2
sudut_tutup_bawah = 2

hitung_sudut_tutup_bawah = 0
hitung_sudut_tutup_atas = 0

# sudut bumi, bulan
sudut = [0, 0]

# koordinat bumi
x_bumi = 0
y_bumi = 0

sinar_matahari = [
    [[-20.0, 60.0, 0.0], [20.0, 60.0, 0.0], [0.0, 100.0, 0.0]],
    [[-20.0, -60.0, 0.0], [20.0, -60.0, 0.0], [0.0, -100.0, 0.0]],
    [[60.0, 20.0, 0.0], [60.0, -20.0, 0.0], [100.0, 0.0, 0.0]],
    [[-60.0, 20.0, 0.0], [-60.0, -20.0, 0.0], [-100.0, 0.0, 0.0]]
]

# GELAS & TUTUPNYA
tutup_bawah = [[20.0, 60.0, 0.0], [0.0, 60.0, 0.0], [0.0, 180.0, 0.0], [20.0, 180.0, 0.0]]
gelas = [[20.0, -60.0, 0.0], [0.0, -60.0, 0.0], [0.0, 60.0, 0.0], [20.0, 60.0, 0.0]]    
tutup_atas = [[20.0, -180.0, 0.0], [0.0, -180.0, 0.0], [0.0, -60.0, 0.0], [20.0, -60.0, 0.0]]

# GELOMBANG SINUS
pengurang = 360

# ========== Transformation Function =============
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

# ========== Draw Single 2D Object ============
def draw_point(x, y):
    glColor3f(1.0,0.0,0.0)
    glPointSize(5)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_point_custom(x, y, size):
    glColor3f(1.0,0.0,0.0)
    glPointSize(size)
    glEnable(GL_POINT_SMOOTH)
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

# ========== Custom Draw Single 2D Object ============
def lingkaran_custom(x, y, r, red, green, blue):
    col = [red, green, blue]
    circle = [[],[]]*360
    for i in range(360):
        circle[i] = [r * math.cos(i*3.14/180) + x, r * math.sin(i*3.14/180) + y]
    draw_polygon(circle, 360, col)

def lingkaran_custom_solid(x, y, r, red, green, blue):
    col = [red, green, blue]
    circle = [[],[]]*360
    for i in range(360):
        circle[i] = [r * math.cos(i*3.14/180) + x, r * math.sin(i*3.14/180) + y]
    draw_fillpolygon(circle, 360, col)

def titik_berputar_custom(size, a, b, r, arah_putar, i):
    global sudut, x_bumi, y_bumi
    teta = sudut[i]/57.3
    x = r*math.cos(teta) + a
    y = r*math.sin(teta) + b
    draw_point_custom(x, y, size)
    sudut[i] = sudut[i] + arah_putar
    if sudut[i] <= -360:
        sudut[i]=0.0
    if i == 0:
        x_bumi = x        
        y_bumi = y        

# ========== Drawing Function ============
def garis_koordinat():
    sumbuX = [[0.0, 0.0], [0.0, 0.0]]
    sumbuY = [[0.0, 0.0], [0.0, 0.0]]
    col = [0.862, 0.862, 0.862]

    draw_line(sumbuX, 2, col)
    draw_line(sumbuY, 2, col)
    
    y = -1.0
    for i in range(11):
        sumbuX = [[-360.0, y], [360.0, y]]
        y = y + 0.2
        draw_line(sumbuX, 2, col)
    
    x = -360
    for i in range(12):
        sumbuY = [[x, -360.0], [x, 360.0]]
        x = x + 60
        draw_line(sumbuY, 2, col)

def tata_surya():
    # === MATAHARI DAN SINARNYA ===
    lingkaran_custom_solid(0, 0, 50, 0.0, 1.0, 0.0)
    n = 3
    col = [1.0, 0.0, 0.0]

    # Rotation matrix
    matrix3DZ = [
        [math.cos(sudut_rotasi/57.3), -1 * math.sin(sudut_rotasi/57.3), 0.0],
        [math.sin(sudut_rotasi/57.3), math.cos(sudut_rotasi/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]    
    
    for i in range(4):       
        # Draw sinar matahari
        draw_fillpolygon(sinar_matahari[i], n, col)

        # Rotate sinar matahari
        for j in range(n):
            sinar_matahari[i][j] = operatorBintangVector3D_t(matrix3DZ, sinar_matahari[i][j])

    # === BUMI DAN ROTASINYA ===
    lingkaran_custom(0, 0, 200, 0.0, 0.0, 1.0)
    titik_berputar_custom(25, 0, 0, 200, 1, 0)

    # === BULAN DAN ROTASINYA ===
    lingkaran_custom(x_bumi, y_bumi, 50, 0.0, 0.0, 1.0)    
    titik_berputar_custom(10, x_bumi, y_bumi, 50, 5, 1)
    
def tutup_gelas():
    global sudut_tutup_bawah
    global sudut_tutup_atas
    global hitung_sudut_tutup_atas
    global hitung_sudut_tutup_bawah

    col = [0.0, 0.0, 1.0]
    col2 = [1.0, 0.0, 0.0]

    # === GELAS ===
    draw_fillpolygon(gelas, 4, col)

    # === TUTUP GELAS ATAS ===
    n = 4   
    matrix3DZ = [
        [math.cos(sudut_tutup_atas/57.3), -1 * math.sin(sudut_tutup_atas/57.3), 0.0],
        [math.sin(sudut_tutup_atas/57.3), math.cos(sudut_tutup_atas/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]

    draw_polygon(tutup_atas, n, col2)

    # putar tutup gelas atas
    titik_putar_atas = [0.0, 60.0, 0.0]
    for i in range(4):
        for j in range(3):        
            tutup_atas[i][j] = tutup_atas[i][j] + titik_putar_atas[j]

    for i in range(n):
        tutup_atas[i] = operatorBintangVector3D_t(matrix3DZ, tutup_atas[i])
    
    for i in range(4):
        for j in range(3):        
            tutup_atas[i][j] = tutup_atas[i][j] - titik_putar_atas[j]

    hitung_sudut_tutup_atas += 1
    if(hitung_sudut_tutup_atas == 45):
        hitung_sudut_tutup_atas = 0
        sudut_tutup_atas *= -1
    
    # === TUTUP GELAS BAWAH ===
    n = 4   
    matrix3DZ = [
        [math.cos(sudut_tutup_bawah/57.3), -1 * math.sin(sudut_tutup_bawah/57.3), 0.0],
        [math.sin(sudut_tutup_bawah/57.3), math.cos(sudut_tutup_bawah/57.3), 0.0],
        [0.0, 0.0, 0.0]
    ]
    draw_polygon(tutup_bawah, 4, col2)

    # putar tutup gelas bawah
    titik_putar_bawah = [0.0, -60.0, 0.0]
    for i in range(4):
        for j in range(3):        
            tutup_bawah[i][j] = tutup_bawah[i][j] + titik_putar_bawah[j]

    for i in range(n):
        tutup_bawah[i] = operatorBintangVector3D_t(matrix3DZ, tutup_bawah[i])

    for i in range(4):
        for j in range(3):        
            tutup_bawah[i][j] = tutup_bawah[i][j] - titik_putar_bawah[j]        

    hitung_sudut_tutup_bawah += 1
    if(hitung_sudut_tutup_bawah == 45):
        hitung_sudut_tutup_bawah = 0
        sudut_tutup_bawah *= -1
              
def gelombang():  
    garis_koordinat()    
    global pengurang

    # Gelombang sinus
    sinus = [[]]*720
    for i in range(720):
        y = i*2+pengurang
        sinus[i] = [i*2-360, math.sin(y/57.3)]

    col = [0, 0, 1]
    draw_polyline(sinus, 360, col)

    # Gerakan gelombang
    pengurang = pengurang + 1
    if pengurang == 720:
        pengurang = 360

    # Bola
    draw_point_custom(-100, sinus[130][1], 20)

# ========== Call Drawing Function =============
def draw0():
    # tata_surya()
    tutup_gelas()
    # gelombang()          

def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1.0,1.0,1.0,0.0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-300.0, 300.0, -300.0, 300.0) # Set window ortho
    # gluOrtho2D(-360.0, 360.0, -1.1, 1.1) # Window ortho for gelombang sin
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