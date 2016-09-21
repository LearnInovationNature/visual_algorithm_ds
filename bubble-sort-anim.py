import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#the array length that participate in sorting
data_len = 100 

#the indi and indj
indi = 0
indj = 0
times = data_len * (data_len + 1) / 2
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
    indi = 0
    indj = 0
    for indi in range(data_len):
        for indj in range(indi+1, data_len):
            if data[indi] < data[indj]:
                tmp = data[indi]
                data[indi] = data[indj]
                data[indj] = tmp
            if indi * data_len + indj >= num:
                break;
        if indi * data_len + indj >= num:
            break;
    for ind in range(data_len):
        rects[ind].set_height(data[ind])
#    print num, indi, indj, data
    return rects
# plot obj
fig1 = plt.figure()
rects = plt.bar(x, data, 0.9) 
plt.axis([0, data_len + 2, 0, 1.2])
line_ani = animation.FuncAnimation(fig1, update_line, times,  
                                   interval=1, blit=False)
#line_ani.save('lines.mp4')
plt.show()

