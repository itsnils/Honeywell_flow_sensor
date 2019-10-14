# Honeywell flow sensor
Read the i2c Honeywell HAFBSF0200C2AX3 flow sensor on Raspberry Pi 3B+/4B

What you need.
- Raspberry Pi 3B+ or Raspberry Pi 4B
- Sensor Honeywell HAFBSF0200C2AX3
- 4 cables 

###### installation of the pigpio library

`sudo rm -rf PIGPIO`

`wget abyz.me.uk/rpi/pigpio/pigpio.zip`

`unzip pigpio.zip`

`cd PIGPIO`

`make`

`sudo make install`

###### The Pigpio is executed at each start/restart:


Pi3B+

`sudo systemctl enable pigpiod`

Pi4B

`sudo crontab -e`

There must be written in the crontab:

`@reboot /usr/local/bin/pigpiod`
