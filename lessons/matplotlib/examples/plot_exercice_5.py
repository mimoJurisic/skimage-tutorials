"""
Exercise 5
===========

Exercise 5 with matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5), dpi=80)
ax = fig.add_subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S = np.sin(X)
C = np.cos(X)

ax.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
ax.plot(X, S, color="red", linewidth=2.5, linestyle="-")

ax.set_xlim(X.min() * 1.1, X.max() * 1.1)
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

ax.set_ylim(C.min() * 1.1, C.max() * 1.1)
ax.set_yticks([-1, 0, +1])

plt.show()
