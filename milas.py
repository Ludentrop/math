import matplotlib.pyplot as plt
from samila import GenerativeImage
import random
import math
from samila import Projection


def f1(x, y):
    result = random.gauss(0, 1) * math.sin(y) + (y + x) * random.uniform(-1, 1)
    return result


def f2(x, y):
    result = random.uniform(-1, 1) * y * x + math.cos(x**2) + random.gauss(0, 1)
    return result


g = GenerativeImage(f1, f2)
g.generate(seed=300)
g.plot(color='blue', bgcolor='black', projection=Projection.POLAR)
plt.show()
