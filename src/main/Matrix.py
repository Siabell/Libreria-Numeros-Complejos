import math
import sys
import ComplexNumber as complex

class Matrix:
    def __init__(self, pmatrix):
        self.mtx =pmatrix
        self.m = len(pmatrix) #rows
        self.n = len(pmatrix) #column

    def add (self, mat2):
        """ Suma de dos matrices """
        if (self.m != mat2.m and self.n != mat2.n):
            raise Exception('The dimensions of the matrices are not the same ')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
            for i in range (self.m):
                for j in range (self.n):
                    matrixResult[i][j] = self.mtx[i][j].add(mat2.mtx[i][j])
            matResult = Matrix(matrixResult)
            return matResult

    def subtract (self, mat2):
        """ Resta de dos matrices """
        if (self.m != mat2.m and self.n != mat2.n):
            raise Exception('The dimensions of the matrices are not the same ')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
            for i in range (self.m):
                for j in range (self.n):
                    matrixResult[i][j] = self.mtx[i][j].subtract(mat2.mtx[i][j])
            matResult = Matrix(matrixResult)
            return matResult

    def inverse (self):
        """ Inversa de una matriz"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[i][j] = self.mtx[i][j].inverse()
        matResult = Matrix(matrixResult)
        return matResult
    
    def scalarMultiplication(self,c):
        """ Producto escalar de una matrix y un numero complejo c """
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[i][j]=self.mtx[i][j].multiplication(c)
        matResult = Matrix(matrixResult)
        return matResult

    def multiplication(self, mat2):
        """ multiplicacion de dos matrices """
        if (self.m != mat2.n ):
            raise Exception('The dimensions of rows and columns do not match')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
            for i in range (self.m):
                for j in range (mat2.n):
                    sum = complex.ComplexNumber(0,0)
                    for z in range(self.n):
                        sum = sum.add(self.mtx[i][z].multiplication(mat2.mtx[z][j]))
                    matrixResult[i][j] = sum
            matResult = Matrix(matrixResult)
            return matResult

    def transpose (self) :
        """ Transpuesta de una matriz"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[j][i] = self.mtx[i][j]
        matResult = Matrix(matrixResult)
        return matResult
    
    def conjugate (self):
        """ Conjuagada de una matriz"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[i][j] = self.mtx[i][j].conjugate()
        matResult = Matrix(matrixResult)
        return matResult

    def adjoint (self):
        """ Adjunta de una matriz que es la tranpuesta de la conjugada"""
        return self.conjugate().transpose()

    def trace (self):   
        """ Traza de una matriz: la suma de los elementos de la diagonal"""
        if (self.m != self.n ):
            raise Exception('The dimensions of rows and columns do not match')
        else:
            sum = complex.ComplexNumber(0,0)
            for i in range (self.m):
                sum = sum.add(self.mtx[i][i])
            print(sum.partReal)
            return sum.partReal

    def innerProduct(self,mat2):
        """ Producto interno de una matriz: la traza del resultado de 
            la multiplicacion de las mattriz adjunta y la segunda matriz"""
        adjunta = self.adjoint()
        matResult = adjunta.multiplication(mat2)
        return matResult.trace()

    def norm(self):
        """ norma de una matriz: raiz del producto interno de la misma matriz """
        result = math.sqrt(self.innerProduct(self))
        return round(result,3)
        

    def equals(self,mat2):
        """ Compara si los elementos de las matrices son iguales """
        result = True
        if (self.m!= mat2.m or self.n != mat2.n):
            raise Exception('The dimensions of the matrices are not the same ')
        for i in range(self.m):
            for j in range(self.n):
                if(self.mtx[i][j].partReal != mat2.mtx[i][j].partReal or self.mtx[i][j].partImag != mat2.mtx[i][j].partImag):
                    result = False
        return result

    def showMatrix(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.mtx[i][j].partReal,self.mtx[i][j].partImag)
            print("-----")