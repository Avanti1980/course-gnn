import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)
gamma = 0.2
relu = np.maximum(0, x)
lrelu = np.maximum(0, x) + gamma * np.minimum(0, x)
softplus = np.log(1 + np.exp(x))

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

plt.plot(x, relu, color="#b58900", linestyle="-", linewidth=2, label="ReLU")
plt.plot(x, lrelu, color="#268bd2", linestyle="dashed", linewidth=2, label="LeakyReLU")
plt.plot(x, elu, color="#dc322f", linestyle=":", linewidth=2, label="ELU")
plt.plot(x, softplus, color="#d33682", linestyle="-.", linewidth=2, label="Softplus")

legend = plt.legend(loc='upper left', prop={'family': 'EB Garamond', 'size': 15})
plt.setp(legend.get_texts(), color='#586e75')

plt.savefig('ReLU.svg', transparent=True)
plt.show()
