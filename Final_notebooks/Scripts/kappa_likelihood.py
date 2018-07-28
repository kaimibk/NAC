import numpy as np

def Likelihood(K, cosi):
	return K / (2.0*np.sinh(K)) * np.exp(K*cosi)