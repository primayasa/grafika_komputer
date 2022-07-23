from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def showScreen():
    glClearColor(1.0,1.0,1.0,0.0) # Window background color
    glLoadIdentity() # Reset all graphic/shape's position
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0) # Set window ortho
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(400, 400)   # Set the w and h of the window
glutInitWindowPosition(200, 200)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"Drawing by Wahyu Primayasa 2110191046") # Set a window title
glutDisplayFunc(showScreen)
glutMainLoop()  # Keeps the above created window displaying/running in a loop