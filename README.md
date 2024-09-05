# Butterworth Filter Implementation

Welcome to the **Butterworth Filter Implementation** repository! This project documents the result of my journey of developing a Butterworth filter to process sensor data, a challenge that significantly pushed me beyond my comfort zone. Leveraging my Python programming skills and my background in electronics from my technician degree, I navigated the complexities of signal processing to achieve this implementation.

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

![image](https://github.com/user-attachments/assets/ab61fd85-dd6b-425d-b577-ae72e5334a9e)

![image](https://github.com/user-attachments/assets/e670d835-47e8-4304-a6d7-0052f0d0f53d)


### Formula

The Butterworth filter's transfer function can be expressed as:

![Butterworth Filter Formula](https://github.com/user-attachments/assets/e138855c-e9ad-430e-8e7b-aabe277ac5e1)

Where:

- **|H(f)|** is the magnitude of the filter’s frequency response.
- **f** is the frequency of the input signal.
- **f_c** is the cutoff frequency — the point where the filter starts to significantly attenuate the signal.
- **n** is the order of the filter, which determines how sharp the transition is between the passband and stopband.

## Practical Application: AM Modulation

One real-world application of the Butterworth filter is in **Amplitude Modulation (AM) used in radios**. In AM, the amplitude (or strength) of a carrier wave is varied in proportion to the signal (like music or voice) you want to transmit. A Butterworth filter can be used to extract the original signal components from the modulated carrier wave, providing a clean and accurate reproduction of the transmitted signal.

![image](https://github.com/user-attachments/assets/d83cae05-03d5-43d2-b435-d8f7459bf87b)


## Project Files

- `linear.py`: Contains the Python implementation of the Butterworth filter using a linear wave.
  
  ![image](https://github.com/user-attachments/assets/ca3130f9-c933-4f23-9b55-3a24461ac1df)

- `square.py`: Contains the Python implementation of the Butterworth filter using a square wave.
  
![image](https://github.com/user-attachments/assets/8c910e6c-6c4c-4c95-acba-9fde0c6843f7)
  
- `triangular.py`: Contains the Python implementation of the Butterworth filter using a triangular wave.
  
![image](https://github.com/user-attachments/assets/07dc0d29-a9c5-44ea-9da9-9a5450894350)
  
- `senoidal.py`: Contains the Python implementation of the Butterworth filter using a sin wave.
  
  ![image](https://github.com/user-attachments/assets/cc6d6804-842b-4976-b413-f4d45ce957a4)


## Getting Started

To use the Butterworth filter in your own projects, follow these steps:

1. **Clone the repository**:

   ````bash
   git clone https://github.com/Gabriel-Volpini/Butterworth.git

   ````

2. **Install the required dependencies**:

   ```bash
    pip install -r requirements.txt
   ```

3. **Run the example scripts to see the filter in action:**:
   ```bash
   python linear.py
   ```
