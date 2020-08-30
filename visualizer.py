from matplotlib import pyplot as plt 
import numpy as np
from perceptron import Perceptron
import random
    

def setup():
    p1 = Perceptron()

    points_x = []
    points_y = []
    n = 100
    i = 0
    while i < n:
        a = random.randint(0, 30)
        b = random.randint(0, 30)
        points_x.append(a)
        points_y.append(b)
        i += 1

    x = np.arange(0, 30)
    y = x
    plt.plot(x, y)

    labels = []
    for x, y in zip(points_x, points_y):
        plt.scatter(x, y, color='blue' if x >= y else 'orange')

        labels.append(1 if x >= y else -1)

    for point_x, point_y, target in zip(points_x, points_y, labels):
        inputs = point_x, point_y
        p1.train(inputs, target)

        if p1.guess(inputs) != target:
            plt.annotate('', xy=(x,y), xytext=(0,0), color='red', textcoords='offset points')

    plt.show()

if __name__ == "__main__":
    setup()

    
