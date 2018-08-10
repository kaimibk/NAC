from plotly.plotly import image, iplot
from os.path import exists
from time import time
from IPython.display import Image

def save_fig(figure, filename, out_directory='', dynamic=False, scale=None):
	"""
	Renders and saves plotly figures
	Parameters
	----------
	figure : plotly figure object
		plotly figure to render
	filename : str
		Name to save figure as
	out_directory : str
		Location to store the figure
	dynamic : bool
		Return dynamic (True) or static (False)
	scale : int
		Increase the resolution of saved image by 'scale'
	Returns
	-------
	Dynamic or static image based on user request
	"""
	path = "{0}{1}".format(out_directory, filename)

	if not exists("{}.png".format(path)):
		name = "{}.png".format(path)
		image.save_as(figure, name, scale=scale)

	else:
		name = "{}_{}.png".format(path, int(time()))
		image.save_as(figure, name, scale=scale)

	if dynamic == True:
		return iplot(figure, filename=filename)

	elif dynamic == False:
		return Image("{}".format(name))
	else:
		print("Invalid entry")
