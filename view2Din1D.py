import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig, (ax1,ax2) = plt.subplots(1,2)
ax1.set_xlim(-2,2); ax1.set_ylim(-2,2)

linespace = np.arange(-2, 2, 0.01)        # x-array
line, = ax1.plot([], [],lw=2)

# shape function
def f(x,y):
    #x^2+y^2<=1
    index=[x*x+(y+1)*(y+1)<1]
    return x[index],y[index]

# line function
def g(x):
    #y=0
    y=0*x
    return y

#direction vector
d=(0,1)

def animate(i):# i is lamda, notating the distance of movement
    x=linespace-i*d[0]
    y=g(x)-i*d[1]
    x,y=f(x,y)
    x=x+i*d[0]
    y=y+i*d[1]
    line.set_data(x,y)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_data([],[])
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0,2, 0.01), init_func=init, \
    interval=25, blit=False)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()