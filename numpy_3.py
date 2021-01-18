import numpy as np

V1 = 20000
V0 = 20

dB = 20*np.log10(V1/20)

print(dB)

dB = 20*np.log10(200/20)     #30dB

dB = 20*np.log10(6325/20)    #50dB

print(6325/200)               #31.625倍
