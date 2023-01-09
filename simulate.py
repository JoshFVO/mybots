import pybullet as p
import time

passphysicsClient = p.connect(p.GUI)

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/6000)
    print(i)

p.disconnect()
