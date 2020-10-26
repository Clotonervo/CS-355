# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Line3D():

    def __init__(self, start, end):
        self.start = start
        self.end = end


def loadOBJ(filename):
    vertices = []
    indices = []
    lines = []

    f = open(filename, "r")
    for line in f:
        t = str.split(line)
        if not t:
            continue
        if t[0] == "v":
            vertices.append(Point3D(float(t[1]), float(t[2]), float(t[3])))

        if t[0] == "f":
            for i in range(1, len(t) - 1):
                index1 = int(str.split(t[i], "/")[0])
                index2 = int(str.split(t[i + 1], "/")[0])
                indices.append((index1, index2))

    f.close()

    # Add faces as lines
    for index_pair in indices:
        index1 = index_pair[0]
        index2 = index_pair[1]
        lines.append(Line3D(vertices[index1 - 1], vertices[index2 - 1]))

    # Find duplicates
    duplicates = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            # Case 1 -> Starts match
            if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
                if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
                    duplicates.append(j)
            # Case 2 -> Start matches end
            if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
                if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
                    duplicates.append(j)

    duplicates = list(set(duplicates))
    duplicates.sort()
    duplicates = duplicates[::-1]

    # Remove duplicates
    for j in range(len(duplicates)):
        del lines[duplicates[j]]

    return lines


def loadHouse():
    house = []
    # Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    # Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    # Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    # Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    # Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))

    return house


def loadCar():
    car = []
    # Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    # Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))

    # Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car


def loadTire():
    tire = []
    # Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    # Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    # Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))

    return tire

x_position = 31
y_position = 12
z_position = -29
view_degrees = 60

def convert3Dto4D(coordinate):
    return np.matrix([[coordinate.x],
                    [coordinate.y],
                    [coordinate.z],
                    [1]])

def getWorldToCameraMatrix():
    rotation_matrix = np.matrix([[math.cos(math.radians(view_degrees)), 0, math.sin(math.radians(view_degrees)), 0],
                                   [0, 1, 0, 0],
                                   [-math.sin(math.radians(view_degrees)), 0, math.cos(math.radians(view_degrees)), 0],
                                  [0, 0, 0, 1]])
    transition_matrix = np.matrix([[1, 0, 0, -x_position],
                                 [0, 1, 0, -y_position],
                                 [0, 0, 1, -z_position],
                                 [0, 0, 0, 1]])
    return np.matmul(rotation_matrix, transition_matrix)

def getClipMatrix():
    zoom_x = 1/math.tan(math.radians(30))
    zoom_y = 1/math.tan(math.radians(30))
    near_plane = 10
    far_plane = 500

    clip_matrix = np.matrix([[zoom_x, 0, 0, 0],
                             [0, zoom_y, 0 , 0],
                             [0, 0, (near_plane + far_plane)/(far_plane - near_plane), -2*(near_plane * far_plane)/(far_plane - near_plane)],
                             [0, 0, 1, 0]])
    return clip_matrix

def clippingTest(line):
    clip_matrix = getClipMatrix()
    success = [True, True]
    points = [line[0], line[1]]
    i = 0
    # print(line[0])

    for point in points:
        result = np.matmul(clip_matrix, point)
        x = result.item(0)
        y = result.item(1)
        z = result.item(2)
        w = result.item(3)

        if w < z or -w > z:
            return False
        else:
            if w < x or -w > x or w < y or -w > y:
                success[i] = False

        i += 1



    return success[0] or success[1]

def normalizePoint(point):
    clip_matrix = getClipMatrix()

    # new_point = [point.x, point.y, point.z, 1]
    result = np.matmul(clip_matrix, point)
    x = result.item(0)
    y = result.item(1)
    z = result.item(2)
    w = result.item(3)

    x = x/w
    y = y/w


    return Point3D(x, y, 1)

def viewpointTransformation(point):
    matrix = np.matrix([[512/2, 0, 512/2],
                        [0, -512/2, 512/2],
                        [0, 0, 1]])
    point_matrix = [point.x, point.y, point.z]
    result = np.matmul(matrix, point_matrix)

    return Point(result.item(0), result.item(1))

def objectToWorld(line, transformation_matrix):
    i = 0

    for point in line:
        result = np.matmul(transformation_matrix, point)
        x = result.item(0)
        y = result.item(1)
        z = result.item(2)
        w = result.item(3)
        line[i] = np.matrix([[x],[y],[z],[w]])
        i += 1

    return line

def drawHouse(transformation_matrix):
    for s in loadHouse():
        line = []
        line.append(convert3Dto4D(s.start))
        line.append(convert3Dto4D(s.end))
        line = objectToWorld(line, transformation_matrix)

        world_to_camera_matrix = getWorldToCameraMatrix()

        line[0] = np.matmul(world_to_camera_matrix, line[0])
        line[1] = np.matmul(world_to_camera_matrix, line[1])

        passesClipping = clippingTest(line)

        if (passesClipping):
            line[0] = normalizePoint(line[0])
            line[1] = normalizePoint(line[1])

            line[0] = viewpointTransformation(line[0])
            line[1] = viewpointTransformation(line[1])
            line.append(RED);
            linelist.append(line)

