import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ========== Tabung Object ============
# tabung vertices 
radius = 50
height = 250

circle = []
for i in range(32):
    titik = []
    titik.append(round(radius * math.cos(i * 3.14/8),2))
    titik.append(round(radius * math.sin(i * 3.14/8),2))
    if(i<16):        
        titik.append(20)
    else:        
        titik.append(-1 * height)
    circle.append(titik)

for i in range(16):
    faces = []
    for i in range(16):
        if(i!=15):
            faces.append([i, 16+i, 17+i, i+1])
        else:
            faces.append([15, 31, 16, 0])

# ========== Read / Write OFF file ============
def saveFile(vertices, faces, fileName):
    fileName = fileName + ".off"
    numVertices = str(len(vertices))
    numFaces = str(len(faces))
    secondLine = str("\n" + numVertices + " " + numFaces + " 0")

    offFile = open(fileName, "w")       
    offFile.write("OFF")    
    offFile.write(secondLine)

    r, g, b, a = 255, 255, 255, 255

    for vertice in vertices:
        # line = '\n{} {} {} {} {} {} {}'.format(vertice[0], vertice[1], vertice[2], r, g, b, a)
        line = '\n{} {} {}'.format(vertice[0], vertice[1], vertice[2])
        offFile.write(line)

    for face in faces:
        line = str(len(face))
        for vertice in face:
            line = line + " " + str(vertice)
        line = "\n" + line 
        offFile.write(line)

    offFile.close() 

def readFile(fileName):
    fileName = fileName + ".off"
    offFile = open(fileName, "r")
    firstLine = offFile.readline().split()
    # print(firstLine)

    if(firstLine[0] == "OFF"):
        secondLine = offFile.readline().split()
        numVertices = int(secondLine[0])
        numFaces = int(secondLine[1])
        # print(numVertices, numFaces)

        # read vertices
        vertices = []
        for i in range(numVertices):
            line = offFile.readline().split()
            vertice = line[:3]

            for j in range(3):
                vertice[j] = float(vertice[j])
            print(vertice)
            vertices.append(vertice)

        # read faces
        faces = []
        for i in range(numFaces):
            line = offFile.readline().split()
            face = line[1:]
            
            for j in range(len(face)):
                face[j] = float(face[j])
            print(face)
            faces.append(face)

    else:
        print("Error! Not supported file")
        return 1

    # return vertices, faces

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
def operatorPerkalian(a, b):
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
        circle[i] = operatorPerkalian(matrix3DZ, circle[i])
        circle[i] = operatorPerkalian(matrix3DY, circle[i])
        circle[i] = operatorPerkalian(matrix3DX, circle[i])

def draw_tabungroda():    
    global circle
    global faces

    rotateVertices()
    for i in range(len(faces)):
        sisi = []        
        for j in range(len(faces[i])):
            sisi.append(circle[faces[i][j]])            
        draw_polygon(sisi, len(faces[i]), [1, 0, 0])    

# ========== Call Drawing Function =============
def showScreen():    
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1, 1, 1, 0)
    glLoadIdentity()
    gluOrtho2D(-300, 300, -300, 300)
    draw_tabungroda()
    glutSwapBuffers()

# ========== Timer Function ============
def timer(fps):
    glutTimerFunc(1000//fps, timer, fps)
    glutPostRedisplay()

# ========== Main Fuction ============
# glutInit()
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(500, 500)
# glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046")
# glutDisplayFunc(showScreen)
# glutTimerFunc(1000//60, timer, 60)
# glutMainLoop()

saveFile(circle, faces, "tabungku")
readFile("tabungku")