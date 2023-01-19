import pybullet as p
import random
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time

amplitudeBl = numpy.pi/4.0
frequencyBl = 10.0
phaseOffsetBl = 0
amplitudeFl = numpy.pi/4.0
frequencyFl = 10.0
phaseOffsetFl = 0

passphysicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAnglesBl = numpy.linspace(0, 2 * numpy.pi, 1000)
targetAnglesFl = numpy.linspace(0, 2 * numpy.pi, 1000)
for i in range(1000):
    targetAnglesBl[i] = amplitudeBl * numpy.sin(frequencyBl * targetAnglesBl[i] + phaseOffsetBl)
    targetAnglesFl[i] = amplitudeFl * numpy.sin(frequencyFl * targetAnglesFl[i] + phaseOffsetFl)

#numpy.save('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/sinusoidalValuesBl.npy', targetAnglesBl)
#numpy.save('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/sinusoidalValuesFl.npy', targetAnglesFl)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBl[i], maxForce = 25)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFl[i], maxForce = 25)
    time.sleep(1/480)


numpy.save('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/frontLegSensorValues.npy', frontLegSensorValues)

p.disconnect()
