import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 
def update_line(i,data,dx,line):
    data +=dx
    line.set_data(data)
    return line,
 
dx = np.random.rand(2, 500)
data = np.random.rand(2, 500)*-3
fig = plt.figure()
 
 
line, = plt.plot([], [], 'r*')
ax = fig.add_subplot(111)
#ax.set_axis_bgcolor(&amp;quot;white&amp;quot;)
 
plt.xlim(-3, 6)
plt.ylim(-3,6)
 
 
fig.suptitle('H a p p y    R a k h i', fontsize=20)
line_ani = animation.FuncAnimation(fig, update_line,fargs=(data,dx, line),
interval=100, blit=False)
plt.axis('off')
img = plt.imread("rakhi.jpg")
x = np.array([[1,2,1,4],[2,5,8,1],[0,1,2,2]])
plt.imshow(img,extent=[-x.shape[1]/2., x.shape[1]/2., -x.shape[0]/2., x.shape[0]/2. ])
plt.get_current_fig_manager().full_screen_toggle() # toggle fullscreen mode

plt.show()
