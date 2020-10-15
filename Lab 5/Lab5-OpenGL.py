import sys

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
    import math
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
isPerspective = True
isOrtho = False
x_position = 0.0
y_position = 0.0
z_position = 0.0
view_degrees = 0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    global x_position
    global y_position
    global z_position
    global view_degrees

    if isOrtho:
        glOrtho(-10.0, 10.0, -3.0, 10.0, -10.0, 10.0)
    elif isPerspective:
        gluPerspective(45.0, 1.0, 0.1, 50.0)

    glRotated(view_degrees, 0, 1, 0)
    glTranslated(x_position, y_position, z_position)

    
    drawHouse()

    
    glFlush()
    

def keyboard(key, x, y):

    global isOrtho
    global isPerspective
    global x_position
    global y_position
    global z_position
    global view_degrees
    
    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        z_position = z_position + math.cos(math.radians(view_degrees))
        x_position = x_position - math.sin(math.radians(view_degrees))
        # Zoom in

    if key == b's':
        # Zoom out
        z_position = z_position - math.cos(math.radians(view_degrees))
        x_position = x_position + math.sin(math.radians(view_degrees))

    if key == b'r':
        # Pan up
        y_position = y_position - 1

    if key == b'f':
        # Pan Down
        y_position = y_position + 1

    if key == b'a':
        # Pan left
        z_position = z_position + math.cos(math.radians(view_degrees - 90))
        x_position = x_position - math.sin(math.radians(view_degrees - 90))

    if key == b'd':
        # Pan right
        z_position = z_position + math.cos(math.radians(view_degrees + 90))
        x_position = x_position - math.sin(math.radians(view_degrees + 90))

    if key == b'q':
        # look left
        view_degrees = view_degrees - 1

    if key == b'e':
        # look right
        view_degrees = view_degrees + 1

    if key == b'h':
        # Return to original position
        glMatrixMode(GL_PROJECTION)
        x_position = 0
        y_position = 0
        z_position = 0
        view_degrees = 0

    if key == b'o':
        # Orthographic projection mode
        isOrtho = True
        isPerspective = False


    if key == b'p':
        # Perspective mode
        print("P is pressed")
        isOrtho = False
        isPerspective = True

    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
