from numpy.core.numeric import NaN
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from figilyzer import Figilyzer

fa = Figilyzer()
#fa.loadRedis(host='dsihome.ru', port=6379)
#fa.saveFile('figis.json')
fa.loadFile('figis.json')
fa.normalize()

f = plt.figure(0)
plt.imshow(fa.genBitmap(), interpolation='nearest', cmap=cm.Greys_r)

f = plt.figure(1)
plt.imshow(fa.genAverageBitmap(), interpolation='nearest', cmap=cm.Greys_r)

f = plt.figure(2)
plt.imshow(fa.genSortBitmap(), interpolation='nearest', cmap=cm.Greys_r)

plt.show()

