import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        if self.jointName == 'Torso_FrontLeg':
            self.amplitude = numpy.pi/4.0
            self.frequency = 20.0
            self.phaseOffset = 0
        elif self.jointName == 'Torso_BackLeg':
            self.amplitude = numpy.pi/4.0
            self.frequency = 10.0
            self.phaseOffset = 0
        else:
            self.amplitude = numpy.pi/4.0
            self.frequency = 10.0
            self.phaseOffset = 0

        self.motorValues = numpy.linspace(0, 2 * numpy.pi, 1000)
        for i in range(1000):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * self.motorValues[i] + self.phaseOffset)

    def Set_Value(self, robotId, time):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[time], maxForce = 25)

