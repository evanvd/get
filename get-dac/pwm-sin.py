import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.3)

    t = 0
    while True:
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = value * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1 / sampling_frequency

finally:
    dac.deinit()
