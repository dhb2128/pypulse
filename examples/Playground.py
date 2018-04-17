import scipy.signal as sps
import matplotlib.pyplot as plt
import numpy as np
import pypulse.PulseGeneration as pg
import pypulse.PulseInterface as pi

sampling_rate = 20000
duration = 2
hz = 2

# pulse_times = np.linspace(0, duration, duration*hz, endpoint=False)
pulse_times = [0.0, 0.4, 0.6, 1.75]
pulse_length = (1.0 / hz) / 2.0
print(pulse_times)

default_params = {'type': 'ContCorr',
                  'frequency': hz,
                  'pulse_length': pulse_length,
                  'pulse_times': pulse_times,
                  'onset': 0.0,
                  'offset': 0.1,
                  'target_duty': 0.5,
                  'amp_min': 0.0,
                  'amp_max': 1.0,
                  'shatter_frequency': 500.0,
                  'invert': False,
                  'reverse': False}

inverse_params = {'type': 'ContCorr',
                  'frequency': hz,
                  'pulse_length': pulse_length,
                  'pulse_times': pulse_times,
                  'onset': 0.0,
                  'offset': 0.1,
                  'target_duty': 0.5,
                  'amp_min': 0.0,
                  'amp_max': 1.0,
                  'shatter_frequency': 500.0,
                  'invert': True,
                  'reverse': False}

params = [default_params, inverse_params]

pulses, t = pi.make_pulse(sampling_rate, 0.0, 0.0, params)

plt.plot(t, pulses[0])
plt.plot(t, pulses[1])
# plt.xlim((0, duration))
plt.show()


params = {'fromLength': True, 'fromRepeats': False,
          'frequency': 20, 'repeats': 5, 'seed': 1, 'amp_min': 0.1,
          'amp_max': 0.9, 'shatter_frequency': 500, 'length': 1,
          'onset': 0.1, 'offset': 0.1}

pulse, t = pg.dummy_noise_pulse(10000, params)

plt.plot(t, pulse)
plt.show()

# Testing - random shatter
pulse, t = pg.random_shatter_pulse(20000.0, 2.0, 5.0, 0.5, 200.0, 1.0, 0.1, 0.9)
print(sum(pulse) / len(pulse))
plt.plot(t, pulse)
plt.xlim((-0.1, 2.1))
plt.ylim((-0.1, 1.1))
plt.show()
