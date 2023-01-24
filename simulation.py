import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import time
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self):
        
        self.world = WORLD()
        self.robot = ROBOT()

    def RUN(self):
        for t in range(100):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(1/300)
            #print(t)

    def __del__(self):
        p.disconnect()


