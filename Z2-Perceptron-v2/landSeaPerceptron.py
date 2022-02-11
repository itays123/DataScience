# An extension to the perceptron class that works with string sources instead of numeric inputs
# Created by Itay Schechner

import string
from PIL import Image
from perceptron import * # perceptron and numpy

NUM_OF_INPUTS = 2
xAxisColor = 1 # green index in RGB
yAxisColor = 2 # blue index in RGB

# Open image as a numpy array
def openSourceAsNumpy(source: string):
    img = Image.open(source)
    img.load()
    return np.array(img, dtype=np.uint8)

# Get average RGB values of a picture matrix
def getAverageRGBValues(arr: np.ndarray):
    xValues = arr[:,:,xAxisColor]
    yValues = arr[:,:,yAxisColor]
    return xValues.sum() / xValues.size, yValues.sum() / yValues.size

class LandSeaClassificationPerceptron(Perceptron):
    def __init__(self):
        super().__init__(NUM_OF_INPUTS)
    
    # Get a list of sources and a matching label for each, and train the perceptron
    def trainFromSources(self, sources, label_list):
        inputs = []
        labels = []
        for sourceList, label in zip(sources, label_list):
            for source in sourceList:
                image = openSourceAsNumpy(source)
                xAvg, yAvg = getAverageRGBValues(image)
                inputs.append((xAvg, yAvg))
                labels.append(label)
        
        self.train(np.array(inputs), np.array(labels))
    
    def predictFromSource(self, source):
        image = openSourceAsNumpy(source)
        xAvg, yAvg = getAverageRGBValues(image)
        return super().predict(np.array([xAvg, yAvg]))