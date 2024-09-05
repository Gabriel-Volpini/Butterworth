# Butterworth Filter Implementation

Welcome to the **Butterworth Filter Implementation** repository! This project documents my journey of developing a Butterworth filter to process sensor data, a challenge that significantly pushed me beyond my comfort zone. Leveraging my Python programming skills and my background in electronics from my technician degree, I navigated the complexities of signal processing to achieve this implementation.

## Introduction

Signal processing is a crucial field in engineering and applied sciences, encompassing the analysis, manipulation, and interpretation of signals. Signals are representations of time-varying or spatially varying physical quantities, such as sound, electromagnetic radiation, images, or sensor data. The primary objective of signal processing is to extract meaningful information from these signals, enhance their quality, or transform them for specific applications.

## What is a Filter?

A filter is like a gatekeeper for signals. Signals can be any form of information, such as sound waves, light, or electrical signals in a computer. Filters allow certain parts of a signal to pass through while blocking others.

## What is a Butterworth Filter?

A **Butterworth filter** is a type of filter named after the scientist Stephen Butterworth. It is designed to have a very smooth and flat response within the frequency range you want to keep. This characteristic ensures that no ripples or distortions are introduced in the passband (the frequency range you want to retain). Think of a Butterworth filter as a smooth hill—no sudden drops or spikes, just a gradual slope that effectively separates what you want to keep from what you want to filter out.

### Types of Butterworth Filters

The Butterworth filter can be configured in three main ways:

1. **Low-pass Filter**: Allows low-frequency signals to pass through while blocking high-frequency signals. For example, hearing the bass at a party but not the chatter.
2. **High-pass Filter**: Allows high-frequency signals to pass through while blocking low-frequency signals. For example, hearing voices clearly but not the bass.
3. **Band-pass Filter**: Lets through only a specific range of frequencies, blocking everything outside this range. This is like tuning a radio to a single station.

## How the Butterworth Filter Works

The Butterworth filter is defined by a mathematical formula that dictates how it attenuates (reduces) different frequencies to achieve a smooth and flat response. It is designed to be as flat as possible in the passband and to smoothly roll off in the stopband (the range of frequencies it blocks).

### Formula

The Butterworth filter's transfer function can be expressed as:

![Butterworth Filter Formula](img1.png)

Where:

- **|H(f)|** is the magnitude of the filter’s frequency response.
- **f** is the frequency of the input signal.
- **f_c** is the cutoff frequency — the point where the filter starts to significantly attenuate the signal.
- **n** is the order of the filter, which determines how sharp the transition is between the passband and stopband.

## Practical Application: AM Modulation

One real-world application of the Butterworth filter is in **Amplitude Modulation (AM) used in radios**. In AM, the amplitude (or strength) of a carrier wave is varied in proportion to the signal (like music or voice) you want to transmit. A Butterworth filter can be used to extract the original signal components from the modulated carrier wave, providing a clean and accurate reproduction of the transmitted signal.

![AM Modulation Example](img2.png)

## Project Files

- `butterworth_filter.py`: Contains the Python implementation of the Butterworth filter.
- `examples/`: A folder containing examples of the filter applied to different types of signals.
- `docs/`: Documentation files explaining the mathematical background and practical usage of the Butterworth filter.

## Getting Started

To use the Butterworth filter in your own projects, follow these steps:

1. **Clone the repository**:

   ````bash
   git clone https://github.com/yourusername/butterworth-filter.git```

   ````

2. **Install the required dependencies**:

   ```bash
    pip install -r requirements.txt
   ```

3. **Run the example scripts to see the filter in action:**:
   ```bash
   python examples/low_pass_filter_example.py
   ```
