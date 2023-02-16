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

        sizeList = []

        for i in range(c.numOfLinks):
            randSize = random.random()
            sizeList.append(randSize)
            if i == 0:
                pyrosim.Send_Cube(name="0", pos=[0,0, 0.5] , size=[randSize,randSize,randSize])
                pyrosim.Send_Joint(name =  "0_1" , parent= "0" , child = "1" ,type = "revolute", position = [sizeList[0]/2, 0, 0.5], jointAxis= "0 0 1")
            elif i == 1:
                pyrosim.Send_Cube(name="1", pos=[randSize/2,0,0] , size=[randSize,randSize,randSize])
            else:
                pyrosim.Send_Joint(name = str(i - 1) + "_" + str(i) , parent= str(i - 1) , child = str(i) ,type = "revolute", position = [sizeList[i - 1], 0, 0], jointAxis= "0 0 1")
                pyrosim.Send_Cube(name=str(i), pos=[randSize/2,0,0] , size=[randSize,randSize,randSize])


        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        for i in range(c.numOfLinks):
            if c.senses[i] == 1:
                pyrosim.Send_Sensor_Neuron(name = i, linkName= str(i))
            if i > 0:
                pyrosim.Send_Motor_Neuron(name = c.numOfLinks + i , jointName = str(i-1) + "_" + str(i))



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