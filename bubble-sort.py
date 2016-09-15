
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as text

#the array length that participate in sorting
data_len = 10 
data = np.random.rand(data_len)  
#gen the x axis marks
x = np.linspace(0, 100, data_len)

ch_input = ''
x = np.arange(data_len)
rect = None

for i in range(data_len):
    if ch_input == 'q':
        break;
    for j in range(i+1, data_len):
        bar_color = []
        for i1 in range(data_len):
            bar_color.append('g')
        if data[i] < data[j]:
            swp = data[j]
            data[j] = data[i]
            data[i] = swp
            bar_color[i] = bar_color[j] = 'r'
        ch_input = raw_input('input your choice: q for quit, n for next step:')
        ch_input = ch_input.strip()
        if ch_input == 'n':
            if rect:
                rect.remove()
            rect = plt.bar(x, data, 0.9, color = bar_color)
            plt.axis([0, data_len + 2, 0, 1.2])
            plt.show(block=False)
        text.Annotation('hello', (3, 1.0))
        if ch_input == 'q':
            break;
while True:
    ch_input = raw_input('algorithm is done, press q to quit:')
    if ch_input == 'q':
        break;
    
