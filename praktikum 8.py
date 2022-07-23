from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

# ========== Object Global Variable============
# bola pantul
ball = [[-220, -20, 0.0], [220, 100, 0.0], [60, -60, 0.0]]
translation_dir = [[2, 2, 0], [2, 2, 0], [2, 2, 0]]

# roda berputar
sudut = [0, 0, 180, 180]
roda_size = 40
roda = [[-300, 100, 0.0],
        [-400, 100, 0.0]]
roda_dir = [[2, 0, 0],
            [2, 0, 0]]

batang_roda1 = [[roda[0][0], roda[0][1], 0],
                [roda[1][0], roda[1][1], 0]]
batang_roda2 = [[roda[0][0], roda[0][1], 0],
                [roda[1][0], roda[1][1], 0]]

# pacman
pacman_coor = [-300, -100, 0]
pacman_dir = [2, 0, 0]
buka = True
counter = 0

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
def draw_point_custom(x, y, size, col):
    glColor3f(col[0], col[1], col[2])
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
    circle = [[]]*360
    for i in range(360):
        circle[i] = [r * math.cos(i*3.14/180) + x, r * math.sin(i*3.14/180) + y]
    draw_polygon(circle, 360, col)

def titik_berputar_custom(size, a, b, r, arah_putar, i):
    global sudut
    teta = sudut[i]/57.3
    x = r*math.cos(teta) + a
    y = r*math.sin(teta) + b
    # draw_point_custom(x, y, size, [0, 0, 1])
    sudut[i] = sudut[i] + arah_putar
    if sudut[i] <= -360:
        sudut[i]=0.0
    return x, y

# ========== Drawing Function ============
def bola_pantul():
    frame_size = 220
    ball_size = 30
    frame = [[-220.0, 220.0, 0.0], [220.0, 220.0, 0.0], [220.0, -220.0, 0.0], [-220.0, -220.0, 0.0]]
    ball_color = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    
    global ball
    global translation_dir

    # draw ball
    for i in range(3):
        # check x frame limit
        if ball[i][0] >= frame_size-ball_size/2:
            translation_dir[i][0] = -2
        elif ball[i][0] <= -(frame_size-ball_size/2):
            translation_dir[i][0] = 2

        # check y frame limit
        if ball[i][1] >= frame_size-ball_size/2:
            translation_dir[i][1] = -2
        elif ball[i][1] <= -(frame_size-ball_size/2):
            translation_dir[i][1] = 2

        ball[i] = operatorTambahVector3D_t(translation_dir[i], ball[i])
        draw_point_custom(ball[i][0], ball[i][1], ball_size, ball_color[i])

    # draw frame
    draw_polygon(frame, 4, [1, 0, 0])

def pacman():
    # ===  RODA BERPUTAR ===
    global roda
    global batang_roda1
    global batang_roda2
    global sudut

    draw_batang_roda1 = [[0, 0, 0],
                         [0, 0, 0]]
    draw_batang_roda2 = [[0, 0, 0],
                         [0, 0, 0]]
    
    for i in range(2):
        # check x frame limit
        if roda[1][0] >= 330:
            roda = [[-300, 100, 0.0],
                    [-400, 100, 0.0]]
            batang_roda1 = [[roda[0][0], roda[0][1], 0],
                [roda[1][0], roda[1][1], 0]]
            batang_roda2 = [[roda[0][0], roda[0][1], 0],
                            [roda[1][0], roda[1][1], 0]]

        roda[i] = operatorTambahVector3D_t(roda_dir[i], roda[i])        
        batang_roda1[i] = operatorTambahVector3D_t(roda_dir[i], batang_roda1[i])
        batang_roda2[i] = operatorTambahVector3D_t(roda_dir[i], batang_roda2[i])
        lingkaran_custom(roda[i][0], roda[i][1], 30, 0.0, 0.0, 1.0)        

        draw_batang_roda1[i][0], draw_batang_roda1[i][1] = titik_berputar_custom(5, batang_roda1[i][0], batang_roda1[i][1], 30, -5, i)
        draw_batang_roda2[i][0], draw_batang_roda2[i][1] = titik_berputar_custom(5, batang_roda2[i][0], batang_roda2[i][1], 30, -5, i+2)
    
    # draw batang roda
    draw_point_custom(draw_batang_roda1[0][0], draw_batang_roda1[0][1], 5, [0, 0, 0])
    draw_point_custom(draw_batang_roda1[1][0], draw_batang_roda1[1][1], 5, [0, 0, 0])
    draw_line(draw_batang_roda1, 2, [1, 0, 0])
    draw_line(draw_batang_roda2, 2, [1, 0, 0])

    # ===  PACMAN ===
    global pacman_coor
    global buka
    global counter

    # timer buka tutup
    if(counter == 20):
        if(buka):
            buka = False
            counter = 0
        else:
            buka = True
            counter = 0

    # change pacman direction
    if pacman_coor[0] >= 270:
        pacman_dir[0] = -2
    elif pacman_coor[0] <= -270:
        pacman_dir[0] = 2
    
    pacman_coor = operatorTambahVector3D_t(pacman_coor, pacman_dir)

    if pacman_dir[0] == 2 :
        draw_point_custom(pacman_coor[0]-10, pacman_coor[1]+10, 5, [0, 0, 0])
    else :
        draw_point_custom(pacman_coor[0]+10, pacman_coor[1]+10, 5, [0, 0, 0]) 

    # draw pacman
    if(buka):
        col = [0.0, 0.0, 1.0]
        circle = [[]]*360
        if pacman_dir[0] == 2 :
            for i in range(360):            
                if(i==45):
                    circle[i] = pacman_coor
                elif(i==315):
                    circle[i] = pacman_coor
                else:
                    circle[i] = [30 * math.cos(i*3.14/180) + pacman_coor[0], 30 * math.sin(i*3.14/180) + pacman_coor[1]]
            draw_polygon(circle[44:316], 272, col)
        else:
            for i in range(360):            
                if(i==135):
                    circle[i] = pacman_coor
                elif(i==225):
                    circle[i] = pacman_coor
                else:
                    circle[i] = [30 * math.cos(i*3.14/180) + pacman_coor[0], 30 * math.sin(i*3.14/180) + pacman_coor[1]]
            del circle[136:224]
            draw_polygon(circle, 272, col)            
    else: 
        lingkaran_custom(pacman_coor[0], pacman_coor[1], 30, 0.0, 0.0, 1.0)
            
    counter += 1

# ========== Call Drawing Function =============
def draw0():
    # bola_pantul()
    pacman()          

def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glClearColor(1.0,1.0,1.0,0.0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-300.0, 300.0, -300.0, 300.0) # Set window ortho
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