import unittest
import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *
class ComplexNumberTest(unittest.TestCase):

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

    def testShouldGetTheInverseOfAVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, -7.86), complex.ComplexNumber(6.5, 1),complex.ComplexNumber(-4, 8)]])
        mTest = m1.inverse()
        mSol = matrix.Matrix([[complex.ComplexNumber(-2, 7.86), complex.ComplexNumber(-6.5, -1),complex.ComplexNumber(4, -8)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldMultiplyAnScalarAndAComplexVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, 3), complex.ComplexNumber(0, 0),complex.ComplexNumber(5, 1), complex.ComplexNumber(4, 0)]])
        scalar = complex.ComplexNumber(3,2)
        mTest = m1.scalarMultiplication(scalar)
        mSol =  matrix.Matrix([[complex.ComplexNumber(12, 21), complex.ComplexNumber(0, 0),complex.ComplexNumber(13, 13), complex.ComplexNumber(12, 8)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldAddTwoComplexMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 4)], [complex.ComplexNumber(0, 2), complex.ComplexNumber(-3, 1)]])
        m3 = matrix.Matrix([[complex.ComplexNumber(2, -7.86), complex.ComplexNumber(6.5, 1),complex.ComplexNumber(-4, 8)]])
        MatricesDifferentLength = False
        try:
            mTest1 = m1.add(m3)
        except:
            MatricesDifferentLength = True
        mTest2 = m1.add(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(0, -1), complex.ComplexNumber(6, 4)], [complex.ComplexNumber(4, 8), complex.ComplexNumber(-1, 3)]])
        self.assertTrue(MatricesDifferentLength)
        self.assertTrue(mTest2.equals(mSol))

    def testShouldSubtractTwoMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 4)], [complex.ComplexNumber(0, 2), complex.ComplexNumber(-3, 1)]])
        m3 = matrix.Matrix([[complex.ComplexNumber(2, -7.86), complex.ComplexNumber(6.5, 1),complex.ComplexNumber(-4, 8)]])
        MatricesDifferentLength = False
        try:
            mTest1 = m1.subtract(m3)
        except:
            MatricesDifferentLength = True
        mTest2 = m1.subtract(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(-2, -1), complex.ComplexNumber(0, -4)], [complex.ComplexNumber(4, 4), complex.ComplexNumber(5, 1)]])
        self.assertTrue(MatricesDifferentLength)
        self.assertTrue(mTest2.equals(mSol))

    def testShouldGetTheInverseOfAMatrix(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, -7.86), complex.ComplexNumber(6.5, 1)],[complex.ComplexNumber(-4, 8),complex.ComplexNumber(-5, 3)]])
        mTest = m1.inverse()
        mSol = matrix.Matrix([[complex.ComplexNumber(-2, 7.86), complex.ComplexNumber(-6.5, -1)],[complex.ComplexNumber(4, -8),complex.ComplexNumber(5, -3)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldMultiplyAnScalarAndAComplexMatrix(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, -7.86), complex.ComplexNumber(6.5, 1)],[complex.ComplexNumber(-4, 8),complex.ComplexNumber(-5, 3)]])
        scalar = complex.ComplexNumber(4,2)
        mTest = m1.scalarMultiplication(scalar)
        mSol = matrix.Matrix([[complex.ComplexNumber(27.72, -25.44), complex.ComplexNumber(24, 17)],[complex.ComplexNumber(-32, 24),complex.ComplexNumber(-26, 2)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheTransposeOfAVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, 5), complex.ComplexNumber(1, 1),complex.ComplexNumber(4, 3)]])
        mTest = m1.transpose()
        mSol = matrix.Matrix([[complex.ComplexNumber(2, 5)],[complex.ComplexNumber(1, 1)],[complex.ComplexNumber(4, 3)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheTransposeOfAMatrix(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.transpose()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)], [complex.ComplexNumber(2, 12), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(2, 5)],[complex.ComplexNumber(0, -19), complex.ComplexNumber(17, 0),complex.ComplexNumber(3, -4.5)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheConjugateOfAVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, 5), complex.ComplexNumber(1, -8.62),complex.ComplexNumber(4, -3)]])
        mTest = m1.conjugate()
        mSol = matrix.Matrix([[complex.ComplexNumber(2, -5),complex.ComplexNumber(1, 8.62),complex.ComplexNumber(4, 3)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheConjugateOfAMatrix(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.conjugate()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, 3), complex.ComplexNumber(2, -12),complex.ComplexNumber(0, 19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, -2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, -5),complex.ComplexNumber(3, 4.5)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheAdjointOfAVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(2, 5), complex.ComplexNumber(1, 1),complex.ComplexNumber(4, -3)]])
        mTest = m1.adjoint()
        mSol = matrix.Matrix([[complex.ComplexNumber(2, -5)],[complex.ComplexNumber(1, -1)],[complex.ComplexNumber(4, 3)]])
        self.assertTrue(mTest.equals(mSol))

    def testShouldGetTheAdjointOfAMatrix(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(6, -3), complex.ComplexNumber(2, 12),complex.ComplexNumber(0, -19)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(5, 2.1),complex.ComplexNumber(17, 0)],[complex.ComplexNumber(1, 0), complex.ComplexNumber(2, 5),complex.ComplexNumber(3, -4.5)]])
        mTest = m1.adjoint()
        mSol =  matrix.Matrix([[complex.ComplexNumber(6, 3), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)], [complex.ComplexNumber(2, -12), complex.ComplexNumber(5, -2.1),complex.ComplexNumber(2, -5)],[complex.ComplexNumber(0, 19), complex.ComplexNumber(17, 0),complex.ComplexNumber(3, 4.5)]])
        self.assertTrue(mTest.equals(mSol))
    
    def testMatricesMultiplication(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, 2), complex.ComplexNumber(0, 0),complex.ComplexNumber(5, -6)], [complex.ComplexNumber(1, 0), complex.ComplexNumber(4, 2),complex.ComplexNumber(0, 1)],[complex.ComplexNumber(4, -1), complex.ComplexNumber(0, 0),complex.ComplexNumber(4, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(5, 0), complex.ComplexNumber(2, -1),complex.ComplexNumber(6, -4)], [complex.ComplexNumber(0, 0), complex.ComplexNumber(4, 5),complex.ComplexNumber(2, 0)],[complex.ComplexNumber(7, -4), complex.ComplexNumber(2, 7),complex.ComplexNumber(0, 0)]])
        m3 = matrix.Matrix([[complex.ComplexNumber(-1, -1), complex.ComplexNumber(3, 0)], [complex.ComplexNumber(4, 6), complex.ComplexNumber(2, 2)]])
        MatricesDifferentLength = False
        try:
            mTest1 = m1.subtract(m3)
        except:
            MatricesDifferentLength = True
        mTest2 = m1.multiplication(m2)
        mSol =  matrix.Matrix([[complex.ComplexNumber(26, -52), complex.ComplexNumber(60, 24),complex.ComplexNumber(26, 0)], [complex.ComplexNumber(9, 7), complex.ComplexNumber(1, 29),complex.ComplexNumber(14, 0)],[complex.ComplexNumber(48, -21), complex.ComplexNumber(15, 22),complex.ComplexNumber(20, -22)]])
        self.assertTrue(MatricesDifferentLength)
        self.assertTrue(mTest2.equals(mSol))

    def testShouldGetTheInnerProductoOfTwoVectors(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(8, 0), complex.ComplexNumber(3,0),complex.ComplexNumber(7, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(0, 0), complex.ComplexNumber(-1,0),complex.ComplexNumber(2, 0)]])
        mTest = m1.innerProduct(m2)
        temo = mTest.getParteReal()
        mSol = 11
        self.assertEqual(mSol,temo)

    def testShouldGetTheInnerProductoOfTwoMatrices(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(1, 0)], [complex.ComplexNumber(-1, 0), complex.ComplexNumber(1, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(2, 0), complex.ComplexNumber(1, 0)], [complex.ComplexNumber(1, 0), complex.ComplexNumber(3, 0)]])
        mTest = m1.innerProduct(m2)

        mSol = 5
        self.assertEqual(mSol,mTest)
    
    def testActionOfaMatrixAndVector(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)],[ complex.ComplexNumber(0, 0), complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0)],[ complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0), complex.ComplexNumber(1, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(0, 0),complex.ComplexNumber(1, 0)]])
        mTest = m2.action(m1)
        mSol = matrix.Matrix([[complex.ComplexNumber(2, 0), complex.ComplexNumber(0, 0),complex.ComplexNumber(2, 0)]])
        self.assertTrue(mTest.equals(mSol))
    
    def testGetTheNorm (self):
        m1 = matrix.Matrix([[complex.ComplexNumber(4, 3), complex.ComplexNumber(6,-4),complex.ComplexNumber(12, -7), complex.ComplexNumber(0, 13)]])
        mTest = m1.norm()
        mSol = 20.952
        self.assertEqual(mTest, mSol)

    def testShouldGetTheDistance(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(3, 0),complex.ComplexNumber(1,0),complex.ComplexNumber(2, 0)]])
        m2 = matrix.Matrix([[complex.ComplexNumber(2, 0),complex.ComplexNumber(2,0),complex.ComplexNumber(-1, 0)]])
        mTest = m1.distance(m2)
        mSol = round(math.sqrt(11),3)
        self.assertEqual(mTest, mSol)
    
    def testIsUnitary(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(0.5, 0.5), complex.ComplexNumber(0.5, -0.5)], [complex.ComplexNumber(0.5, -0.5), complex.ComplexNumber(0.5, 0.5)]])
        mTest = m1.isUnitary()
        mSol = True
        self.assertTrue(mTest == mSol)

    def testShoulIsHermitian(self):
        m1 = matrix.Matrix([[complex.ComplexNumber(7, 0),complex.ComplexNumber(6,5)],[complex.ComplexNumber(6, -5),complex.ComplexNumber(-3, 0)]])
        mTest = m1.isHermitian()
        mSol = True
        self.assertTrue(mTest == mSol)

    def testShouldGetTensorProduct(self):
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
        #resultado.show()

    def testShouldGeteigenValues(self):
        self.assertTrue(True)
        mSol =  matrix.Matrix([[complex.ComplexNumber(1, 0), complex.ComplexNumber(-3, 0),complex.ComplexNumber(3, 0)], [complex.ComplexNumber(3, 0), complex.ComplexNumber(-5,0),complex.ComplexNumber(3, 0)],[complex.ComplexNumber(6, 0), complex.ComplexNumber(-6, 0),complex.ComplexNumber(4, 0)]])
        listValues = mSol.eigenValues()
        listSolutio = [complex.ComplexNumber(4, 0), complex.ComplexNumber(-2, 0),complex.ComplexNumber(-2, 0)]
        result = True
        if (len(listValues)!= len(listSolutio)):
            raise Exception('The dimensions of the lists are not the same ')
        for i in range(len(listValues)):
            if(listValues[i].partReal != listSolutio[i].partReal or listValues[i].partImag != listSolutio[i].partImag):
                result = False


if __name__ == '__main__':
    unittest.main()
