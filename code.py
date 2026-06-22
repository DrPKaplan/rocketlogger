# code.py
import board
import digitalio
import time

import adafruit_lps2x
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

# pressure = adafruit_lps2x.LPS22(i2c)
# accel = adafruit_adxl34x.ADXL343(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

i=0
 
while True:
#     print(
#         pressure.pressure,
#         pressure.temperature,
#         accel.acceleration
#     )
    i += 1
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(1)
    if i >= 50:
        i = 0
        time.sleep(10)
