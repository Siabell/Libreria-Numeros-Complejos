import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.partReal=real
        self.partImag=imag

    def add(nComplex1,nComplex2):
        real = nComplex1.partReal+nComplex2.partReal
        imag = nComplex1.partImag+nComplex2.partImag
        return ComplexNumber(real,imag)

    def subtract(nComplex1,nComplex2):
        real = nComplex1.partReal-nComplex2.partReal
        imag = nComplex1.partImag-nComplex2.partImag
        return ComplexNumber(real,imag)

    def multiplication(nComplex1,nComplex2):
        real=(nComplex1.partReal*nComplex2.partReal)-(nComplex1.partImag*nComplex2.partImag)
        imag=(nComplex1.partReal*nComplex2.partImag)+(nComplex1.partImag*nComplex2.partReal)
        return ComplexNumber(real,imag)

    def division(nComplex1,nComplex2):
        real=(nComplex1.partReal*nComplex2.partReal)+(nComplex1.partImag*nComplex2.partImag)
        debajo=(pow(nComplex2.partReal,2)+pow(nComplex2.partImag,2))
        imag=(nComplex1.partReal*nComplex2.partImag)-(nComplex1.partImag*nComplex2.partReal)
        partereal= real/debajo
        parteImag= imag/debajo
        return ComplexNumber(partereal,parteImag)

    def modulus(nComplex):
        return math.sqrt(pow(nComplex.partReal,2)+pow(nComplex.partImag,2))

    def conjugate(nComplex):
        return ComplexNumber(nComplex.partReal,nComplex.partImag*(-1))

    def cartesianToPolar(nComplex):
        p = math.sqrt(pow(nComplex.partReal,2)+pow(nComplex.partImag,2))
        o = math.atan(nComplex.partReal/nComplex.partImag)
        return (p,o)

    def phase(nComplex):
        return math.atan(nComplex.partReal/nComplex.partImag)

    def inverse(nComplex):
        nComplex.partReal = nComplex.partReal*-1
        nComplex.partImag = nComplex.partImag*-1

    def showNumber(num):
        print(num.partReal,num.partImag)

