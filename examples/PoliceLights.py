import time
import PyBrite

pb = PyBrite.PyBrite(18, 23, 24, 25)
DELAY = .05


def off():
    sb.sendColor(0, 0, 0)
    time.sleep(DELAY)


def red():
    sb.sendColor(1023, 0, 0)
    time.sleep(DELAY)
    off()


def blue():
    sb.sendColor(0, 0, 1023)
    time.sleep(DELAY)
    off()

while True:
    for i in range(0, 3):
        red()
        red()
        red()
        time.sleep(DELAY)
        blue()
        blue()
        blue()
        time.sleep(DELAY)

    for j in range(0, 6):
        red()
        time.sleep(DELAY)
        blue()
        time.sleep(DELAY)