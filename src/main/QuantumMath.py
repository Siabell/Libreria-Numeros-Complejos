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



    

