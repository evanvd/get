import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 4.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(4.2, verbose=False)

    t = 0
    while True:
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = value * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1 / sampling_frequency

finally:
    dac.deinit()
