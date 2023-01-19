import pybullet as p
import pybullet_data

class WORLD:

    def __init__(self):
        self.passphysicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")