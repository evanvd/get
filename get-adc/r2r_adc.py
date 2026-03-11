import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        binary_str = bin(number)[2:].zfill(8)
        signals = [int(bit) for bit in binary_str]
        GPIO.output(self.bits_gpio, signals)

    def sequential_counting_adc(self):
        for num in range(256):
            self.number_to_dac(num)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                return num
        return 255

    def successive_approximation_adc(self):
        tmp_bits = [0] * 8
        for i in range(8):
            tmp_bits[i] = 1
            GPIO.output(self.bits_gpio, tmp_bits)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                tmp_bits[i] = 0
        
        res_value = int("".join(map(str, tmp_bits)), 2)
        return res_value

    def get_voltage(self, method='sar'):
        if method == 'sar':
            value = self.successive_approximation_adc()
        else:
            value = self.sequential_counting_adc()
        return (value / 255.0) * self.dynamic_range

if __name__ == "__main__":
    adc = R2R_ADC(3.177)
    try:
        while True:
            voltage = adc.get_voltage(method='sar')
            print(f"Voltage: {voltage:.3f} V")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        adc.deinit()