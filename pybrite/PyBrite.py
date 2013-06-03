import RPi.GPIO as io
import time


class PyBrite(object):
    def __init__(self, data_pin, latch_pin, enable_pin, clock_pin):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.enable_pin = enable_pin
        self.clock_pin = clock_pin

        io.setmode(io.BCM)

        for pin in [data_pin, latch_pin, enable_pin, clock_pin]:
            io.setup(pin, io.OUT)
        for pin in [clock_pin, latch_pin, enable_pin]:
            io.output(pin, False)

    def sendColor(self, red, green, blue):
        packet = self.assemblePacket(0x01, 127, 127, 127)
        self.shiftOutPacket(packet)

        packet = self.assemblePacket(0, red, green, blue)
        self.shiftOutPacket(packet)

    def assemblePacket(self, commandMode, redCommand, greenCommand, blueCommand):
        packet = commandMode & 0x3
        packet = (packet << 10) | (blueCommand & 1023)
        packet = (packet << 10) | (redCommand & 1023)
        packet = (packet << 10) | (greenCommand & 1023)
        return packet

    def shiftOutPacket(self, packet):
        for i in reversed(range(0, 32)):
            io.output(self.data_pin, ((packet & (1 << i)) != 0))
            io.output(self.clock_pin, True)
            time.sleep(.0001)
            io.output(self.clock_pin, False)

        time.sleep(.001)
        io.output(self.latch_pin, True)
        time.sleep(.001)
        io.output(self.latch_pin, False)
        time.sleep(.001)
