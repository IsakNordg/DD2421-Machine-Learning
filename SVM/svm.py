from scipy.optimize import minimize
import numpy, random, math
import matplotlib.pyplot as plt

#ret = minimize(objective, start bounds=B, constraints=XC)
#alpha = ret['x']
#This will find the vector ⃗ which minimizes the function objective within the bounds B and the constraints XC.

def objective(vector):
    #Effectively implements the expression that should be minimized (our equation)
    return scalarValue