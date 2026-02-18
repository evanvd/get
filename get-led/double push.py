import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

up = 12
down = 10
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

sleep_time = 0.2
num = 0

try:
    while True:
        if GPIO.input(up) and GPIO.input(down):
            num = 255
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        elif GPIO.input(up):
            num = num + 1
            if num > 255:
                num = 0
            GPIO.output(leds, dec2bin(num))
            time.sleep(sleep_time)
        else:
            GPIO.output(leds, dec2bin(num))

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
