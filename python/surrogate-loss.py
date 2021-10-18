import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.02)

loss01 = [(1-np.sign(xi))/2 for xi in x]
hinge = np.maximum(0, 1-x)
square_hinge = np.maximum(0, 1-x)**2
exp = np.exp(-x)
logistic = np.log2(1 + np.exp(-x))


with plt.style.context('Solarize_Light2'):
    
    plt.axis([-5.1, 5.1, -1.1, 5.1])

    ax = plt.gca()

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    #ax.spines['bottom'].set_color('#586e75')

    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    #ax.spines['left'].set_color('#586e75')

    ax.xaxis.set_ticks_position('top')
    ax.spines['top'].set_position(('data', 0))
    ax.spines['top'].set_color('#586e75')

    ax.yaxis.set_ticks_position('right')
    ax.spines['right'].set_position(('data', 0))
    ax.spines['right'].set_color('#586e75')

    ax.tick_params(axis='x')
    ax.tick_params(axis='y')

    plt.plot(x, loss01, linestyle="solid", linewidth=2, label="0-1 loss")
    plt.plot(x, hinge, linestyle="-", linewidth=2, label="hinge")
    plt.plot(x, square_hinge, linestyle="dashed", linewidth=2, label="square hinge")
    plt.plot(x, exp, linestyle=":", linewidth=2, label="exp")
    plt.plot(x, logistic, linestyle="-.", linewidth=2, label="logistic")

    legend = plt.legend(loc='upper right', prop={'family': 'EB Garamond', 'size': 15})
    plt.setp(legend.get_texts(), color='#586e75')

    plt.xlabel(r'$y f(x)$', loc='right')

plt.savefig('surrogate-loss.svg', transparent=True)
plt.show()
