import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid()
    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)
    plt.show()

def plot_sampling_period_hist(time_values):
    sampling_periods = [time_values[i] - time_values[i-1] for i in range(1, len(time_values))]
    
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods, bins=50)
    plt.title("Распределение периодов измерений")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.grid()
    plt.xlim(0, 0.06)
    plt.show()
