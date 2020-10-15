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
    import Lab6Models
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
x_position = -23
y_position = -16
z_position = -49
view_degrees = -53
tire_display =[{"x":1, "z":1},{"x":-1, "z":1}, {"x":1, "z":-1}, {"x":-1, "z":-1}]
time = 0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)


def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()


def drawTire():
    glLineWidth(2.5)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    # Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    # Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    # Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()

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

def drawHouses():
    # First Row
    for x in range(0, 3):
        glPushMatrix()
        x_offset = 15 * x
        glRotatef(view_degrees, 0, 1, 0)
        glTranslate(0 + x_position - x_offset, 0 + y_position, 0 + z_position)
        drawHouse()
        glPopMatrix()

    # Second Row
    for x in range(0, 3):
        glPushMatrix()
        z_offset = 15 * x
        glRotatef(90 + view_degrees, 0, 1, 0)
        glTranslate(-40 - z_position + z_offset, 0 + y_position, -50 + x_position)
        drawHouse()
        glPopMatrix()

    # Third Row
    for x in range(0, 3):
        glPushMatrix()
        x_offset = 15 * x
        glRotatef(180 + view_degrees, 0, 1, 0)
        glTranslate(0 - x_position + x_offset, 0 + y_position, -50 - z_position)
        drawHouse()
        glPopMatrix()

def drawCarStuff():
    global time
    # print(time)
    glPushMatrix()
    glRotatef(view_degrees, 0, 1, 0)
    glTranslate(x_position - 30 + time, y_position, 12 + z_position)
    drawCar()
    for x in range(0, 4):
        drawWheel(x)
    glPopMatrix()

def drawWheel(x):
    glPushMatrix()
    global time
    # print(time)
    tranformations = tire_display[x]
    x = tranformations["x"]
    z = tranformations["z"]
    glTranslate(2*x, 0, 2*z)
    glRotatef(time*(-10), 0, 0, 1)

    drawTire()
    glPopMatrix()

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

    gluPerspective(90.0, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


    drawHouses()
    drawCarStuff()

    glFlush()
    

def keyboard(key, x, y):

    global x_position
    global y_position
    global z_position
    global view_degrees
    global time
    
    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        z_position = z_position + 1
        # Zoom in

    if key == b's':
        # Zoom out
        z_position = z_position - 1

    if key == b'r':
        # Pan up
        y_position = y_position - 1

    if key == b'f':
        # Pan Down
        y_position = y_position + 1

    if key == b'a':
        # Pan left
        x_position = x_position + 1

    if key == b'd':
        # Pan right
        x_position = x_position - 1

    if key == b'q':
        # look left
        view_degrees = view_degrees - 1

    if key == b'e':
        # look right
        view_degrees = view_degrees + 1

    if key == b'h':
        # Return to original position
        # glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x_position = -23
        y_position = -16
        z_position = -49
        view_degrees = -53
        time = 0

    glutPostRedisplay()

def updateTimer(value):
    global time
    time = time + 1
    glutPostRedisplay()
    glutTimerFunc(300, updateTimer, 0)


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(1, updateTimer,0)
glutMainLoop()