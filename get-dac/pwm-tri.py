import pwm_dac as pwm
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3)

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
