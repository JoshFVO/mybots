import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time

passphysicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(100)

for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #print(i)
    time.sleep(1/60)


numpy.save('/Users/kaizoku-o-gumi/Desktop/CS 396 - Artificial Life/mybots/data/sensordata.npy', backLegSensorValues)

p.disconnect()
