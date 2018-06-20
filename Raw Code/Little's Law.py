%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

process = np.random.randint(101, size=(1, 6)) # generate random process with 6 steps with times between 1-100 units time
# process = [18,59,30,21,78,10] # <- alternatively fill in your own process times

# define variables
T0 = np.amax(process)
rb = np.amax(process)/np.sum(process)
w0 = rb*T0
THw = 1/T0
maxw = int(w0*25)

# setup arrays for each line in the plot
wip =[] # WIP levels
THpwc =[] # practical worst case throughput
THw =[] # worst case throughput
THb = [] # best case throughput

# loop through our formulas and fill the arrays
for i in range(1,maxw):
    wip = np.append(wip, [i], axis=0)
    pwc = i/(w0+i-1)*rb
    THpwc = np.append(THpwc, [pwc], axis=0)
    worst = 1/T0
    THw = np.append(THw, [worst], axis=0)
    if i<w0:
        best = i/T0
    else:
        best = rb
    THb = np.append(THb, [best], axis=0)

# plot our results
plt.plot(wip, THpwc, marker='', color='blue', linewidth=2, label="TH PWC")
plt.plot(wip, THw, marker='', color='red', linewidth=2, label="TH Worst")
plt.plot(wip, THb, marker='', color='green', linewidth=2, linestyle='dashed', label="TH Best")
plt.legend()
plt.show()
