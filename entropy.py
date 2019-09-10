#usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#virgil
#length
L = 100

p_i = np.linspace(0.0, 1.0, L)
#p_1 = np.random.uniform(0.0, 1.0, L)
#compute inside sum
e1 = p_i*np.log(1/p_i)
#e2 = p_1*np.log(1/p_1)
plt.figure
plt.plot(p_i, e1)
#plt.plot(p_1, e2)
plt.show()
	


