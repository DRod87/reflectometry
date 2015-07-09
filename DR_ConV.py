import matplotlib.pyplot as plt  # import the necessary graphing functions
import numpy as np               # import numerical python

x = np.linspace(0, 2*np.pi, 301)    # create my array with 300 elements

_x = np.fft.fftshift(np.fft.fftfreq(x.size, x[1] - x[0]))  # my
                                                        #frequency domain


y = np.zeros(301, dtype = np.complex)                # create a delta function
y[3] = 1                       # insert a 1 to create a spike in our array


_y = np.fft.fftshift(np.fft.fft(y))   # create my sine function by taking 
                                            # the FFT of the delta function


plt.figure(1)
plt.plot(_x, _y, 'b')               # plot the figure to view the sine wave
plt.title('The Delta Function')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

N = 301
b = np.arange(N)
b[150:] = b[150::-1]            # create the triangle using splice commands
b[100:200] = b[100:200:100]     # create the band pass signal

plt.figure(2)
plt.plot(b, 'b')                # plot the band pass signal

C = b*_y                        # multiple the bandpass signal by the sine wave
_C = np.fft.ifftshift(C)        # take the inverse to convolve the two
                                # signals (sine and bandpass)
            

plt.figure(3)                   # plot the multiplication of the Fourier
plt.plot(C,'r',_C,'g')          # and compare it to the inverse Fourier
plt.xlabel('Frequency')
plt.ylabel('Signal Range')
plt.show()




