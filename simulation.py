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
        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            time.sleep(1/60)

    def __del__(self):
        p.disconnect()


