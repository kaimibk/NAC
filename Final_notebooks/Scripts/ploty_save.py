from plotly.plotly import image, iplot
from IPython.display import Image


def save_fig(figure, filename, out_directory=''):
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
	Returns
	-------
	Dynamic or static image based on user request
	"""
	image.save_as(figure, "{0}{1}.png".format(out_directory, filename))

	request = input("Enter 0 for dynamic or  1 for static image...")

	if request == str(0):
		iplot(figure, filename=filename)
	elif request == str(1):
		Image("{0}{1}.png".format(out_directory, filename))
	else:
		print("Invalid entry")
