import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM)

button = 13 
led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
state = 0

while True:
    if GPIO.input(button):
        state = 1 - state 
        GPIO.output(led,state)
        time.sleep(0.2)