import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.partReal=round(real,3)
        self.partImag=round(imag,3)

    def add(nComplex1,nComplex2):
        """ sumar dos numeros complejos """
        real = nComplex1.partReal+nComplex2.partReal
        imag = nComplex1.partImag+nComplex2.partImag
        return ComplexNumber(real,imag)

    def subtract(nComplex1,nComplex2):
        """ restar dos numeros complejos """
        real = nComplex1.partReal-nComplex2.partReal
        imag = nComplex1.partImag-nComplex2.partImag
        return ComplexNumber(real,imag)

    def multiplication(nComplex1,nComplex2):
        """ multiplicar dos numeros complejos """
        real=round((nComplex1.partReal*nComplex2.partReal)-(nComplex1.partImag*nComplex2.partImag),3)
        imag=round((nComplex1.partReal*nComplex2.partImag)+(nComplex1.partImag*nComplex2.partReal),3)
        return ComplexNumber(real,imag)

    def division(nComplex1,nComplex2):
        """ dividir dos numeros complejos """
        real=((nComplex1.partReal)*(nComplex2.partReal))+((nComplex1.partImag)*(nComplex2.partImag))
        debajo=(pow(nComplex2.partReal,2)+pow(nComplex2.partImag,2))
        imag=(nComplex1.partReal*nComplex2.partImag)-(nComplex1.partImag*nComplex2.partReal)
        partereal= real/debajo
        parteImag= imag/debajo
        return ComplexNumber(partereal,parteImag)

    def modulus(nComplex):
        """ modulo de un numero complejo """
        return round(math.sqrt(pow(nComplex.partReal,2)+pow(nComplex.partImag,2)),3)

    def conjugate(nComplex):
        """ conjugada de un numero complejo """
        return ComplexNumber(nComplex.partReal,nComplex.partImag*(-1))

    def cartesianToPolar(nComplex):
        """ de cartesiana a polar de un numero complejo """
        p = math.sqrt(pow(nComplex.partReal,2)+pow(nComplex.partImag,2))
        o = math.atan2(nComplex.partReal,nComplex.partImag,)
        return (round(p,3),round(o,3))

    def phase(nComplex):
        """ phase de un numeros complejo """
        return round(math.atan2(nComplex.partReal,nComplex.partImag),3)

    def inverse(nComplex):
        """ inversa de un numeros complejo """
        parteReal = nComplex.partReal*-1
        parteImag = nComplex.partImag*-1
        return ComplexNumber(parteReal,parteImag)

    def showNumber(num):
        strNum = "( "+str(num.partReal)+" "+str(num.partImag)+"i )"
        return strNum

    def getParteReal(self):
        self.partReal

