import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import base64

matplotlib.style.use('fivethirtyeight')


####### DEFINE THE CSV TO READ FROM ########
df = pd.read_csv(raw_input('enter dataset: '))

####### GET COLUMNS #########
columns = list(df.columns.values)
print "columns in dataframe: " + str(columns)


print "available plot types ['bar', 'box', 'pie', 'scatter']"

# dfplot = df.plot()
# fig = dfplot.get_figure()
# fig.savefig('output.png')

# dfplot = df.plot.box()
# fig = dfplot.get_figure()
# fig.savefig('outputbox.png')

# ####### GET AXISES ###########
# given_x = raw_input("column to plot on x: ")
# given_y = raw_input("column to plot on y: ")

# dfplot = df.plot(kind='scatter',x=given_x, y=given_y)
# fig = dfplot.get_figure()
# fig.savefig('outputscatter.png')


def make_pie( df, column ):
	counts = pd.DataFrame(df[column].value_counts())

	plot = counts.plot.pie(y=column)
	fig = plot.get_figure()
	fig.savefig('output.png')
	plt.show()

def make_bar( df, column ):
	counts = pd.DataFrame(df[column].value_counts())

	plot = counts.plot.bar(y=column)
	fig = plot.get_figure()
	fig.savefig('output.png')
	plt.show()

def make_scatter( df, x_axis, y_axis):
	dfplot = df.plot.scatter(x=x_axis, y=y_axis)
	fig = dfplot.get_figure()
	fig.savefig('output.png')	
	plt.show()

def make_box( df, column ):
	if column not in df:
		plot = df.plot.box()
	else:
		plot = df.plot.box(y=column)

	fig = plot.get_figure()
	fig.savefig('output.png')
	plt.show()

while True:
	kind = raw_input("What type of chart do you want?: ")

	if kind == 'pie':
		make_pie(df, raw_input("What column do you want to chart?: "))
	elif kind == 'bar':
		make_pie(df, raw_input("What column do you want to chart?: "))
	elif kind == 'box':
		make_box(df, raw_input("What column do you want to chart?: "))
	elif kind == 'scatter':
		make_scatter(df, raw_input("What should the x-axis be?: "), raw_input("What should the y-axis be?: "))

	print base64.b64encode(open("output.png", "rb").read())

	print "\n\n"

