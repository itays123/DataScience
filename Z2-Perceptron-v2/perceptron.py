# The perceptron class, by Yariv
import numpy as np

class Perceptron(object):
    def __init__(self, numOfInputs, epochs=200, learningRate=0.01):
        self.epochs = epochs
        self.learningRate = learningRate
        self.weights = np.zeros(numOfInputs)
        self.bios = 1
    def Activation(self, s):
        if s > 0:
            activation = 1
        else:
            activation = 0
        return activation
    def predict(self, inputs):
        sum = np.dot(inputs, self.weights) + self.bios
        out = self.Activation(sum)
        return out
    def train(self, inputs, labels):
        for _ in range(self.epochs):
            for i in range(len(inputs)):
                prd = self.predict(inputs[i])
                self.weights -= (prd - labels[i]) * inputs[i] * self.learningRate
                self.bios -= (prd - labels[i]) * self.learningRate