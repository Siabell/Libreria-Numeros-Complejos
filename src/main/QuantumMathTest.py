import unittest
import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import QuantumMath as qm 

class QuantumMathTest(unittest.TestCase):

    def testPShouldGetPositionOfParticle(self):
        ket = matrix.complexMatrix([[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]])
        probPart=qm.particleProbability(ket,2)
        self.assertAlmostEqual(probPart,0.0526)

        ket = matrix.complexMatrix([[(2,1)],[(-1,2)],[(0,1)],[(1,0)],[(3,-1)],[(2,0)],[(0,-2)],[(-2,1)],[(1,-3)],[(0,-1)]])
        probPart=qm.particleProbability(ket,7)
        self.assertAlmostEqual(probPart,0.1087)
        

    def testShouldCalculateAmplitude(self):
        
        ket = matrix.complexMatrix([[(2,1)],[(-1,2)],[(0,1)],[(1,0)],[(3,-1)],[(2,0)],[(0,-2)],[(-2,1)],[(1,-3)],[(0,-1)]])
        ket2 = matrix.complexMatrix([[(-1,-4)],[(2,-3)],[(-7,6)],[(-1,1)],[(-5,-3)],[(5,0)],[(5,8)],[(4,-4)],[(8,-7)],[(2,-7)]])
        braket = qm.transitionAmplitude(ket,ket2)
        mSol = complex.ComplexNumber(-0.022,-0.131)
        self.assertAlmostEqual(braket.partReal,mSol.partReal)
        self.assertAlmostEqual(braket.partImag,mSol.partImag)
        
    def testSloudCalculateExpectedValue(self):
        ket3 = matrix.complexMatrix([[(1/math.sqrt(2),0)],[(0,1/math.sqrt(2))]])
        omega =  matrix.complexMatrix([[(2,0),(1,1)],[(1,-1),(3,0)]])
        esd = qm.expectedValue(omega,ket3)
        nSol = 1.50
        esd = round(esd.partReal,2)
        self.assertAlmostEqual(nSol,esd)

        ket = matrix.complexMatrix([[(math.sqrt(2)/2,0)],[(0,math.sqrt(2)/2)]])
        omega =  matrix.complexMatrix([[(1,0),(0,-1)],[(0,1),(2,0)]])
        esd = qm.expectedValue(omega,ket)
        nSol = 2.5
        esd = round(esd.partReal,1)
        self.assertAlmostEqual(nSol,esd)


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

    def testShouldVerifiedIfObservableisHermitianAndCalculateMeanAndVariance(self):
        omega =  matrix.complexMatrix([[(0,0),(0,-1)],[(0,1),(0,0)]])
        ket = matrix.complexMatrix([[(1/math.sqrt(2),0)],[(0,1/math.sqrt(2))]])
        mean,variance = qm.HermitianVarianceAndMean(omega,ket)
        varianceSol = 0
        meanSol = 1
        variance = round(variance.partReal,0)
        mean = round(mean.partReal,0)
        self.assertAlmostEqual(varianceSol,variance)
        self.assertAlmostEqual(meanSol,mean)

        #noHermitianMatriz
        omega =  matrix.complexMatrix([[(0,7),(0,-1)],[(0,1),(0,0)]])
        ket = matrix.complexMatrix([[(1/math.sqrt(2),0)],[(0,1/math.sqrt(2))]])
        HermitianMatrix = True
        try:
            variance,mean = qm.HermitianVarianceAndMean(omega,ket)
        except:
            HermitianMatrix = False
        self.assertFalse(HermitianMatrix)

    def testeigenValuesAndEigenVectorsProbability(self):
        omega = matrix.complexMatrix([[(-1,0),(0,-1)],[(0,1),(1,0)]])
        startState = matrix.complexMatrix([[(1/2,0)],[(1/2,0)]])
        #Valores Propios
        eigenValues = omega.eigenValues()
        solutionEigenValues = [complex.ComplexNumber(-math.sqrt(2),0),complex.ComplexNumber(math.sqrt(2),0)]
        for i in range(len(eigenValues)):
            solutionEigenValues[i]
            solutionEigenValues[i]
        #Vectores Propios
        eigenVectorsProbabilities = qm.probabilityForAStateToCollapseIntoAnEigenVentor(omega,startState)
        solutionProbabilities=[0.5,0.5]
        for i in range(len(eigenVectorsProbabilities)):
            probability = round(eigenVectorsProbabilities[i],2)
            self.assertAlmostEqual(probability,solutionProbabilities[i])


if __name__ == '__main__':
    unittest.main()


