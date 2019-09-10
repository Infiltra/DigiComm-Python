#/usr/bin/env python3
#virgil
import numpy as np
import matplotlib.pyplot as plt

snr_db = np.linspace(0, 10, 100)
#print(snr_db)

snr_lin = 10**(snr_db/10)
#print(snr_lin)

#set bandwidth
B = np.linspace(10, 20*10**3, 10)
#print(B)
for band in B:
    C = band*np.log2(1+snr_lin)
    print(C)
    plt.plot(snr_db, C)
plt.xlabel('SNR(dB)')
plt.ylabel('Capacity')
plt.show()



