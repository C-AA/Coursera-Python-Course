
import math

def area(numbersides, l):
    arua = .25 * numbersides * (l**2) / ( math.tan( math.pi / numbersides)) 
    return arua

print area (7, 3)