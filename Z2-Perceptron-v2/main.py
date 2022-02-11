# Using the LandSeaClassificationPerceptron
# Created by Itay Schechner
from landSeaPerceptron import LandSeaClassificationPerceptron

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

SEA_LABEL = 1
LAND_LABEL = 0

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

def main():      
    # craete perceptron
    perceptron = LandSeaClassificationPerceptron()
    perceptron.trainFromSources([seaSources, landSources], [SEA_LABEL, LAND_LABEL])

    # test it
    for source in testSources:
        prd = perceptron.predictFromSource(source)
        print("Source =", source, ",Prediction =", 'sea' if prd == SEA_LABEL else 'land')

main()