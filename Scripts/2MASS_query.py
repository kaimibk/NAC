import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord, match_coordinates_sky
from astroquery.irsa import Irsa

main_dir = "/u/kaimibk/Documents/"
data_dir = main_dir+"data/"
out_dir = main_dir+"out/"

features = [
    'j_m', 'j_msigcom',
    'h_m', 'h_msigcom',
    'k_m', 'k_msigcom'
    ]

def to_skycoord(ra, dec, units):
    return SkyCoord(ra=ra, dec=dec, unit=units)

def Query_2MASS(series, units=units):
    global features
    c = to_skycoord(ra=series.RA, dec=series.Dec, units=units)

    temp = Irsa.query_region(c, radius = 5. * u.arcsecond, catalog='fp_psc').to_pandas
    catalog = SkyCoord(ra=temp.ra, dec=temp.dec)

    i, _, _ = match_coordinates_sky(c, catalog)

    return pd.concat([series, temp.loc[i][features]], axis=1, sort=False)

## Example of future use
## def function(row)
##      return row['key'] % row['key2']
## df['out'] = df.apply(function, axis=1)