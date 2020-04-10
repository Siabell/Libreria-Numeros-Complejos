import unittest
import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import QuantumMath as qm 


class ObservableAndMeasuringTest(unittest.TestCase):
    
    def testExercise431(self):
        print("--- Exercise 4.3.1")
        mState =  matrix.complexMatrix([[(0,0),(1,0)],[(1,0),(0,0)]])
        eigenVectors = mState.eigenVectors()
        print("The eigen Vectors")
        for i in range(2):
            eigenVectors[i].show()
            print("")
            


    def testExercise441(self):
        print("\n--- Exercise 4.4.1")
        u1 =  matrix.complexMatrix([[(0,0),(1,0)],[(1,0),(0,0)]])
        u2 = matrix.complexMatrix([[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],[(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]])
        u1Unitary = "The u1 matrix is unitary: "+ str(u1.isUnitary())
        u2Unitary = "The u2 matrix is unitary: "+ str(u2.isUnitary())
        print(u1Unitary)
        print(u2Unitary)
        u1yu2 = u1.multiplication(u2)
        u1yu2Unitary = "The product of the matrices is unitary: "+ str(u1yu2.isUnitary())
        print(u1yu2Unitary)

    def testExercise442(self):
        print("\n--- Exercise 4.4.2")
        stateVector = matrix.realMatrix([[1],[0],[0],[0]])
        matrixDynamic = matrix.complexMatrix([
        [(0,0),(1/math.sqrt(2),0),(1/math.sqrt(2),0),(0,0)],
        [(0,1/math.sqrt(2)),(0,0),(0,0),(1/math.sqrt(2),0)],
        [(1/math.sqrt(2),0),(0,0),(0,0),(0,1/math.sqrt(2))],
        [(0,0),(1/math.sqrt(2),0),(-1/math.sqrt(2),0),(0,0)]])
        stateOfSystem3 = matrixDynamic.marbleMove(stateVector,3)
        probability = qm.particleProbability(stateOfSystem3,3)
        probabilityPos = "The chance of the quantum ball to be found at point 3 is : "+str(probability)
        print(probabilityPos)

if __name__ == '__main__':
    unittest.main()