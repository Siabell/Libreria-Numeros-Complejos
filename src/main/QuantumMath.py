import ComplexNumber as complex
import Matrix as matrix
import math
import sympy 
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def particleProbability(ket,position):
    """ calcular la probabilidad de encontrar la particula en una posición en particular"""
    m = matrix.getRows(ket) #rows
    n = matrix.getColumns(ket) #column
    ketM = matrix.getMtx(ket)
    ci = math.pow(ketM[position][0].modulus(),2)
    sum = 0
    for i in range (m):
        for j in range (n):
            sum = sum + math.pow(ketM[i][j].modulus(),2)
    pxi = ci/sum 
    return round (pxi,4)

def normalize(ket):
    """Normaliza un vector ket, dividiendo a las entradas por la longitud del vector """
    length = ket.norm()
    m = matrix.getRows(ket) #rows
    n = matrix.getColumns(ket) #column
    ketM = matrix.getMtx(ket)
    for i in range (m):
        for j in range (n):
            temp = ketM[i][j]
            lengthC = complex.ComplexNumber(length,0)
            ketM[i][j] = temp.division(lengthC)
    matrixVector = matrix.Matrix(ketM)
    return matrixVector


def transitionAmplitude(ketIni,ketFin):
    """Dados dos vectores ket (inicial y final ) calcula la probabilidad de transitar del primer vector al segundo."""
    ket1M = normalize(ketIni)
    ket2M = normalize(ketFin)
    braket = ket2M.innerProduct(ket1M)
    norm1 =  ket1M.norm()
    norm2 = ket2M.norm()
    productNorm = norm1*norm2
    productC = complex.ComplexNumber(productNorm,0)
    amplitud = braket.division(productC)
    return amplitud

def expectedValue(observable, state):
    """El valor esperado de observar un observable repetidamente en el mismo estado"""
    observableState = observable.action(state)
    value = state.innerProduct(observableState)
    return value

def mean(observable, state):
    """La media de observar un observable repetidamente en el mismo estado"""
    observableState = observable.action(state)
    value = state.innerProduct(observableState)
    return value

def variance(omega, ket):
    """Varianza:  la dispersión de la distribución en torno a su valor esperado """
    expectedVal = expectedValue(omega, ket)
    identity = matrix.identityMatrix(matrix.getRows(omega), matrix.getColumns(omega))
    matrixExpected = identity.scalarMultiplication(expectedVal)
    hermitianOp = omega.subtract(matrixExpected)
    HermitCuadrado = hermitianOp.multiplication(hermitianOp)
    expectedResult = expectedValue(HermitCuadrado,ket)
    return expectedResult

def HermitianVarianceAndMean(omega,ket):
    """Revisa que la matriz (observable) sea hermitiana, y si lo es, calcula la media
    y la varianza del observable en el estado dado y los retorna."""
    if (omega.isHermitian()==False):
        raise Exception('The matrix is not hermitian ')
    else:
        var = variance(omega,ket)
        meanVal = mean(omega, ket)
        return (meanVal, var)



    

