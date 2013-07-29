import pyaudio
import wave
import numpy as np
import time


import matplotlib
matplotlib.use('WXAgg')
matplotlib.interactive(True)
import matplotlib.pyplot as plt

plt.ion()




# http://www.swharden.com/blog/2010-06-23-insights-into-ffts-imaginary-numbers-and-accurate-spectrographs/

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

CHUNK = 2**10

print "Frame duration:", CHUNK/(RATE+0.0)*1000 

window = np.hamming(CHUNK)


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

time.sleep(1)

print("* done recording")




fig = plt.figure()
ax = fig.add_subplot(2,1,1)
[t] = ax.plot(np.array(range(CHUNK)*2**16)-2**15)
plt.show()

for i in range(1):
	data = stream.read(CHUNK)
	stream.stop_stream()
	signal = np.fromstring(data, 'Int16')
	t.set_ydata(signal)
	#draw()
	plt.pause(1)


stream.close()
p.terminate()

plt.ioff()
