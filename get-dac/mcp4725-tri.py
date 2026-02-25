import mcp4725_driver as mcp
import time

amplitude = 5.0
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(5.0, verbose=False)

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
