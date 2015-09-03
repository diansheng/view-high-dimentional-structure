import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)
fig.set_figheight(2)
fig.set_figheight(4)
ax1.set_xlim(-2,2); ax1.set_ylim(-2,2);
ax1.set_aspect('equal');
#ax2.set_xlim(-2,2); ax2.set_ylim(-2,2);
ax2.set_aspect('equal')

linespace = np.arange(-2, 2, 0.01)        # x-array
line1, = ax1.plot([], [],lw=2)
line2, = ax2.plot([], [],lw=2)
patch =plt.Circle((0,-1),1,fc='y')
ax2.add_patch(patch)

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

def animate(i):# i is lamda, representing the distance of movement
    x=linespace-i*d[0]
    y=g(x)-i*d[1]
    x,y=f(x,y)
    x=x+i*d[0]
    y=y+i*d[1]
    line1.set_data(x,y)  # update the data
    line2.set_data(x,y)  # update the data
    patch.center=(0,i-1)
    return patch,

#Init only required for blitting to give a clean slate.
def init():
    line1.set_data([],[])
    line2.set_data([],[])
    patch.center=(0,-1)
    return patch,

ani = animation.FuncAnimation(fig, animate, np.arange(0,2, 0.01), init_func=init, \
    interval=25, blit=False)

Writer = animation.writers['ffmpeg']
writer =Writer(fps=30,metadata=dict(artist='diansheng'), bitrate=1800)
ani.save('view2Din1D.mp4',writer=writer)
#ani.save('view2Din1D.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()