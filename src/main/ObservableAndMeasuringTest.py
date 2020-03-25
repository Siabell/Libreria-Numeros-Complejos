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
    
    def testExcerise441(self):
        u1 =  matrix.complexMatrix([[(0,0),(1,0)],[(1,0),(0,0)]])
        u2 = matrix.complexMatrix([[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],[(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]])
        print(u1.isUnitary())
        print(u2.isUnitary())
        u1yu2 = u1.multiplication(u2)
        print(u1yu2.isUnitary())

    def testShouldCalculateVariance(self):
        ket = matrix.complexMatrix([[(math.sqrt(2)/2,0)],[(0,math.sqrt(2)/2)]])
        omega =  matrix.complexMatrix([[(1,0),(0,-1)],[(0,1),(2,0)]])
        result = qm.variance(omega,ket)
        nSol = 0.25
        result = round(result.partReal,2)
        self.assertAlmostEqual(nSol,result)


        ket = matrix.complexMatrix([[(1/math.sqrt(2),0)],[(0,1/math.sqrt(2))]])
        omega =  matrix.complexMatrix([[(0,0),(0,-1)],[(0,1),(0,0)]])
        result = qm.variance(omega,ket)
        nSol = 0
        result = round(result.partReal,0)
        self.assertAlmostEqual(nSol,result)

if __name__ == '__main__':
    unittest.main()