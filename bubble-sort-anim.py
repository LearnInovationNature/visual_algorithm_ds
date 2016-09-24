import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#the array length that participate in sorting
data_len = 30 

#the indi and indj
indi = 0
indj = 0
times = data_len * data_len + 100
#the data source

data = np.random.rand(data_len)  
#gen the x axis marks
x = np.linspace(0, 100, data_len)

x = np.arange(data_len)
rects = None
#update function, called for many times
def update_line(num):
    global data_len 
    global data
    global rects
    global indi
    global indj
    if indi == data_len:
        return rects
    if indj == 0:
        indj += 1
    if indj == data_len:
        indj = indi + 1
        indi += 1
    if indi * data_len + indj >= num:
        return rects
    if data[indi] < data[indj]:
        tmp = data[indi]
        data[indi] = data[indj]
        data[indj] = tmp
        for ind in range(data_len):
            rects[ind].set_height(data[ind])
    indj += 1
    print num, indi, indj
    return rects
# plot obj
fig1 = plt.figure()
rects = plt.bar(x, data, 0.9) 
plt.axis([0, data_len + 2, 0, 1.2])
line_ani = animation.FuncAnimation(fig1, update_line, times,  
                                   interval=1, blit=False)
#line_ani.save('lines.mp4')
plt.show()

