import unittest
import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import QuantumMath as qm 

class classicToQuantumTest(unittest.TestCase):

    def testMarbleExperimenWtithBooleans(self):
        m =  matrix.booleanMatrix([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]])
        x = matrix.realMatrix([[6],[2],[1],[5],[3],[10]])
        # un movimiento
        mState1 = m.marbleMove(x,1)
        mSolState1= matrix.realMatrix([[0],[0],[12],[5],[1],[9]])
        self.assertTrue(mState1.equals(mSolState1))

        # dos movimientos
        mState2 = m.marbleMove(x,2)
        mSolState2 = matrix.realMatrix([[0],[0],[9],[5],[12],[1]])
        self.assertTrue(mState2.equals(mSolState2))

        # tres movimientos
        mState3 = m.marbleMove(x,3)
        mSolState3 = matrix.realMatrix([[0],[0],[1],[5],[9],[12]])
        self.assertTrue(mState3.equals(mSolState3))

        # seis movimientos
        mState6 = m.marbleMove(x,6)
        mSolState6 = matrix.realMatrix([[0],[0],[1],[5],[9],[12]])
        self.assertTrue(mState6.equals(mSolState6))

    def testProbabilisticExperimentWithTripleSlits(self):
        # se crea la matrix que representa la dinamica del sistema
        m =  matrix.realMatrix([
        [0,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [0,1/3,0,0,1,0,0,0,0,0,0],
        [0,1/3,0,0,0,1,0,0,0,0,0],
        [0,1/3,1/3,0,0,0,1,0,0,0,0],
        [0,0,1/3,0,0,0,0,1,0,0,0],
        [0,0,1/3,1/3,0,0,0,0,1,0,0],
        [0,0,0,1/3,0,0,0,0,0,1,0],
        [0,0,0,1/3,0,0,0,0,0,0,1],
        ])
        # stado inicial
        x = matrix.booleanMatrix([[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
        # estado despues de 4 "clicks"
        mState = m.marbleMove(x,4)
        mSolState = matrix.realMatrix([[0],[0],[0],[0],[0.1111],[0.1111],[0.2222],[0.1111],[0.2222],[0.1111],[0.1111]])     
        self.assertTrue(mState.equals(mSolState))

    def testDoubleSlitQuantumExperiment(self):
        # se crea la matrix que representa la dinamica del sistema
        m =  matrix.complexMatrix([
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(1,0),(0,0)],
        [(0,0),(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]])
        # estado inicial 
        s0 = matrix.booleanMatrix([[1],[0],[0],[0],[0],[0],[0],[0]])
        # Se realizan 2 clicks y se obtiene el vector de stado
        s2 = m.marbleMove(s0,2)
        # Se calcula la probabilidad del vector de estado
        p2 = s2.probability()
        # grafica de las probabilidades
        vPosition = [0,1,2,3.5,4,5.8,6,7]
        #matrix.plot_bar(vPosition,p2 ,"probability","Position","Position probability double Slit")

    def testPShouldGetPositionOfParticle(self):
        ket = matrix.complexMatrix([[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]])
        probPart=qm.particleProbability(ket,2)
        self.assertAlmostEqual(probPart,0.0526)

        ket = matrix.complexMatrix([[(2,1)],[(-1,2)],[(0,1)],[(1,0)],[(3,-1)],[(2,0)],[(0,-2)],[(-2,1)],[(1,-3)],[(0,-1)]])
        probPart=qm.particleProbability(ket,7)
        self.assertAlmostEqual(probPart,0.1087)
        

    def testShouldCalculateAmplitude(self):
        ket = matrix.complexMatrix([[(-3,-1)],[(0,-2)],[(0,1)],[(2,0)]])
        ket2 = matrix.complexMatrix([[(-1,-4)],[(2,-3)],[(-7,6)],[(-1,1)],[(-5,-3)],[(5,0)],[(5,8)],[(4,-4)],[(8,-7)],[(2,-7)]])
        braket = qm.transitionAmplitude(ket,ket2)
        print(braket)
        
        '''
        ket3 = matrix.complexMatrix([[(1/math.sqrt(2),0)],[(0,1/math.sqrt(2))]])
        omega =  matrix.complexMatrix([[(2,0),(1,1)],[(1,-1),(3,0)]])
        omegaKet = omega.action(ket3)
        esd = ket3.innerProduct(omegaKet)
        esd.showNumber()
        print('braket')
        '''




if __name__ == '__main__':
    unittest.main()





