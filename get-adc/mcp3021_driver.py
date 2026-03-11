import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_i2c_block_data(self.address, 0x00, 2)
        number = (data[0] << 2) | (data[1] >> 6)
        if self.verbose:
            print(f"Принятые данные: {data}, Число {number}")
        return number
    def get_voltage(self):
        return self.get_number()/1023*self.dynamic_range

if __name__ == "__main__":
    try:
        adc = MCP3021(5.0)
        while True:
            print("Напряжение:", adc.get_voltage(), "В")
            time.sleep(0.5)
    finally:
        adc.deinit()