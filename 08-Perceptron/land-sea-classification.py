# Classification between land and sea pictures
from PIL import Image
from perceptron import * # numpy and perceptron

# SECTION A - open image and calculate its average

# Open image as numpy RGB pixels array
def openImgAsNumpy(source):
    img = Image.open(source)
    img.load()
    return np.array(img, dtype=np.uint8)

# Calculate avergae RGB value in an image
RED_INDEX_RGB = 0
GREEN_INDEX_RGB = 1
BLUE_INDEX_RGB = 2
def calculateRGBAverage(npArr, index):
    values = npArr[:,:,index]
    return values.sum() / values.size

# Answer to question: The ocean images can contain some green values, 
# because the color of the ocean isn't rgb(0,0,255) but another combination of RGB values,
# where blue is the most dominant one but red and green can be present.

# source = "data/sea0.jpg"
# image = openImgAsNumpy(source)
# green = calculateRGBAverage(image, GREEN_INDEX_RGB)
# print("green average: ", green)

# SECTION B - build a list of green averages from sources

seaSources = [
    'data/sea0.jpg',
    'data/sea1.jpg',
    'data/sea2.jpg',
    'data/sea3.jpg',
    'data/sea4.jpg',
    'data/sea5.jpg',
    'data/sea6.jpg',
    'data/sea7.jpg',
    'data/sea8.jpg',
    'data/sea9.jpg'
]

landSources = [
    'data/land0.jpg',
    'data/land1.jpg',
    'data/land2.jpg',
    'data/land3.jpg',
    'data/land4.jpg',
    'data/land5.jpg',
    'data/land6.jpg',
    'data/land7.jpg',
    'data/land8.jpg',
    'data/land9.jpg'
]

# get an array of sources, and print a list of the corresponsing average RGB value in each picture
def buildRGBAverageList(sources, index):
    greenAverages = []
    for source in sources:
        image = openImgAsNumpy(source)
        greenAverages.append(calculateRGBAverage(image, index))
    return greenAverages

# seaGreenValues = buildRGBAverageList(seaSources, GREEN_INDEX_RGB)
# landGreenValues = buildRGBAverageList(landSources, GREEN_INDEX_RGB)
# print("sea list: \n", seaGreenValues)
# print("land list: \n", landGreenValues)


# SECTION C - display a graph of the differences between RGB values
import matplotlib.pyplot as plt

# Calculate and scatter points
def calculateAndScatterPoints(xAxisColor, yAxisColor):
    plt.title("Relations between colors")
    seaXvalues = buildRGBAverageList(seaSources, xAxisColor)
    seaYvalues = buildRGBAverageList(seaSources, yAxisColor)
    landXvalues = buildRGBAverageList(landSources, xAxisColor)
    landYvalues = buildRGBAverageList(landSources, yAxisColor)
    plt.scatter(seaXvalues, seaYvalues, color="b", marker="o")
    plt.scatter(landXvalues, landYvalues, color="r", marker="*")
    plt.show()

# calculateAndScatterPoints(RED_INDEX_RGB, GREEN_INDEX_RGB)
# calculateAndScatterPoints(RED_INDEX_RGB, BLUE_INDEX_RGB)
# calculateAndScatterPoints(GREEN_INDEX_RGB, BLUE_INDEX_RGB) # BEST ONE!!

# SECTION D - classify land and sea pictures

# Convert an np array to a tuple of (xAverage, yAverage)
X_AXIS_COLOR = GREEN_INDEX_RGB
Y_AXIS_COLOR = BLUE_INDEX_RGB
def imageToPoint(npArr):
    return calculateRGBAverage(npArr, X_AXIS_COLOR), calculateRGBAverage(npArr, Y_AXIS_COLOR)

# Build lists of inputs and labels from a list of sources
def buildInputsAndLabels(sources, label): 
    # build input list
    points = []
    for source in sources:
        image = openImgAsNumpy(source)
        points.append(imageToPoint(image))
    
    # build labels list
    labels = np.full(len(sources), label)
    return np.array(points), labels

# Create a perceptron and train it
def createTrainedPerceptron(): 
    seaInputs, seaLabels = buildInputsAndLabels(seaSources, 1)
    landInputs, landLabels = buildInputsAndLabels(landSources, 0)
    inputs = np.concatenate([seaInputs, landInputs])
    labels = np.concatenate([seaLabels, landLabels])  
    numOfInputs = inputs.shape[1] # 2
    print('inputs shape: ', inputs.shape)
    print ('inputs \n', inputs)
    print ('labels ', labels)
    perceptron = Perceptron(numOfInputs)
    perceptron.train(inputs, labels)
    return perceptron

perceptron = createTrainedPerceptron()
    
testSources = [
    'test/test0.jpg',
    'test/test1.jpg',
    'test/test2.jpg',
    'test/test3.jpg',
    'test/test4.jpg',
    'test/test5.jpg',
    'test/test6.jpg',
    'test/test7.jpg',
    'test/test8.jpg',
]

for source in testSources:
    image = openImgAsNumpy(source)
    xAvg, yAvg = imageToPoint(image)
    prd = perceptron.predict(np.array([xAvg, yAvg]))
    print("Source =", source, ",Prediction (0 -land, 1 - sea) =", prd)
