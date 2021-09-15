import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)
beta = [0, 0.5, 1, 100]

swish0 = x / (1 + np.exp(- beta[0] * x))
swish1 = x / (1 + np.exp(- beta[1] * x))
swish2 = x / (1 + np.exp(- beta[2] * x))
swish3 = x / (1 + np.exp(- beta[3] * x))

gamma2 = 0.5
elu = np.maximum(0, x) + np.minimum(0, gamma2 * (np.exp(x) - 1))

plt.axis([-5.1, 5.1, -1.1, 5.1])

ax = plt.gca()

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['bottom'].set_color('#586e75')

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.spines['left'].set_color('#586e75')

ax.xaxis.set_ticks_position('top')
ax.spines['top'].set_position(('data', 0))
ax.spines['top'].set_color('#586e75')

ax.yaxis.set_ticks_position('right')
ax.spines['right'].set_position(('data', 0))
ax.spines['right'].set_color('#586e75')

ax.tick_params(axis='x', colors='#586e75')
ax.tick_params(axis='y', colors='#586e75')

plt.plot(x, swish0, color="#b58900", linestyle="-",
         linewidth=2, label=r'$\beta=0$')
plt.plot(x, swish1, color="#268bd2", linestyle="dashed",
         linewidth=2, label=r'$\beta=0.5$')
plt.plot(x, swish2, color="#dc322f", linestyle=":",
         linewidth=2, label=r'$\beta=1$')
plt.plot(x, swish3, color="#d33682", linestyle="-.",
         linewidth=2, label=r'$\beta=100$')

legend = plt.legend(loc='upper left', prop={'family': 'EB Garamond', 'size': 15})
plt.setp(legend.get_texts(), color='#586e75')

plt.savefig('Swish.svg', transparent=True)
