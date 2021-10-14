import numpy as np
import matplotlib.pyplot as plt

m = 20
w0_true = 2
w1_true = 0.5
x = np.linspace(-1, 1, m)
y = w0_true + w1_true * x

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0].scatter(x, y, marker='x', s=40, color='k')


def cost_func(w0, w1):
    w0 = np.atleast_3d(np.asarray(w0))
    w1 = np.atleast_3d(np.asarray(w1))
    return np.average((y-hypothesis(x, w0, w1))**2, axis=2)/2


def hypothesis(x, w0, w1):
    return w0 + w1*x


# First construct a grid of (w0, w1) parameter pairs and their corresponding cost function values.
w0_grid = np.linspace(-1, 4, 101)
w1_grid = np.linspace(-5, 5, 101)
J_grid = cost_func(w0_grid[np.newaxis, :, np.newaxis],
                   w1_grid[:, np.newaxis, np.newaxis])

# A labeled contour plot for the RHS cost function
X, Y = np.meshgrid(w0_grid, w1_grid)
contours = ax[1].contour(X, Y, J_grid, 30)
ax[1].clabel(contours)
# The target parameter values indicated on the cost function contour plot
ax[1].scatter([w0_true]*2, [w1_true]*2, s=[50, 10], color=['k', 'w'])

# Take N steps with learning rate alpha down the steepest gradient, starting at (w0, w1) = (0, 0).
N = 5
alpha = 0.7
theta = [np.array((0, 0))]
J = [cost_func(*theta[0])[0]]
for j in range(N-1):
    last_theta = theta[-1]
    this_theta = np.empty((2,))
    this_theta[0] = last_theta[0] - alpha / m * np.sum((hypothesis(x, *last_theta) - y))
    this_theta[1] = last_theta[1] - alpha / m * np.sum((hypothesis(x, *last_theta) - y) * x)
    theta.append(this_theta)
    J.append(cost_func(*this_theta))


# Annotate the cost function plot with coloured points indicating the
# parameters chosen and red arrows indicating the steps down the gradient.
# Also plot the fit function on the LHS data plot in a matching colour.
colors = ['#dc322f', '#859900', '#268bd2', '#d33682', '#cb4b16']
ax[0].plot(x, hypothesis(x, *theta[0]), color=colors[0], lw=2, label=r'$w_0 = {:.3f}, w_1 = {:.3f}$'.format(*theta[0]))
for j in range(1, N):
    ax[1].annotate('', xy=theta[j], xytext=theta[j-1],
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
    ax[0].plot(x, hypothesis(x, *theta[j]), color=colors[j], lw=2,
               label=r'$w_0 = {:.3f}, w_1 = {:.3f}$'.format(*theta[j]))
ax[1].scatter(*zip(*theta), c=colors, s=40, lw=0)

# Labels, titles and a legend.
ax[1].set_xlabel(r'$w_0$')
ax[1].set_ylabel(r'$w_1$')
# ax[1].set_title('Cost function')
ax[0].set_xlabel(r'$x$')
ax[0].set_ylabel(r'$y$')
# ax[0].set_title('Data and fit')
axbox = ax[0].get_position()
# Position the legend by hand so that it doesn't cover up any of the lines.
ax[0].legend(loc=(axbox.x0+0.5*axbox.width, axbox.y0+0.1*axbox.height), fontsize='small')

plt.savefig('gradient-descent.svg', transparent=True)
plt.show()
