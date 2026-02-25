import r2r_dac as r2r
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3)

    period = 1 / signal_frequency
    samples_per_period = int(sampling_frequency / signal_frequency)

    while True:
        for i in range(samples_per_period):
            t = i / samples_per_period
            if t < 0.5:
                value = 2 * t
            else:
                value = 2 * (1 - t)
            voltage = value * amplitude
            dac.set_voltage(voltage)
            time.sleep(1 / sampling_frequency)

finally:
    dac.deinit()
