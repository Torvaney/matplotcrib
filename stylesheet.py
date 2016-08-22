
# coding: utf-8

# # Matplotlib cribsheet
# With stylesheet

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

plt.style.use('~/matplotcrib/style_plain.mplstyle')


# Some useful links:
# * Full colours list: http://matplotlib.org/mpl_examples/color/named_colors.hires.png
# * Linestyles shown here: http://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle

# In[2]:

# Generate some data to use
n = 50  # number of data points

x = np.random.rand(n)  # random x co-ordinates
y = 5*x + np.random.randn(n)  # y as a function of x with some added noise
z = [chr(i) for i in np.random.randint(97, 97+9, n)]  # sample text labels

coords = pd.DataFrame({'x': x, 'y': y, 'z': z})


# In[3]:

# Simple scatter plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=1, color='black', s=10)

# Add title
fig.suptitle('title')
# Add axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')


# In[ ]:



