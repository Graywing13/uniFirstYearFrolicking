"""
a) F(v0) = - c[1]v[0] - c[2]v[0]
         = - 30v[0] - 15v[0]
            kgm/s^2    kg/s
b) F'(v) = - c[1] - 2c[2]v
"""

"""
Author: James Charbonneau
Date: 22 October 2019
Description: An Euler method simulation of a boat being pushed in water in
1 dimension. The force has both laminar and turbulent terms.
Input: nothing
Example running command: python L05_Q4.py
"""

# Import stuff for plotting  
import matplotlib.pyplot as plt

#Choose parameters for the problem
c_1 = 30 # laminar drag coefficient
c_2 = 15 # turbulent drag coefficient
m = 250 # mass of the object

#Choose initial conditions and time step for Euler method
t = 0
dt = 0.1
x = 0
v = 100
v_0 = v # Store the starting velocity for later


# Initialize lists for plotting
time = []
position = []
velocity = []


# perform Euler method
while v > 0.0001:
   time.append(t)
   position.append(x)
   velocity.append(v)

   v = v - (c_1*v + c_2 * v**2)/m*dt
   x = x + v*dt
   t = t + dt

# Print some interesting results from the simulation
print ("The boat travelled %0.2f metres in %0.2f seconds before it came to a stop." % (x , t))

# Plot the phase space
plt.plot(position, velocity ,"b.")
plt.title("Phase Diagram of Boat Problem")
plt.xlabel("position")
plt.ylabel("velocity")

# Plot the postition versus time graph

plt.plot(time, position, "b.")
plt.title("Position of boat pushed with initial velocity of %0.2f m/s" % (v_0))
plt.xlabel("Time (seconds)")
plt.ylabel("Distance Travelled (metres)")

plt.grid(True)
plt.show()