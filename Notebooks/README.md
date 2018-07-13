## Notebooks:
___
Contains miscellaneous Jupyter Notebooks developed for testing purposes.
**[Parsing Data](Notebooks/Parsing%20Data.ipynb)**
- Merge 2 measurement tables from Jackson et al. (2018).
- Coordinate match objects to GAIA catalog.
- Query GAIA D2 to retrieve the following values:
    - parallax, radius_val, lum_val, teff_val and errors where available
- Return a merged pandas DataFrame consisting of 3 tables.

**[Point Estimates](Notebooks/Point_estimates.ipynb)**
- Estimate stellar inclination point estimates for each star by recalling...
*sin(I_s) = P_{rot} / 2\pi R_{s} (v sin(i))*, where *P_{rot}* is the rotation period, 
*R* is the radius, and *vsin(i)* is the sky-projected rotation velocity.
- Analyze the distribution of *sin(I_s)*.
- Analyze the distribution of GAIA parallax measurements to confirm cluster association.
- Analyze the vsini vs v with propagated errors.

**[sin(i) Probabilities](Notebooks/sini_probabilities.ipynb)**
- For each star compute the probability of the data given *sin(i)*.
- Analyze the resulting distributions.

**[cos(i) Probabilities](Notebooks/cosi_probabilities.ipynb)**
- For each star compute the probability of the data given *cos(i)*.
- Analyze the resulting distributions.

**[Query 2MASS](Notebooks/Query%202MASS.ipynb)**
- Coordinate match objects to 2MASS survey and retrieve the *j*, *h*, and *k* magnitudes 
with their associated errors. 
- Using the magnitudes and parallax as inputs in *isoclassiy*, 
retrieve estimates for the stellar radii.
- Compare *isoclassify* radius values to those computed in Jackson et al (2018) and GAIA.

**[Inclination Distribution](Notebooks/Inclination_distribution.ipynb)**
- Inspect the modes of individual *p(cos(i))*.
- Inspect individual, normalized *p(cos(i))*.

**[testing](Notebooks/testing.ipynb)**
- Miscellaneous tests notebook.