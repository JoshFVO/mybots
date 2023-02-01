import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.passphysicsClient = p.connect(p.DIRECT)
        else:
            self.passphysicsClient = p.connect(p.GUI)
        self.world = WORLD(directOrGUI)
        self.robot = ROBOT(solutionID)

    def RUN(self):
        for t in range(250):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI":
                time.sleep(1/300)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


