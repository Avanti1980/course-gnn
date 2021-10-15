import matplotlib.pyplot as plt
import numpy as np

n = 100

x = np.arange(-5, 5, 0.02)
sinc1 = np.sin(1 * x) / x
sinc2 = np.sin(5 * x) / x
sinc3 = np.sin(10 * x) / x

#plt.axis([-5.1, 5.1, -1.1, 1.1])

ax = plt.gca()

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.spines['bottom'].set_color('#586e75')

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.spines['left'].set_color('#586e75')

ax.xaxis.set_ticks_position('top')
ax.spines['top'].set_position(('data',0))
ax.spines['top'].set_color('#586e75')

ax.yaxis.set_ticks_position('right')
ax.spines['right'].set_position(('data',0))
ax.spines['right'].set_color('#586e75')

ax.tick_params(axis='x', colors='#586e75')
ax.tick_params(axis='y', colors='#586e75')

plt.plot(x, sinc1, color="#b58900", linestyle="-", linewidth=2, label=r'$\sin(x) / x$')
plt.plot(x, sinc2, color="#268bd2", linestyle="-", linewidth=2, label=r'$\sin(5x) / x$')
plt.plot(x, sinc3, color="#dc322f", linestyle="-", linewidth=2, label=r'$\sin(10x) / x$')

legend = plt.legend(loc='upper left', prop={'family':'EB Garamond', 'size':15})
plt.setp(legend.get_texts(), color='#586e75')

plt.savefig('sinc.svg', transparent=True)
