import unittest
import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *

class classicToQuantumTest(unittest.TestCase):

    def testShouldDetermineStateOfSystemWithBooleans(self):
        m =  matrix.booleanMatrix([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]])
        x = matrix.booleanMatrix([[6],[2],[1],[5],[3],[10]])
        # un movimiento
        mState1 = m.marbleMove(x,1)
        mSolState1= matrix.booleanMatrix([[0],[0],[12],[5],[1],[9]])
        self.assertTrue(mState1.equals(mSolState1))

        # dos movimientos
        mState2 = m.marbleMove(x,2)
        mSolState2 = matrix.booleanMatrix([[0],[0],[9],[5],[12],[1]])
        self.assertTrue(mState2.equals(mSolState2))

        # tres movimientos
        mState3 = m.marbleMove(x,3)
        mSolState3 = matrix.booleanMatrix([[0],[0],[1],[5],[9],[12]])
        self.assertTrue(mState3.equals(mSolState3))

        # seis movimientos
        mState6 = m.marbleMove(x,6)
        mSolState6 = matrix.booleanMatrix([[0],[0],[1],[5],[9],[12]])
        self.assertTrue(mState6.equals(mSolState6))
    '''
    def testTripleSlitExperiment(self):
        m =  matrix.realMatrix([
        [0,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [1/3,0,0,0,0,0,0,0,0,0,0],
        [0,1/3,0,0,1,0,0,0,0,0,0],
        [0,1/3,0,0,0,1,0,0,0,0,0],
        [0,1/3,1/3,0,0,0,1,0,0,0,0],
        [0,0,0,1/3,0,0,0,1,0,0,0],
        [0,0,0,1/3,1/3,0,0,0,1,0,0],
        [0,0,0,0,0,1/3,0,0,0,1,0],
        [0,0,0,0,0,1/3,0,0,0,0,1],
        ])
        x = matrix.booleanMatrix([[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
        mState = m.marbleMove(x,1)
        mState.show()'''

    def testDoubleSlitExperiment(self):
        m =  matrix.ComplexMatrix([
        [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
        [(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
        [(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
        [(0,0),(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(1,0),(0,0)],
        [(0,0),(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]])

    
if __name__ == '__main__':
    unittest.main()





