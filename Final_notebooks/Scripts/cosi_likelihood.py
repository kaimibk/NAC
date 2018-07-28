import scipy.stats as stats
import numpy as np
from scipy.integrate import quad
from multiprocessing import Pool

def integrand(u, p1, p2, cosi):
	"""
	Intermediate step for compute_L
	Parameters
	----------
	u : For use in scipy.integrate.quad
	p1 : scipy.stats._distn_infrastructure.rv_frozen
		Frozen distribution of "v"
	p2 : scipy.stats._distn_infrastructure.rv_frozen
		Frozen distribution of "vsini"
	cosi : float
		cosi measurement for a star

	Returns
	-------
	u * (p1 evaluated at u) * (p2 evaluated at u * sqrt(1-cosi^2))
	"""
	return u * p1.pdf(u) * p2.pdf(u * np.sqrt(1 - cosi ** 2))


def compute_L(args, start=0.0, end=300.0):
	""""""
	global integrand
	cosi, p1, p2 = args
	return quad(integrand, start, end, args=(p1, p2, cosi))[0]


def Likelihood(cosis, v, v_sigma, vsini, vsini_sigma, distribution="uniform"):
	"""
	Calculate the likelihood of D given cosi
	Parameters
	----------
	cosis : array-like
		values of cosi to evaluate
	v : float
		velocity for a star
	v_sigma : float
		Error on the velocity
	vsini : float
		Sky projected velocity for the star
	vsini_sigma : float
		Error on the sky projected velocity

	Returns
	-------
	(pdf / norm) : ndarray
		Normalized likelihoods given a range of cosi
	"""
	p1 = stats.norm(loc=v, scale=v_sigma)

	if distribution == "uniform":
		p2 = stats.norm(loc=vsini, scale=vsini_sigma)

	elif distribution == "flat":
		p2 = stats.uniform()

	else:
		print("Invalid distribution...defaulting to normal")
		p2 = stats.norm(loc=vsini, scale=vsini_sigma)

	with Pool(10) as pool:
		pdf = np.array(pool.map(compute_L, [(i, p1, p2) for i in cosis]))

	norm = np.trapz(pdf, cosis, dx=0.01)

	return pdf / norm