from ulab import numpy as np
from math import sqrt, log
import random



def normal(loc=0, scale=1, shape=None):
    #TODO: make random normal out of uniform
    return uniform(shape=shape)
    
def uniform(low=-1.0, high=1.0, shape=None):
    if shape == None:
        return random.uniform(low, high)
    uniform_setter = np.vectorize(lambda _: random.uniform(low, high))
    return uniform_setter(np.zeros(shape))

def square(x):
    square_setter = np.vectorize(lambda x: x * x)
    return square_setter(x)

def softmax(x, t=1.0, axis=-1):
    x_ = x / t
    x_max = np.max(x_, axis=axis, keepdims=True)
    exps = np.exp(x_ - x_max)
    return exps / np.sum(exps, axis=axis, keepdims=True)


def log_softmax(x, t=1.0, axis=-1):
    x_ = x / t
    x_max = np.max(x_, axis=axis, keepdims=True)
    exps = np.exp(x_ - x_max)
    exp_sum = np.sum(exps, axis=axis, keepdims=True)
    return x_ - x_max - np.log(exp_sum)

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))