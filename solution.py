import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, nextAvailableID):

        self.weights = []
        self.myID = nextAvailableID

        for i in range(c.numSensorNeurons):
            row = []
            for j in range(c.numMotorNeurons):
                row.append(numpy.random.rand() * 2 - 1)
            self.weights.append(row)

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5, 5, 0.5] , size=[1,1,1])
        pyrosim.End()


    def Create_Body(self):

        #Head and Torso
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,2.75] , size=[0.3,1,1.5])
        pyrosim.Send_Joint(name = "Torso_Head" , parent= "Torso" , child = "Head" ,type = "revolute", position = [0,0,3.5], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="Head", pos=[0,0,0.25] , size=[0.5,0.5,0.5])

        #Upper Legs
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" ,type = "revolute", position = [0, 0.25 , 2], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0,0, -0.5] , size=[0.3, 0.3, 1.0])
        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" ,type = "revolute", position = [0,-0.25,2], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0,0,-0.5] , size=[0.3,0.3,1.0])

        #Lower Legs
        pyrosim.Send_Joint(name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" ,type = "revolute", position = [0,0,-1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.375] , size=[0.3,0.3,0.75])
        pyrosim.Send_Joint(name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" ,type = "revolute", position = [0,0,-1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.375] , size=[0.3,0.3,0.75])

        #Feet
        pyrosim.Send_Joint(name = "LowerRightLeg_RightFoot" , parent= "LowerRightLeg" , child = "RightFoot" ,type = "revolute", position = [0,0,-0.75], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightFoot", pos=[-0.1,0,-0.125] , size=[0.5,0.4,0.25])
        pyrosim.Send_Joint(name = "LowerLeftLeg_LeftFoot" , parent= "LowerLeftLeg" , child = "LeftFoot" ,type = "revolute", position = [0,0,-0.75], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftFoot", pos=[-0.1,0,-0.125] , size=[0.5,0.4,0.25])

        #Upper Arm
        pyrosim.Send_Joint(name = "Torso_RightArm" , parent= "Torso" , child = "RightArm" ,type = "revolute", position = [0, 0.5 , 3.25], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightArm", pos=[0, 0.15, -0.375] , size=[0.3, 0.3, 0.75])
        pyrosim.Send_Joint(name = "Torso_LeftArm" , parent= "Torso" , child = "LeftArm" ,type = "revolute", position = [0, -0.5, 3.25], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftArm", pos=[0, -0.15,-0.375] , size=[0.3, 0.3, 0.75])

        #Lower Arm
        pyrosim.Send_Joint(name = "RightArm_LowerRightArm" , parent= "RightArm" , child = "LowerRightArm" ,type = "revolute", position = [0, 0.150 , -0.75], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LowerRightArm", pos=[0, 0, -0.375] , size=[0.3, 0.3, 0.75])
        pyrosim.Send_Joint(name = "LeftArm_LowerLeftArm" , parent= "LeftArm" , child = "LowerLeftArm" ,type = "revolute", position = [0, -0.150, -0.75], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LowerLeftArm", pos=[0, 0,-0.375] , size=[0.3, 0.3, 0.75])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftFoot")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightFoot")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "RightLeg_LowerRightLeg")

        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightArm")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_LeftArm")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftArm_LowerLeftArm")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "RightArm_LowerRightArm")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "LowerRightLeg_RightFoot")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "LowerLeftLeg_LeftFoot")



        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def SET_ID(self, id):
        self.myID = id