import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)

photo = 6
led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)
while True:
    sensore = GPIO.input(photo)
    GPIO.output(led,not sensore)
