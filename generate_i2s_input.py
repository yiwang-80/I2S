import numpy as np

# Parameters
sample_rate = 48000       # Hz
frequency = 1000          # Hz
bit_depth = 32            # bits
amplitude = 1           # normalized amplitude (0~1)
total_samples = 4096  # Number of samples to generate
duration = total_samples/sample_rate            # seconds

# Generate time axis
t = np.linspace(0, duration, int(total_samples), endpoint=False)

# Generate sine wave
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Convert to 32-bit signed integers
max_val = 2**(bit_depth - 1) - 1
int_wave = (sine_wave * max_val).astype(np.int32)

# Convert to 32-bit binary strings
binary_wave = ['0b'+format(np.uint32(x), '032b') for x in int_wave]

# Save to CSV
csv_path = "./dac_sine_1kHz_48kHz_32bit.csv"
with open(csv_path, 'w') as f:
    for line in binary_wave:
        f.write(line + '\n')
csv_path
