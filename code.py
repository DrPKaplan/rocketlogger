# code.py
import board
import digitalio
import time

import adafruit_lps2x
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

pressure = adafruit_lps2x.LPS22(i2c)
accel = adafruit_adxl34x.ADXL343(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(
        pressure.pressure,
        pressure.temperature,
        accel.acceleration
    )
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(1)
