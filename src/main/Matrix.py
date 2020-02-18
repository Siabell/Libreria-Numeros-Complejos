import math
import sys
import ComplexNumber as complex
import sympy 
from sympy import *

class Matrix:
    def __init__(self, pmatrix):
        self.mtx =pmatrix
        self.m = len(pmatrix) #rows
        self.n = len(pmatrix[0]) #column

    def add (self, mat2):
        """ Suma de dos matrices/vectores """
        if (self.m != mat2.m or self.n != mat2.n):
            raise Exception('The dimensions of the matrices/vectors are not the same ')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
            for i in range (self.m):
                for j in range (self.n):
                    matrixResult[i][j] = self.mtx[i][j].add(mat2.mtx[i][j])
            matResult = Matrix(matrixResult)
            return matResult

    def subtract (self, mat2):
        """ Resta de dos matrices/vectores """
        if (self.m != mat2.m or self.n != mat2.n):
            raise Exception('The dimensions of the matrices are not the same ')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
            for i in range (self.m):
                for j in range (self.n):
                    matrixResult[i][j] = self.mtx[i][j].subtract(mat2.mtx[i][j])
            matResult = Matrix(matrixResult)
            return matResult

    def inverse (self):
        """ Inversa de una matriz/vectore"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[i][j] = self.mtx[i][j].inverse()
        matResult = Matrix(matrixResult)
        return matResult
    
    def scalarMultiplication(self,c):
        """ Producto escalar de una matrix/vector y un numero complejo c """
        
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[i][j]=self.mtx[i][j].multiplication(c)
        matResult = Matrix(matrixResult)
        return matResult

    def multiplication(self, mat2):
        """ multiplicacion de dos matrices """
        if (self.n != mat2.m ):
            raise Exception('The dimensions of rows and columns do not match')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(mat2.n)] for y in range(self.m)] 
            for i in range (self.m):
                for j in range (mat2.n):
                    sum = complex.ComplexNumber(0,0)
                    for z in range(self.n):
                        sum = sum.add(self.mtx[i][z].multiplication(mat2.mtx[z][j]))
                    matrixResult[i][j] = sum
            matResult = Matrix(matrixResult)
            return matResult

    def action(self, mat2):
        """ accion de una matriz sobre un vector (primero vector, luego matriz) """
        if (self.n != mat2.m ):
            raise Exception('The dimensions of rows and columns do not match')
        else:
            matrixResult = [[complex.ComplexNumber(0,0) for x in range(mat2.n)] for y in range(self.m)] 
            for i in range (self.m):
                for j in range (mat2.n):
                    sum = complex.ComplexNumber(0,0)
                    for z in range(self.n):
                        sum = sum.add(self.mtx[i][z].multiplication(mat2.mtx[z][j]))
                    matrixResult[i][j] = sum
            matResult = Matrix(matrixResult)
            return matResult

    def transpose (self) :
        """ Transpuesta de una matriz/vector"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.m)] for y in range(self.n)] 
        for i in range (self.m):
            for j in range (self.n):
                matrixResult[j][i] = self.mtx[i][j]
        matResult = Matrix(matrixResult)
        return matResult
    
    def conjugate (self):
        """ Conjuagada de una matriz/vector"""
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
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
            #print(sum.partReal)
            return sum.partReal

    def innerProduct(self,mat2):
        """ Producto interno de una matriz: la traza del resultado de 
            la multiplicacion de las matriz adjunta y la segunda matriz"""
        adjunta = self.adjoint()
        matResult = adjunta.multiplication(mat2)
        return matResult.trace()

    def norm(self):
        """ norma de una matriz: raiz del producto interno de la misma matriz """
        result = math.sqrt(self.innerProduct(self))
        return round(result,3)
    
    def distance(self,mat2):
        """ distance de vectores""" 
        reduc=self.subtract(mat2)
        return reduc.norm()

    def isHermitian(self):
        """ verifica si una matriz es hermitian""" 
        transpuesta = self.transpose()
        conjugada = self.conjugate()
        hermitian = False
        if transpuesta.equals(conjugada):
            hermitian = True
        return hermitian

    def isUnitary(self):
        """ verifica si una matriz es unitaria""" 
        adjunta = self.adjoint()
        mUnitaria = self.multiplication(adjunta)
        unitary = True
        for i in range (self.m):
            for j in range (self.n):
                if (i == j and (mUnitaria.mtx[i][j].partReal!=1 or mUnitaria.mtx[i][j].partImag!=0)) :
                    unitary = False
                elif (i != j and (mUnitaria.mtx[i][j].partReal!=0 or mUnitaria.mtx[i][j].partImag!=0)):
                    unitary = False
        #mUnitaria.show()
        return unitary

    def tensorProduct(self,mat2):
        "producto tensor"
        matrixResult = [[complex.ComplexNumber(0,0) for x in range(self.n*mat2.n)] for y in range(self.m*mat2.m)] 
        for i in range (self.m):
            for j in range (self.n):
                matriz = mat2.scalarMultiplication(self.mtx[i][j])
                matrixResult = self.fillTensor(matrixResult,matriz,i,j)
        matResult = Matrix(matrixResult)
        return matResult
    
    def fillTensor(self,matrixResult,add,rows,colums):
        inicioI = add.m*rows
        inicioJ = add.n*colums
        finI=inicioI+add.m
        finJ=inicioJ+add.n
        realI=0
        realJ=0
        for i in range(inicioI,finI):
            for j in range(inicioJ,finJ):
                matrixResult[i][j]=add.mtx[realI][realJ]
                realJ=realJ+1
            realJ=0
            realI=realI+1
        return matrixResult
    
    def eigenValues(self):
        """ retorna los vectores propios de una matriz""" 
        SympyMatrix = [[complex.ComplexNumber(0,0) for x in range(self.n)] for y in range(self.m)] 
        for i in range (self.m):
            for k in range (self.n):
                SympyMatrix[i][k] = ((self.mtx[i][k].partReal)+(self.mtx[i][k].partImag*1j))
        matResult = sympy.Matrix(SympyMatrix)
        values = matResult.eigenvals()
        resultValues = []
        for key,value in values.items():
            for nRepetidos in range(value):
                #print(key)
                resultValues.append(complex.ComplexNumber(sympy.re(key),sympy.im(key)))
        return resultValues

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

    def equalsList(self,list2):
        result = True
        if (self.length!= list2.length):
            raise Exception('The dimensions of the lists are not the same ')
        for i in range(self.length):
            if(self[i].partReal != list2[i][j].partReal or self[i].partImag != list2[i].partImag):
                result = False
        return result

    def show(self):
        for i in range(self.m):
            strRow=""
            for j in range(self.n):
                strRow = strRow + " " +self.mtx[i][j].showNumber()
                #print(self.mtx[i][j].showNumber()+"numero")
            print(strRow)


    def determinante (self, x, num):
        mat = self
        mat.show()
        print("------------------")
        for i in range(num):
            
            temp = self.multiplication(mat)
            #temp.show()
            mat = temp
        mat.show()
        print("hola yo")
        return x.multiplication(mat)
