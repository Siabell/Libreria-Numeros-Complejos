import unittest
import ComplexNumber as complex

class ComplexNumberTest(unittest.TestCase):

    def testShouldAddTwoComplexNumbers(self):
        c1 = complex.ComplexNumber(3, -1)
        c2 = complex.ComplexNumber(1,4)
        cResultTest = c1.add(c2)
        self.assertEqual(cResultTest.partReal,4)
        self.assertEqual(cResultTest.partImag,3)

    def testShouldSubtractTwoComplexNumbers(self):
        c1 = complex.ComplexNumber(7, 9)
        c2 = complex.ComplexNumber(3,4)
        cResultTest = c1.subtract(c2)
        self.assertEqual(cResultTest.partReal,4)
        self.assertEqual(cResultTest.partImag,5)

    def testShouldMultiplyTwoComplexNumbers(self):
        c1 = complex.ComplexNumber(3, -1)
        c2 = complex.ComplexNumber(1,4)
        cResultTest = c1.multiplication(c2)
        self.assertEqual(cResultTest.partReal,7)
        self.assertEqual(cResultTest.partImag,11)

    def testShouldDivideTwoComplexNumbers(self):
        c1 = complex.ComplexNumber(4, 5)
        c2 = complex.ComplexNumber(2,6)
        cResultTest = c1.division(c2)
        self.assertAlmostEqual(cResultTest.partReal,0.95)
        self.assertAlmostEqual(cResultTest.partImag,0.35)

    def testShouldGetConjugateOfComplexNumber(self):
        c1 = complex.ComplexNumber(4, -5)
        cResultTest = c1.conjugate()
        self.assertEqual(cResultTest.partImag,5)

    def testShouldGetModulusOfComplexNumber(self):
        c1 = complex.ComplexNumber(6, 8)
        cResultTest = c1.modulus()
        self.assertEqual(cResultTest,10)

    def testShouldGetPhaseOfComplexNumber(self):
        c1 = complex.ComplexNumber(1, 1)
        cResultTest = c1.phase()
        self.assertAlmostEqual(cResultTest,0.78539816339)

    def testShouldGetPolarRepresentationOfComplexNumber(self):
        c1 = complex.ComplexNumber(1, 1)
        cResultTest = c1.cartesianToPolar()
        self.assertAlmostEqual(cResultTest[0],1.41421356237)
        self.assertAlmostEqual(cResultTest[1],0.7853981633)

if __name__ == '__main__':
    unittest.main()
