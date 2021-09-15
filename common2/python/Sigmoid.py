import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)
logistic = 1 / (1 + np.exp(-x))
tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

plt.axis([-5.1, 5.1, -1.1, 1.1])

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

plt.plot(x, logistic, color="#b58900", linestyle="-", linewidth=2, label="Logistic")
plt.plot(x, tanh, color="#268bd2", linestyle="dashed", linewidth=2, label="Tanh")

legend = plt.legend(loc='upper left', prop={'family':'EB Garamond', 'size':15})
plt.setp(legend.get_texts(), color='#586e75')

plt.savefig('Sigmoid.svg', transparent=True)
