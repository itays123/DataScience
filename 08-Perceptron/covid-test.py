# Using perceptron to determine covid test results
from perceptron import * # numpy and perceptron class

DATA_FILE = "covid.csv"

# load inputs and labels from file
def loadInputsLabels():
    data = np.loadtxt(DATA_FILE, delimiter=',', dtype=int)
    inputs = data[:,0:-1] # all columns except last one
    labels = data[:,-1] # last column
    return inputs, labels

inputs, labels = loadInputsLabels()
print("inputs = \n", inputs)
print("labels = ", labels)

# Create a trained perceptron
numOfInputs = inputs.shape[1]
perceptron = Perceptron(numOfInputs)
perceptron.train(inputs, labels)

# get symptoms from user
def loadUserSymptoms():
    lossOfSmell = int(input("Loss of smell (1=yes, 0=no) "))
    highBodyHeat = int(input("Body heat about 38 (1=yes, 0=no) "))
    runnyNose = int(input("Runny nose (1=yes, 0=no) "))
    bodyPain = int(input("Body pain (1=yes, 0=no) "))
    return lossOfSmell, highBodyHeat, runnyNose, bodyPain

shouldContinue = True
while shouldContinue:
    lossOfSmell, highBodyHeat, runnyNose, bodyPain = loadUserSymptoms()
    prediction = perceptron.predict(np.array([lossOfSmell, highBodyHeat, runnyNose, bodyPain]))
    if prediction:
        print("< Positive!!")
    else:
        print("< Negative!!")
    shouldContinue = int(input("Stop? (1=yes, 0=no) ")) == 0
