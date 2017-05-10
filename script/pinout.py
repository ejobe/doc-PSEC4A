import matplotlib as mpl
mpl.use('Qt4Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv

NUM_PINS = 128
CORNER_PINS = [1,32,64,96]
FILENAME='../PSEC4A_package_pinout.txt' #csv file

pinout=[]
with open(FILENAME, 'rb') as csvfile:
    _pinout = csv.reader(csvfile, delimiter=',')
    for row in _pinout:
        pinout.append(row)


fig, ax = plt.subplots(1,figsize=(15,15))

for i in range(1,NUM_PINS+1):

    if i > CORNER_PINS[3]:
        yoffset = 32.5
        ax.add_patch(patches.Rectangle((31-i%32,yoffset), 0.6,1.2,lw=1,edgecolor='black',
                                       facecolor='none'))
        ax.text(31-(i-1)%32,yoffset+1.5, pinout[i-1][2], rotation=90, va='bottom', size=16)
        ax.text(31-(i-1)%32+0.3,yoffset-0.7, pinout[i-1][0], ha='center', size=9)

    elif i > CORNER_PINS[2]:
        xoffset=32
        ax.add_patch(patches.Rectangle((xoffset,i%32), 1.2,0.6,lw=1,edgecolor='black',
                                       facecolor='none'))
        ax.text(xoffset+1.5, (i-1)%32, pinout[i-1][2], ha='left', size=16)
        ax.text(xoffset-0.5, (i-1)%32+0.1, pinout[i-1][0], ha='center', size=9)

    elif i > CORNER_PINS[1]:
        yoffset=-2
        ax.add_patch(patches.Rectangle((i%32,yoffset), 0.6,1.2,lw=1,edgecolor='black',
                                       facecolor='none'))
        ax.text((i-1)%32, yoffset-0.5, pinout[i-1][2], rotation=90, va='top', size=16)
        ax.text((i-1)%32+0.3,yoffset+1.4, pinout[i-1][0], ha='center', size=9)

                
    else:
        xoffset=-1.5
        ax.add_patch(patches.Rectangle((xoffset,31-i%32), 1.2,0.6,lw=1,edgecolor='black',
                                    facecolor='none'))
        ax.text(xoffset-0.5, 31-(i-1)%32, pinout[i-1][2], ha='right', size=16)
        ax.text(xoffset+1.4, 31-(i-1)%32+0.1, pinout[i-1][0], ha='left', size=9)


ax.text(16,16,'PSEC4A pinout', size=36, ha='center')
ax.text(16,14.5,'v1  2017.4.10', size=16, ha='center')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.axis('off')
plt.ylim([-3,37.6])
plt.xlim([-3,37.6])
plt.show()
