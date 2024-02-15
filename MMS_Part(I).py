#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Verifying a solution of the non-linear harmonic oscillator equation by
# establishing convergence to an exact solution.

import matplotlib.pyplot as plt
import numpy

k      = 1.0 # Spring constant
m      = 1.0 # Mass
cycles = 2.0 # No. of periods to integrate over
x0     = 1.0 # Initial displacement
v0     = 0.0 # Initial velocity
H      = 0.4 # Non-linear constant

def leapfrog( steps ):
    """Solve the simple harmonic motion equations for several oscillation cycles,
       assuming that the mass (m) and spring constant (k) are defined in the
       global space.
    """
    omega = (k/m)**0.5
    delta = 2.0*cycles*numpy.pi/omega/steps
    x     = numpy.empty( steps+1 )
    v     = numpy.empty( steps+1 )
    t     = numpy.empty( steps+1 )
    t[0]  = 0.0
    x[0]  = x0
    v[0]  = v0 + 0.5*delta*( (1+H*x[0])*x[0]*omega**2 - H*(omega*x[0]*numpy.cos(omega*t[0]))**2)
    for i in range(steps):
        t[i+1] = t[i] + delta
        v[i+1] = v[i] + delta*( - (1+H*x[i])*x[i]*omega**2 + H*numpy.square(omega*x0*numpy.cos(omega*t[i])))
        x[i+1] = x[i] + delta*v[i+1]
    return t, x, v

# Defining the Manufactured Solution
def manufactured_sol(t):
    omega = (k/m)**0.5
    return x0*numpy.cos(omega*t)

def l2_error_norm( t , x ):
    """Calculate the L2 relative error norm."""
    steps  = len( x ) - 1
    omega  = (k/m)**0.5
    l2_err = 0.0
    l2     = 0.0
    for i in range(steps):
        x_exact = manufactured_sol(t[i])
        l2_err += (x[i] - x_exact)**2.0
        l2     += x[i]**2.0
    return (l2_err/l2)**0.5


# The backend choice here may be platform dependent. You may need to
# change 'TkAgg' to something else.

plt.switch_backend( 'TkAgg' )

# This loop integrates the SHM equations repeatedly using an increasing
# number of steps (doubling at each loop iteration).
n        = 14
steps    = 8
l2_error = numpy.empty( n )
delta    = numpy.empty( n )
for i in range(0,n):
    t, x, v     = leapfrog( steps )
    x_exact     = manufactured_sol(t)
    delta[i]    = (k/m)**0.5*(t[1]-t[0])
    l2_error[i] = l2_error_norm( t , x )
    plt.plot( t , x )
    #plt.show( block=False )
    steps *= 2

# Switch to a new plotting window, and plot the L2 error norm,
# with guidelines for first, second, and third order accuracy.
plt.figure()
plt.loglog( delta , l2_error , 'o' )
plt.loglog( delta , l2_error[0]*(delta/delta[0])**1.0 )
plt.plot( delta , l2_error[0]*(delta/delta[0])**2.0 )
plt.loglog( delta , l2_error[0]*(delta/delta[0])**3.0 )
plt.show()


# In[ ]:




