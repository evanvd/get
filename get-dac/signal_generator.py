import numpy
import time


def get_sin_wave_amplitude(freq, time):
    """
    Возвращает сдвинутую вверх и нормализованную форму функции sin(2*pi*f*t).
    Область значений от -1 до 1 сдвигается вверх и становится от 0 до 2,
    затем приводится к диапазону от 0 до 1.
    """
    return (numpy.sin(2 * numpy.pi * freq * time) + 1) / 2


def wait_for_sampling_period(sampling_frequency):
    """
    Ждёт в течение одного периода дискретизации.
    """
    period = 1 / sampling_frequency
    time.sleep(period)
