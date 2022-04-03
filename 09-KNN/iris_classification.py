# Classifies iris flowers by given attributes
from os import path
import numpy as np
from predict import predict # my own predict method
from sklearn.neighbors import KNeighborsClassifier
import sklearn.neural_network
from sklearn.metrics import confusion_matrix

DATA_FILE =  path.join(path.dirname(__file__), './iris_flowers.csv')
TEST_ROWS = 30 # out of 150
LABEL_COLUMN = -1 # last column

# Reads train inputs and labels, and test inputs and labels from a file
def readClassificationData():
    fileData = np.genfromtxt(DATA_FILE, delimiter=',')
    np.random.shuffle(fileData) # for more diverse train inputs
    trainInputs = fileData[:-TEST_ROWS,:LABEL_COLUMN] # all rows until test rows, all columns except labels
    trainLabels = fileData[:-TEST_ROWS, LABEL_COLUMN] # all rows until rest rows, label column
    testInputs = fileData[-TEST_ROWS:,:LABEL_COLUMN] # all test rows, all columns except labels
    testLabels = fileData[-TEST_ROWS:, LABEL_COLUMN] # all test rows, label column
    return trainInputs, trainLabels, testInputs, testLabels

def testUsingOwnMethod(trainInputs, trainLabels, testInputs, testLabels):
    print('Predicting using own method: ')
    for row, expected in zip(testInputs, testLabels):
        prediction = predict(row, trainInputs, trainLabels)
        print('Expected: ', expected, 'Prediction: ', prediction)

def testUsingKNeighborsClassifier(trainInputs, trainLabels, testInputs, testLabels):
    print('Predicting using KNeighbordClassifier: ')
    classifier = KNeighborsClassifier(n_neighbors = 5)
    classifier.fit(trainInputs, trainLabels)
    prediction = classifier.predict(testInputs)
    confusionMatrix= confusion_matrix(testLabels, prediction)
    print('Confusion matrix:\n' , confusionMatrix)

def testUsingMultiLayerPerceptron(trainInputs, trainLabels, testInputs, testLabels):
    print('Predicting using a neural network:')
    mlp = sklearn.neural_network.MLPClassifier(
        hidden_layer_sizes=(5),
        solver='sgd',
        learning_rate_init=0.01,
        max_iter=1000)
    mlp.fit(trainInputs, trainLabels)
    prediction = mlp.predict(testInputs)
    confusionMatrix= confusion_matrix(testLabels, prediction)
    print('Confusion matrix:\n' , confusionMatrix)

trainInputs, trainLabels, testInputs, testLabels = readClassificationData()
testUsingOwnMethod(trainInputs, trainLabels, testInputs, testLabels)
testUsingKNeighborsClassifier(trainInputs, trainLabels, testInputs, testLabels)
testUsingMultiLayerPerceptron(trainInputs, trainLabels, testInputs, testLabels)