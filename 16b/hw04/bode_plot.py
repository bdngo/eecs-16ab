from scipy import signal
import matplotlib.pyplot as plt

r_l = 66
r_h = 1600
c_l, c_h = 1e-6, 1e-6

twof = signal.TransferFunction([1], [0.001, 1])
threec = signal.TransferFunction([r_h * c_h, 0], [r_l * r_h * c_l * c_h, r_l * c_l + r_h * c_h, 1])

w, mag, phase = signal.bode(twof)
w2, mag2, phase2 = signal.bode(threec)

plt.figure()
plt.semilogx(w, mag)
plt.title('Frequency vs. Magnitude')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')

plt.figure()
plt.semilogx(w, phase)
plt.title('Frequency vs. Phase')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [deg]')

plt.figure()
plt.semilogx(w2, mag2)
plt.xlim(1e-1, 1e+9)
plt.title('Frequency vs. Magnitude')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')

plt.figure()
plt.semilogx(w2, phase2)
plt.xlim(1e-1, 1e+9)
plt.title('Frequency vs. Phase')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [deg]')
plt.show()
