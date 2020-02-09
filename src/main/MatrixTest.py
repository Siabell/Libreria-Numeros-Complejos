import unittest
import ComplexNumber as complex
import Matrix as matrix
import math

class ComplexNumberTest(unittest.TestCase):

    def testShouldAddTwoMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 4)], [complex.ComplexNumber(0, 2), complex.ComplexNumber(-3, 1)]])
        mTest = m1.add(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(0, -1), complex.ComplexNumber(6, 4)], [complex.ComplexNumber(4, 8), complex.ComplexNumber(-1, 3)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldAddTwoComplexVectors(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, 5), complex.ComplexNumber(1, 1),complex.ComplexNumber(4, 3)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(5, 13), complex.ComplexNumber(6, 2),complex.ComplexNumber(0.53, -6), complex.ComplexNumber(12, 0)]])
        m3 = matrix.Matrix([[complex.ComplexNumber(7, -8), complex.ComplexNumber(0, 4),complex.ComplexNumber(2, 0), complex.ComplexNumber(9.4, 3)]])   
        vectorSDifferentLength = False
        try:
            mTest1 = m1.add(m2)
        except:
            vectorSDifferentLength = True
        mTest2 = m2.add(m3)
        mSol =  matrix.Matrix([[complex.ComplexNumber(12, 5), complex.ComplexNumber(6, 6),complex.ComplexNumber(2.53, -6), complex.ComplexNumber(21.4, 3)]])
        self.assertTrue(vectorSDifferentLength)
        self.assertTrue(mTest2.equals(mSol))

    def testShouldSubtractTwoMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 4)], [complex.ComplexNumber(0, 2), complex.ComplexNumber(-3, 1)]])
        mTest = m1.subtract(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(-2, -1), complex.ComplexNumber(0, -4)], [complex.ComplexNumber(4, 4), complex.ComplexNumber(5, 1)]])
        self.assertTrue(mTest.equals(mSol))

    #def testInverseMatrices(self):
        
    def testMatricesMultiplication(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, 2), complex.ComplexNumber(0, 0),complex.ComplexNumber(5, -6)], [complex.ComplexNumber(1, 0), complex.ComplexNumber(4, 2),complex.ComplexNumber(0, 1)],[complex.ComplexNumber(4, -1), complex.ComplexNumber(0, 0),complex.ComplexNumber(4, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(5, 0), complex.ComplexNumber(2, -1),complex.ComplexNumber(6, -4)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(4, 5),complex.ComplexNumber(2, 0)],[complex.ComplexNumber(7, -4), complex.ComplexNumber(2, 7),complex.ComplexNumber(0, 0)]])
        mTest = m1.multiplication(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(26, -52), complex.ComplexNumber(60, 24),complex.ComplexNumber(26, 0)], [complex.ComplexNumber(9, 7), complex.ComplexNumber(1, 29),complex.ComplexNumber(14, 0)],[complex.ComplexNumber(48, -21), complex.ComplexNumber(15, 22),complex.ComplexNumber(20, -22)]])
        self.assertTrue(mTest.equals(mSol))

    def testMatrixTranspose(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.transpose()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)], [complex.ComplexNumber(2, 12), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(2, 5)],[complex.ComplexNumber(0, -19), complex.ComplexNumber(17, 0),complex.ComplexNumber(3, -4.5)]])
        self.assertTrue(mTest.equals(mSol))

    def testMatrixConjugate(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.conjugate()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, 3), complex.ComplexNumber(2, -12),complex.ComplexNumber(0, 19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, -2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, -5),complex.ComplexNumber(3, 4.5)]])
        self.assertTrue(mTest.equals(mSol))

    def testMatrixAdjoint(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.adjoint()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, 3), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)], [complex.ComplexNumber(2, -12), complex.ComplexNumber(5, -2.1),complex.ComplexNumber(2, -5)],[complex.ComplexNumber(0, 19), complex.ComplexNumber(17, 0),complex.ComplexNumber(3, 4.5)]])
        self.assertTrue(mTest.equals(mSol))
    
    
    def testNorm (self):
        m1 = matrix.Matrix([[complex.ComplexNumber(4, 3), complex.ComplexNumber(6,-4),complex.ComplexNumber(12, -7), complex.ComplexNumber(0, 13)]])
        mTest = m1.norm()
        mSol = 20.952
        self.assertEqual(mTest, mSol)

    def testDistance(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, 0),complex.ComplexNumber(1,0),complex.ComplexNumber(2, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(2, 0),complex.ComplexNumber(2,0),complex.ComplexNumber(-1, 0)]])
        mTest = m1.distance(m2)
        mSol = round(math.sqrt(11),3)
        self.assertEqual(mTest, mSol)
    '''
    def testIsUnitary(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(1/2, 1/2), complex.ComplexNumber(0, 1/math.sqrt(3)),complex.ComplexNumber(3/(2*math.sqrt(15)),1/(2*math.sqrt(15)))], [complex.ComplexNumber(-1/2, 0), complex.ComplexNumber(1/math.sqrt(3), 0),complex.ComplexNumber(4/(2*math.sqrt(15)), 3/(2*math.sqrt(15)))],[complex.ComplexNumber(1/2, 0), complex.ComplexNumber(0, -1/math.sqrt(3)),complex.ComplexNumber(0, 5/(2*math.sqrt(15)))]])
        mTest = m1.isUnitary()
        mSol = True
        self.assertTrue(mTest == mSol)'''

    def testIsHermitian(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(7, 0),complex.ComplexNumber(6,5)],[complex.ComplexNumber(6, -5),complex.ComplexNumber(-3, 0)]])
        mTest = m1.isHermitian()
        mSol = True
        self.assertTrue(mTest == mSol)

    def testTensorProduct(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, 0), complex.ComplexNumber(2,0)],[complex.ComplexNumber(-1, 0), complex.ComplexNumber(0, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(6, 0), complex.ComplexNumber(5,0)],[complex.ComplexNumber(3, 0), complex.ComplexNumber(2, 0)]])
        mTest = m1.tensorProduct(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(18, 0), complex.ComplexNumber(15, 0),complex.ComplexNumber(12, 0),complex.ComplexNumber(10, 0)],
        [complex.ComplexNumber(9, 0),complex.ComplexNumber(6, 0),complex.ComplexNumber(6, 0), complex.ComplexNumber(4, 0)],
        [complex.ComplexNumber(-6, 0),complex.ComplexNumber(-5, 0),complex.ComplexNumber(0, 0),complex.ComplexNumber(0, 0)],
        [complex.ComplexNumber(-3, 0),complex.ComplexNumber(-2, 0),complex.ComplexNumber(0, 0),complex.ComplexNumber(0, 0),]])
        self.assertTrue(mTest.equals(mSol))
        
    def testLabTensor(self):
        h = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(1, 0)], [complex.ComplexNumber(1, 0), complex.ComplexNumber(-1, 0)]])
        h = h.scalarMultiplication(complex.ComplexNumber(1/math.sqrt(2),0))
        x = matrix.Matrix([[complex.ComplexNumber(0, 0), complex.ComplexNumber(1, 0)], [complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0)]])
        m1 = h.tensorProduct(h)
        m2 = h.tensorProduct(x)
        v = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0),complex.ComplexNumber(0, 0), complex.ComplexNumber(0, 0)]])
        res = v.multiplication(m1)
        resultado = res.multiplication(m2)
        resultado.show()


if __name__ == '__main__':
    unittest.main()
