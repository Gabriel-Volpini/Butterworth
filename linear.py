import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal


def generate_waveform(frequency, amplitude_ac, dc_offset, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    ac_component = amplitude_ac * np.sin(2 * np.pi * frequency * t)
    dc_component = dc_offset * np.ones_like(t)
    waveform = ac_component + dc_component
    return t, ac_component, dc_component, waveform


# Example usage:
frequency = 5  # Hz
amplitude_ac = 1.0  # Amplitude of the AC component
dc_offset = 2.0  # DC offset
duration = 2.0  # seconds
sampling_rate = 1000  # samples per second

t, ac_component, dc_component, waveform = generate_waveform(
    frequency, amplitude_ac, dc_offset, duration, sampling_rate
)

#####################################################################


def low_pass_filter(data, cutoff, fs, order=2):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(order, normal_cutoff, btype="low", analog=False)
    y = signal.filtfilt(b, a, data)
    return y


def band_pass_filter(data, low_cutoff, high_cutoff, fs, order=4):
    nyquist = 0.5 * fs
    low = low_cutoff / nyquist
    high = high_cutoff / nyquist
    b, a = signal.butter(order, [low, high], btype="band", analog=False)
    y = signal.filtfilt(b, a, data)
    return y


ir_dc = low_pass_filter(waveform, 0.05, 100)
ir_ac = band_pass_filter(waveform, 0.5, 3, 100)

#####################################################################

# Plotting the components and the combined waveform
plt.figure(figsize=(16, 10))

plt.subplot(5, 1, 1)
plt.plot(t, ac_component, label="AC Component")
plt.title("AC Component")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(t, dc_component, label="Linear Wave DC Component", color="orange")
plt.title("Square Wave DC Component")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(t, waveform, label="Combined Waveform", color="green")
plt.title("Combined Waveform")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 4)
plt.plot(t, ir_dc, label="Filtered DC", color="purple")
plt.title("Filtered DC")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 5)
plt.plot(t, ir_ac, label="Filtered AC", color="black")
plt.title("Filtered AC")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
