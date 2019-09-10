#/usr/bin/env python3
#virgil
import numpy as np
import matplotlib.pyplot as plt

snr_db = np.linspace(0, 10, 100)
#print(snr_db)

snr_lin = 10**(snr_db/10)
#print(snr_lin)

#set bandwidth
B = 200*10**3
#print(B)

C = B*np.log2(snr_lin + 1)
#print(C)
plt.figure()
plt.plot(snr_db, C)
plt.xlabel('SNR(dB)')
plt.ylabel('Capacity')
plt.show()
