from mcp3021_driver import MCP3021
import time
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

DYN_RANGE = 3.3
duration = 5.0

adc = MCP3021(dynamic_range=DYN_RANGE)

voltage_values = []
time_values = []


try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        voltage = adc.get_voltage()
        current_time = time.time() - start_time
        
        voltage_values.append(voltage)
        time_values.append(current_time)
        print(f"Время: {current_time:.2f}с, Напряжение: {voltage:.2f}В")

    plot_voltage_vs_time(time_values, voltage_values, DYN_RANGE)
    plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
