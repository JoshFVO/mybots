from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parent = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parent[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    
    def Evolve(self):
        self.Evaluate(self.parent)
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parent:
            self.children[key] = copy.deepcopy(self.parent[key])
            self.children[key].SET_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parent:
            if (self.parent[key].fitness > self.children[key].fitness):
                self.parent[key] = self.children[key]

    def Print(self):
        for key in self.parent:
            print("\n")
            print(self.parent[key].fitness, self.children[key].fitness)
            print("\n")

    def Show_Best(self):
        best_parent = self.parent[0]
        best_parent_fitness = 10000
        for key in self.parent:
            if self.parent[key].fitness < best_parent_fitness:
                best_parent_fitness = self.parent[key].fitness
                best_parent = self.parent[key]
        best_parent.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

