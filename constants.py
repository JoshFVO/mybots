import numpy
import random
import solution as s

amplitudeBl = numpy.pi/4.0
frequencyBl = 10.0
phaseOffsetBl = 0
amplitudeFl = numpy.pi/4.0
frequencyFl = 10.0
phaseOffsetFl = 0


numOfLinks = random.randint(5, 20)
senses = random.choices([-1,1], k=numOfLinks)


numberOfGenerations = 1
populationSize = 1
numSensorNeurons = 0
for i in senses:
    if i == 1:
        numSensorNeurons += 1
numMotorNeurons = numOfLinks - 1
motorJointRange = 0.5
