import numpy as np
from IPython.display import HTML
import matplotlib.pyplot as plt
from matplotlib import animation

# Setup the figure and axes...
fig, ax = plt.subplots(figsize=(8,8))

## Adjust axes limits according to your problem. Here we don't need more than a couple of meters left or right, and 600 meters up
ax.set(xlim=(-2, 2), ylim=(0, 600), xlabel='Position, meters', ylabel='Height, meters', title='Apple falling from CN tower')

# parameters of the problem
T = 10. #s
m = 0.3 #kg
g = 9.8 #m/s^2
v0x = -0 # Wind Speed m/s
H = 200. # The Initial Height m

# setting a timestep to be 50 ms
dt = 0.01 #s
N = int(T / dt)

# Allocating arrays for 2D problem
v = np.zeros((N+1, 2))
r = np.zeros((N+1, 2))
f = np.zeros((N+1, 2))

# initial conditions:
r[0] = np.array([0., H])
v[0] = np.array([-v0x, 0.])

#Effect of Weight
f[:] = np.array([0., -m * g])

## Run dynamics:
for n in range(N):
    v[n+1] = v[n] + f[n]/m * dt
    r[n+1] = r[n] + v[n+1] * dt

## drawing the first data point  
scat = ax.scatter(r[0,0], r[0,1], marker='o', c='g', s=200)

## animating 
def animate(i):
    scat.set_offsets(r[i])

ani = animation.FuncAnimation(fig, func=animate, frames=N)

## this function will create a lot of *.png files in a folder 'CNtower_frames'
ani.save('CNtower.html', writer=animation.HTMLWriter(fps= 1//dt))
plt.close()
#ani.save('CNtower.mp4', fps= 1//dt)

HTML('CNtower.html')
