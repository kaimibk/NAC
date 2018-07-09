
**Collaborators:**
- Kaimi Kahihikolo
- Kento Masuda

**Updated:** 2018-06-22
___

<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Overall-Project-Goals-and-Notes" data-toc-modified-id="Overall-Project-Goals-and-Notes-1">Overall Project Goals and Notes</a></span></li><li><span><a href="#Weekly-Project-Log" data-toc-modified-id="Weekly-Project-Log-2">Weekly Project Log</a></span><ul class="toc-item"><li><span><a href="#Week-1-Log" data-toc-modified-id="Week-1-Log-2.1">Week 1 Log</a></span></li><li><span><a href="#Week-2-Log" data-toc-modified-id="Week-2-Log-2.2">Week 2 Log</a></span></li><li><span><a href="#Week-3-Log" data-toc-modified-id="Week-3-Log-2.3">Week 3 Log</a></span></li><li><span><a href="#Week-4-Log" data-toc-modified-id="Week-4-Log-2.4">Week 4 Log</a></span></li></ul></li></ul></div>

___
## Overall Project Goals and Notes
___

In the [Pleiades paper](http://adsabs.harvard.edu/abs/2018MNRAS.476.3245J) they used $v sin(i)$ and $P_{rot}$ as inputs and assumed the inclination distribution to derive stellar radii, $R_*$. On the other hand, our purpose is to **use the stellar radii directly measured with Gaia as another input to constrain the inclination distribution**

1. Write a code to derive the probability distribution of the stellar inclination for each star, given $vsin(i)$, $P_{rot}$, and $R_*$

1. Combine those individual constraints to derive the *population-level* distribution for the sample. 

___
## Weekly Project Log
___

### Week 1 Log
___

**2018-06-18**
- Read in Pleiades csv data files
- Query Gaia Database for targets
    - Search around target RA/DEC and retrieve: radius_val, luminosity, teff, parallax, phot_g_mean_mag
- Merge with csv data files
- (optional) Generate sql database for the object

**2018-06-19**
- Make the Gaia scrapping algorithm more efficient (parallel procesing).
- Obtain point estimates for the stellar inclination, $I_s$ for each star.

**2018-06-20**
- Review Bayesian inference
- Meet with Dr. Masuda
- Go back to Gaia and get the uncertainties in radius_val, luminosity, teff, parallax, phot_g_mean_mag

**2018-06-21**
- Double check coordinate matching
    - Making sure that gaia script is choosing the closest matching coordinate
- Handle error propagation and units simultaneously
- Generate Histogram of Parallax (see Fig. 1) and $sin(I_s)$ (see Fig. 2)
- Plot $vsin(i)$ against $v=2\pi R/P_{rot}$ with error bars (see Fig. 3)

**2018-06-22**
- Update Fig. 3
    - Swap x/y axes and add 1:1 line
- Search for uncertainties for $P_{rot}$ in literature
    - Found [HERE](http://tapvizier.u-strasbg.fr/adql/?%20J/MNRAS/408/475/prd)
- Coordinate match new data set and merge with other measurements
    - Running into mismatching issues. Further inspection needed.

<table width="800" border="1" cellpadding="3">

<tr>
<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/124/?share_key=vpH9Fi67I21Pg5rr5yXH3E" target="_blank" title="parallax_hist" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/124.png?share_key=vpH9Fi67I21Pg5rr5yXH3E" alt="parallax_hist" style="max-width: 100%;width: 400px;"  width="400" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
 
<br />
Fig. 1 Histogram of Parallax Measurements
</td> 

<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/120/?share_key=VVq9v1abCXiUic9VgWOBrB" target="_blank" title="sinis_hist" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/120.png?share_key=VVq9v1abCXiUic9VgWOBrB" alt="sinis_hist" style="max-width: 100%;width: 400px;"  width="400" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
<br />
Fig. 2 Histogram of $sin(I_s)$.
</td>
</tr>


<div>
    <a href="https://plot.ly/~kaimibk/126/?share_key=mrg9PDusaPnwG7z1hjWeEo" target="_blank" title="vsinis_v" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/126.png?share_key=mrg9PDusaPnwG7z1hjWeEo" alt="vsinis_v" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
</div>
<br />
<center>Fig. 3 $vsin(i)$ against $v=2\pi R/P_{rot}$</center>

<table width="800" border="1" cellpadding="3">

<tr>
<td align="center" valign="center">
</td>
</tr>

### Week 2 Log
___

**2018-06-25**
- Remove period error values from catalog - errors are unrealistic.
- Derive Eq. 4 of this [paper](http://adsabs.harvard.edu/abs/2017AJ....154..270W)
- Review Bayesian Inferences and MCMC
- Review literature in general

**2018-06-26**
- Review Bayesian Inferences and Stats
    - Attended stats lecture by [@msyriac](https://github.com/msyriac)
- Work on deriving distribution of $sin(I_*)$

**2018-06-27**
- Compute the likelihood, $\mathcal{L}$, given various $sin(I_*) \, \in \, [0, 1]$ for each star.
- Plot $p(sin(I_*))$ see Fig. 4.

**2018-06-28**
- Improve the efficency of Likelihood calculation
- Work on calculating $p(cos i)$

**2018-06-29**
- Incorporate parallel processing to both probability calculations
- Plot $p(cos(I_*))$ see Fig. 5
- Mandatory internship meetings with Dr. Strauss


<table width="800" border="1" cellpadding="3">
<tr>
<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/140/?share_key=RwlpJBWqMfeeTIAwBle9kr" target="_blank" title="psini" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/140.png?share_key=RwlpJBWqMfeeTIAwBle9kr" alt="psini" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="kaimibk:140" sharekey-plotly="RwlpJBWqMfeeTIAwBle9kr" src="https://plot.ly/embed.js" async></script>
<br />
Fig. 4 $p(sini)$
</td>
</tr>

<table width="800" border="1" cellpadding="3">
<tr>
<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/138/?share_key=09XxWtCI9l1zdfeAyQTDF0" target="_blank" title="pcosi" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/138.png?share_key=09XxWtCI9l1zdfeAyQTDF0" alt="pcosi" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="kaimibk:138" sharekey-plotly="09XxWtCI9l1zdfeAyQTDF0" src="https://plot.ly/embed.js" async></script>
<br />
Fig. 5 $p(cosi)$
</td>
</tr>



<table width="800" border="1" cellpadding="3">

<tr>
<td align="center" valign="center">
</td>
</tr>

### Week 3 Log
___

**2018-07-02**
- Inspect distributions of inclinations
- Start deriving Stellar Radii

<table width="800" border="1" cellpadding="3">

<tr>
<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/144/?share_key=ic6Won6o4kKh8uO33tocct" target="_blank" title="pcosi_mode" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/144.png?share_key=ic6Won6o4kKh8uO33tocct" alt="pcosi_mode" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="kaimibk:144" sharekey-plotly="ic6Won6o4kKh8uO33tocct" src="https://plot.ly/embed.js" async></script>
<br />
Fig. 6 Histogram of Modes of Individual $p(\cos(I_*))$
</td> 

<td align="center" valign="center">
    <a href="https://plot.ly/~kaimibk/146/?share_key=YnwAS9EdolOl85LZjZnYCb" target="_blank" title="pcosi_avg" style="display: block; text-align: center;"><img src="https://plot.ly/~kaimibk/146.png?share_key=YnwAS9EdolOl85LZjZnYCb" alt="pcosi_avg" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="kaimibk:146" sharekey-plotly="YnwAS9EdolOl85LZjZnYCb" src="https://plot.ly/embed.js" async></script>
<br />
Fig. 7 Average of Individual, normalized $p(\cos(I_*))$
</td>
</tr>

**2018-07-03**
- Edit previous scripts to generate SQL databases instead of CSV files
- Work on converting *isoclassify* scripts to Python 3.5
- "How to be a good scientist" ethics workshop

**2018-07-04**
- Holiday

**2018-07-05**
- Work on converting *isoclassify* scripts to Python 3.5
- Requery Gaia database to obtain magnitude errors
- Lecture by Dr. Michael Strauss

**2018-07-06**
- Set up Python 2.7 environment for *isoclassify*
- Attempt to use *isoclassify* direct method.
- Mandatory internship meeting with Dr. Michael Strauss

<table width="800" border="1" cellpadding="3">

<tr>
<td align="center" valign="center">
</td>
</tr>

### Week 4 Log

**2018-07-09**
- Continue to fix *isoclassify*


```python

```


```python

```


```python

```
