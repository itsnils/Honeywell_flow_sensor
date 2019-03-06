# Read the i2c Honeywell HAFBSF0200C2AX3 Flow Sensor on Raspberry Pi
# https://www.mouser.ch/datasheet/2/187/honeywell-sensing-airflow-zephyr-haf-series-digita-740409.pdf
# Q1 2019 Python 3.5

import pigpio
import time

pi = pigpio.pi()


class Flow_Sensor:
    def __init__(self):
        self.h = 1
        self.i2c = 0x29
        self.flow = 0

    def read_value(self):
        self.device = pi.i2c_open(self.h, self.i2c)
        self.count, self.data = pi.i2c_read_device(self.device, 2)
        pi.i2c_close(self.device)
        self.flow = int.from_bytes(self.data, "big")


# Example

Flow = Flow_Sensor()

while True:
    Flow.read_value()
    print(Flow.flow)
    time.sleep(0.3)