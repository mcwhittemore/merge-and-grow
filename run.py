from scipy import misc
import numpy as np
import sys

savePath = sys.argv[1]
imgPaths = sys.argv[2:]

print savePath
print len(imgPaths)

def toLuminance(r, g, b):
    rc = 0.2126
    gc = 0.7152
    bc = 0.0722
    return (r * rc) + (g * gc) + (b * bc)

imgs = []

for imgPath in imgPaths:
    imgs.append(misc.imread(imgPath))

color = np.empty([640, 640, 3])

size = xrange(640)

numImgs = len(imgs)

print "staring color"

for x in size:
    for y in size:
        red = 0
        green = 0
        blue = 0
        for img in imgs:
            red += img[x, y, 0]
            green += img[x, y, 1]
            blue += img[x, y, 2]

        color[x, y, 0] = red/numImgs
        color[x, y, 1] = green/numImgs
        color[x, y, 2] = blue/numImgs

luminance = np.empty([640*5, 640*5])
out = np.empty([640*5, 640*5, 3])

for x in size:
    for y in size:
        data = np.zeros([25, 2])
        pos = 0
        for img in imgs:
            data[pos*2, 0] += 1
            data[pos*2, 1] = toLuminance(img[x, y, 0], img[x, y, 1], img[x, y, 2])
            pos = pos +1
            if pos == 13:
                pos = 0

        for p in range(12):
            left = (p*2)
            center = left + 1
            right = center + 1
            data[center, 0] = int( (data[left, 0] + data[right, 0]) / 2)
            data[center, 1] = int( (data[left, 1] + data[right, 1]) / 2)

        bigX = x*5
        bigY = y*5

        for mx in range(5):
            for my in range(5):
                idx = (mx*5) + my
                light = data[idx, 1] / data[idx, 0]
                luminance[bigX+mx, bigY+my] = light
                for c in range(3):
                    out[bigX+mx, bigY+my, c] = (light / 255) * color[x, y, c]

misc.imsave(savePath, out)
