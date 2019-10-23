import math
import random
def sigmoid(x):
    t = ((1)/(1 + math.exp(x)))
    return t
def scalar(x,y):
    s = x[1]*y[1] + x[2]*y[2]
    return s
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
 
    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения 
        # и последующее использование функции активации
        total = scalar(self.weights, intputs) + self.bias
        return sigmoid(total)
 

weights = [0, 1]  # w1 = 0, w2 = 1
bias = 4  # b = 4
n = Neuron(weights, bias)
 
x = [2, 3]  # x1 = 2, x2 = 3
print(n.feedforward(x))  # 0.9990889488055994
