from astropy.coordinates import match_coordinates_sky, SkyCoord
import astropy.units as u
from astroquery.irsa import Irsa;
from astroquery.gaia import Gaia;

search_radius = 5*u.arcsecond

def query_survey(dataframe, idx, features, survey):
	series = dataframe.loc[idx]
	coord = SkyCoord(ra=series.ra, dec=series.dec)
	try:
		if survey == '2MASS':
			temp = Irsa.query_region_async(coord, radius=search_radius, catalog='fp_psc').to_pandas()

		elif survey == 'GAIA':
			temp = Gaia.query_object_async(coord, radius=search_radius).to_pandas()

		else:
			print('Invalid Survey')

		catalog = SkyCoord(ra=temp.ra, dec=temp.dec, unit=(u.deg, u.deg))

		i, _, _ = match_coordinates_sky(coord, catalog)

		for feature in features:
			series.at[idx, feature] = temp.at[int(i), feature]

	except Exception as e:
		print(e)