def drawHouses():
    x = 0
    for i in range(0, 3):
        transformation_matrix = np.matrix([[1, 0, 0, x],
                                           [0, 1, 0, 0],
                                           [0, 0, 1, 0],
                                           [0, 0, 0, 1]])
        drawHouse(transformation_matrix)
        x += 15

    x = -15
    z = 20
    for i in range(0, 1):
        transformation_matrix = np.matrix([[1, 0, 0, x],
                                           [0, 1, 0, 0],
                                           [0, 0, 1, z],
                                           [0, 0, 0, 1]])
        rotation_matrix = np.matrix([[math.cos(math.radians(90)), 0, math.sin(math.radians(90)), 0],
                                     [0, 1, 0, 0],
                                     [-math.sin(math.radians(90)), 0, math.cos(math.radians(90)), 0],
                                     [0, 0, 0, 1]])
        transformation_matrix = np.matmul(transformation_matrix, rotation_matrix)
        drawHouse(transformation_matrix)
        z += 20

    x = 0
    for i in range(0, 3):
        transformation_matrix = np.matrix([[1, 0, 0, x],
                                           [0, 1, 0, 0],
                                           [0, 0, 1, z],
                                           [0, 0, 0, 1]])
        rotation_matrix = np.matrix([[math.cos(math.radians(180)), 0, math.sin(math.radians(180)), 0],
                                     [0, 1, 0, 0],
                                     [-math.sin(math.radians(180)), 0, math.cos(math.radians(180)), 0],
                                     [0, 0, 0, 1]])
        transformation_matrix = np.matmul(transformation_matrix, rotation_matrix)
        drawHouse(transformation_matrix)
        x += 15

def drawWheel(transformation_matrix):
    for s in loadTire():
        line = []
        line.append(convert3Dto4D(s.start))
        line.append(convert3Dto4D(s.end))
        line = objectToWorld(line, transformation_matrix)

        world_to_camera_matrix = getWorldToCameraMatrix()

        line[0] = np.matmul(world_to_camera_matrix, line[0])
        line[1] = np.matmul(world_to_camera_matrix, line[1])

        passesClipping = clippingTest(line)

        if (passesClipping):
            line[0] = normalizePoint(line[0])
            line[1] = normalizePoint(line[1])

            line[0] = viewpointTransformation(line[0])
            line[1] = viewpointTransformation(line[1])
            line.append(BLUE);
            linelist.append(line)

def drawCar():
    transformation_matrix = np.matrix([[1, 0, 0, 15],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 25],
                                       [0, 0, 0, 1]])

    for s in loadCar():
        # BOGUS DRAWING PARAMETERS SO YOU CAN SEE THE HOUSE WHEN YOU START UP
        line = []
        line.append(convert3Dto4D(s.start))
        line.append(convert3Dto4D(s.end))
        line = objectToWorld(line, transformation_matrix)

        wheelLocations = [[-2,-2], [2,2], [2,-2], [-2,2]]
        for x in range(0,4):
            location = wheelLocations[x]
            wheelMatrix = np.matrix([[1, 0, 0, location[0]],
                                    [0, 1, 0, 0],
                                    [0, 0, 1, location[1]],
                                    [0, 0, 0, 1]])

            drawWheel(np.matmul(transformation_matrix, wheelMatrix))

        world_to_camera_matrix = getWorldToCameraMatrix()

        line[0] = np.matmul(world_to_camera_matrix, line[0])
        line[1] = np.matmul(world_to_camera_matrix, line[1])

        passesClipping = clippingTest(line)

        if (passesClipping):
            line[0] = normalizePoint(line[0])
            line[1] = normalizePoint(line[1])

            line[0] = viewpointTransformation(line[0])
            line[1] = viewpointTransformation(line[1])
            line.append(GREEN)
            linelist.append(line)


# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")

# Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0, 0.0)
end = Point(0.0, 0.0)

# Loop until the user clicks the close button.
while not done:
    linelist = []
    # This limits the while loop to a max of 100 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # Controller Code#
    #####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]:
        z_position = z_position + math.cos(math.radians(view_degrees))
        x_position = x_position - math.sin(math.radians(view_degrees))
        # Zoom in

    if pressed[pygame.K_s]:
        # Zoom out
        z_position = z_position - math.cos(math.radians(view_degrees))
        x_position = x_position + math.sin(math.radians(view_degrees))

    if pressed[pygame.K_r]:
        # Pan up
        y_position = y_position + 1

    if pressed[pygame.K_f]:
        # Pan Down
        y_position = y_position - 1

    if pressed[pygame.K_a]:
        # Pan left
        z_position = z_position + math.cos(math.radians(view_degrees + 90))
        x_position = x_position - math.sin(math.radians(view_degrees + 90))

    if pressed[pygame.K_d]:
        # Pan right
        z_position = z_position + math.cos(math.radians(view_degrees - 90))
        x_position = x_position - math.sin(math.radians(view_degrees - 90))

    if pressed[pygame.K_q]:
        # look left
        view_degrees = view_degrees + 1

    if pressed[pygame.K_e]:
        # look right
        view_degrees = view_degrees - 1

    if pressed[pygame.K_h]:
        # Return to original position
        x_position = 0
        y_position = 0
        z_position = 0
        view_degrees = 0

    # Viewer Code#
    #####################################################################

    drawHouses()
    drawCar()

    for line in linelist:
        pygame.draw.line(screen, line[2], (line[0].x, line[0].y), (line[1].x, line[1].y))

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
