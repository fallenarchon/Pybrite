import PyBrite
import time

pb = PyBrite.PyBrite(18, 23, 24, 25)


class coord():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


v = coord(0, 0, 0)

MIN_RGB_VALUE = 0
MAX_RGB_VALUE = 1023
TRANSITION_DELAY = .0005
WAIT_DELAY = .25

vertex = [coord(0, 0, 0), coord(0, 1, 0), coord(0, 1, 1), coord(0, 0, 1), coord(1, 0, 0), coord(1, 1, 0),
          coord(1, 1, 1), coord(1, 0, 1)]

path = [0x01, 0x23, 0x76, 0x54, 0x03, 0x21, 0x56, 0x74, 0x13, 0x64, 0x16, 0x02, 0x75, 0x24, 0x35, 0x17, 0x25, 0x70]


def traverse(dx, dy, dz):
    if (dx == 0) & (dy == 0) & (dz == 0):
        return

    for i in range(MIN_RGB_VALUE, MAX_RGB_VALUE):
        v.x += dx
        v.y += dy
        v.z += dz
        pb.sendColor(v.x, v.y, v.z)
        time.sleep(TRANSITION_DELAY)

    time.sleep(WAIT_DELAY)


while True:
    v1 = 0
    v2 = 0

    v.x = MAX_RGB_VALUE if vertex[v2].x == 1 else MIN_RGB_VALUE
    v.y = MAX_RGB_VALUE if vertex[v2].y == 1 else MIN_RGB_VALUE
    v.z = MAX_RGB_VALUE if vertex[v2].z == 1 else MIN_RGB_VALUE

    for j in range(0, 2*len(path)):
        v1 = v2
        if j%2:
            v2 = path[j>>1] & 0xf
        else:
            v2 = path[j>>1] >> 4

        traverse(vertex[v2].x-vertex[v1].x, vertex[v2].y-vertex[v1].y, vertex[v2].z-vertex[v1].z)
