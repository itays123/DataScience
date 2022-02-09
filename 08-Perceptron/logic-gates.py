# Using perceptron for logic gates
from perceptron import * # numpy and perceptron

inputs = np.array([[0,0],[1,0],[0,1],[1,1]])
labels = np.array([0,0,0,1]) # Labels for AND gate
#labels = np.array([0,1,1,1]) # Labels for OR gate
#labels = np.array([1,0,0,0]) # Labels for NOR gate
#labels = np.array([0,1,1,0]) # Labels for XOR gate

numOfInputs = inputs.shape[1]  # =2
print('inputs shape: ', inputs.shape)
print ('inputs \n', inputs)
print ('labels ', labels)
perceptron = Perceptron(numOfInputs)
perceptron.train(inputs, labels)

expected_labels = []
for input in inputs:
    expected_labels.append(perceptron.predict(input))

print("expected = " ,expected_labels)