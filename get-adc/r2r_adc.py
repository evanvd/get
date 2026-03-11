import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def __del__(self):
        self.deinit()

    def number_to_dac(self, number):
        if number < 0:
            number = 0
        if number > 255:
            number = 255

        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

def sequential_counting_adc(self):
    number = 0

    while number <= 255:
        self.number_to_dac(number)
        time.sleep(self.compare_time)

        if GPIO.input(self.comp_gpio):
            break

        number += 1

    return number
    
    def get_sc_voltage(self):
        value = self.sequential_counting_adc()
        voltage = value / 255 * self.dynamic_range
        return voltage


if __name__ == "__main__":
    adc = R2R_ADC(3.3)

    try:
        while True:
            voltage = adc.get_sc_voltage()
            print("Напряжение:", voltage, "В")
            time.sleep(0.5)

    finally:
        adc.deinit()