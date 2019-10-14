# Read the i2c Honeywell HAFBSF0200C2AX3 Flow Sensor on Raspberry Pi
# https://www.mouser.ch/datasheet/2/187/honeywell-sensing-airflow-zephyr-haf-series-digita-740409.pdf
# Q3 2019 Python 3.7

import pigpio
import time

pi = pigpio.pi()    # Connect to local Raspberry Pi.


class Flow_Sensor:
    def __init__(self):

        self.i2c_handle     = 1     # A number referencing an object opened by one of the following
        self.i2c_address    = 0x29  # The address of a device on the I2C bus.
        self.flow_value     = None  # The sensor value

    def read_value(self):
        """
        - opens the i2c port
        - reads the data.
        - Unpack the data and return it
        count:  The number of bytes of data to be transferred.
        data:   Data to be transmitted, a series of bytes.
        reg:    An I2C device register. The usable registers depend on the actual device.
        """
        device = pi.i2c_open(self.i2c_handle, self.i2c_address)
        count, data = pi.i2c_read_device(device, 2) # 2 = reg
        pi.i2c_close(device)
        self.flow_value = int.from_bytes(data, "big")


# Example

Flow = Flow_Sensor()
if __name__ == '__main__':
    while True:
        """
        creates a loop and prints the value every 0.3 seconds
        """
        Flow.read_value()
        print(Flow.flow_value)
        time.sleep(0.3)
