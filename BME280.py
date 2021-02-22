# Vin to 3V3
# SDI to SDA
# SCK to SCL
# GND to GND
# CS  to 3V3

import time
import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1013.25

while True:
    print("Temperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" %bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altituede = %0.2f meters" % bme280.altitude)
    time.sleep(2)