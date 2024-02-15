#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy

k = 1.0  # Spring constant
m = 1.0  # Mass
cycles = 2.0  # No. of periods to integrate over
x0 = 1.0  # Initial displacement
v0 = 0.0  # Initial velocity
H = 0.5  # Non-linear constant

def leapfrog(steps):
    """Solve the simple harmonic motion equations for several oscillation cycles,
       assuming that the mass (m) and spring constant (k) are defined in the
       global space.
    """
    omega = (k / m) ** 0.5
    delta = 2.0 * cycles * numpy.pi / omega / steps
    x = numpy.empty(steps + 1)
    v = numpy.empty(steps + 1)
    t = numpy.empty(steps + 1)
    t[0] = 0.0
    x[0] = x0
    v[0] = v0 + 0.5 * delta * ((1 + H * x[0]) * x[0] * omega ** 2)
    for i in range(steps):
        t[i + 1] = t[i] + delta
        v[i + 1] = v[i] - delta * ((1 + H * x[i]) * x[i] * omega ** 2)
        x[i + 1] = x[i] + delta * v[i + 1]
    return t, x, v

# The backend choice here may be platform dependent. You may need to
# change 'TkAgg' to something else.

plt.switch_backend('TkAgg')

# This loop integrates the SHM equations repeatedly using an increasing
# number of steps (doubling at each loop iteration).
n = 1
steps1 = 30
steps2 = 60
delta1 = numpy.empty(n)
delta2 = numpy.empty(n)
for i in range(0, n):
    t1, x1, v1 = leapfrog(steps1)
    t2, x2, v2 = leapfrog(steps2)
    delta1[i] = (k / m) ** 0.5 * (t1[1] - t1[0])
    delta2[i] = (k / m) ** 0.5 * (t2[1] - t2[0])
    steps1 *= 2
    steps2 *= 2

# Create a common time array using linspace.
t_common = numpy.linspace(0, t1[-1], len(t1))

# Interpolate x1 and x2 onto the common time array.
x1_common = numpy.interp(t_common, t1, x1)
x2_common = numpy.interp(t_common, t2, x2)

# Plot the difference between x1_common and x2_common against the common time.
plt.plot(t1, x1)
plt.plot(t2, x2)
plt.figure()
plt.plot(x1, v1)
plt.figure()
plt.plot(x2, v2)
plt.figure()
plt.plot(t_common, x1_common - x2_common)
plt.xlabel('Time')
plt.ylabel('x1 - x2')
plt.show()


# In[ ]:




