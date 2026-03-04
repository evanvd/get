import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup(self.bits_gpio)
        GPIO.cleanup(self.comp_gpio)

    def number_to_dac(self, number):
        bin_num = [int(i) for i in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bin_num)

    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 0:
                return i
        return 255
    
    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        return self.dynamic_range * number / 255

    def successive_approximation_adc(self):
        number = 0
        for i in range(7, -1, -1):
            number += 2**i
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 0:
                number -= 2**i
        return number

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        return self.dynamic_range * number / 255


if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range=3.3)
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.2f} В")
            time.sleep(1)
    finally:
        adc.deinit()
