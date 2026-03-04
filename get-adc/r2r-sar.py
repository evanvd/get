from r2r_adc import R2R_ADC
import time
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

# Dynamic range should be measured with a multimeter
DYN_RANGE = 3.3
# Duration of the experiment in seconds
duration = 3.0

adc = R2R_ADC(dynamic_range=DYN_RANGE, compare_time=0.0001)

voltage_values = []
time_values = []


try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        current_time = time.time() - start_time
        
        voltage_values.append(voltage)
        time_values.append(current_time)
        print(f"Time: {current_time:.2f}s, Voltage: {voltage:.2f}V")

    plot_voltage_vs_time(time_values, voltage_values, DYN_RANGE)
    plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
