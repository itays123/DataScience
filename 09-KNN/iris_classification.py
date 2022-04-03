# Classifies iris flowers by given attributes
from os import path
import numpy as np
from predict import predict # my own predict method

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

K = 3

def testUsingOwnMethod(trainInputs, trainLabels, testInputs, testLabels):
    print('Predicting using own method: ')
    for row, expected in zip(testInputs, testLabels):
        print('Expected: ', expected, 'Prediction: ', predict(row, trainInputs, trainLabels, k=K))



trainInputs, trainLabels, testInputs, testLabels = readClassificationData();
testUsingOwnMethod(trainInputs, trainLabels, testInputs, testLabels)
