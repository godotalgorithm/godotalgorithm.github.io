# analysis of a simple investment strategy on historical stock market data

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

date, cpi, val = np.loadtxt('sp500.dat', unpack=True)

# normalize stock market values for convenience
val /= 90.0
val0 = 1.32*np.exp(0.06395*(date - 1871))

ratio = np.arange(0.3, 2.1, 0.05)
strategy = [1.0] * len(ratio)
interval = [(0.0,1.0)] * len(ratio)

# forward simulation of investment strategy
def invest(strategy):
    worth = 1.0
    i=1
    while i < len(val):
        ratio0 = val[i-1]/val0[i-1]
        strategy0 = np.interp(ratio0, ratio, strategy)
        worth = worth*(1.0 - strategy0) + worth*strategy0*val[i]/val[i-1]
        i = i+1
    return -worth

def invest_plot(strategy):
    worth = [1.0]*len(val)
    i=1
    while i < len(val):
        ratio0 = val[i-1]/val0[i-1]
        strategy0 = np.interp(ratio0, ratio, strategy)
        worth[i] = worth[i-1]*(1.0 - strategy0) + worth[i-1]*strategy0*val[i]/val[i-1]
        i = i+1
    return worth

invest0 = invest(strategy)

scan0 = invest_plot(strategy)
res = opt.minimize(invest,strategy,bounds=interval)

optimal_strategy = res.x
scan = invest_plot(optimal_strategy)

safe_strategy = [1.0] * len(ratio)
for (i,strat) in enumerate(safe_strategy):
    if(ratio[i] > 1.5):
        strat = 0.0
scan2 = invest_plot(safe_strategy)

fig, (ax1,ax2) = plt.subplots(2,1,tight_layout=True, figsize=(6.0,6.0))

ax1.plot(ratio,optimal_strategy,color='blue')
ax1.set_xlabel('value of risk asset relative to baseline')
ax1.set_ylabel('allocation')

ax2.semilogy(date,val0,color='black')
ax2.semilogy(date,scan0,color='red')
ax2.semilogy(date,scan,color='blue')
#ax2.semilogy(date,scan2,color='green')

ax2.set_xlabel('year')
ax2.set_ylabel('worth')

plt.savefig('invest.pdf', bbox_inches='tight', pad_inches=0.01)