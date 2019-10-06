from openpyxl import load_workbook
import matplotlib.pyplot as plot
import numpy as np
from datetime import date

# function to fetch workbook data and return sanitized dictionary
def getExcelData(filePath = 'Sample Data.xlsx'):
	# load the file
	revenue = load_workbook(filename = filePath, read_only=True)
	# we only need the first worksheet
	workSheet = revenue.get_sheet_by_name(revenue.sheetnames[0])
	data = {'revenue': {}, 'regions': []}
	products = None
	# loop through rows
	for r in workSheet.iter_rows():
		# r is a tuple of ReadOnlyCell objects
		# (Region, Detergent, Cooking Oil, Sugar, Cereal, Total)
		regionName = str(r[0].value)
		# Skip header row
		if regionName == 'REGION':
			# get the product names
			products = r[1].value, r[2].value, r[3].value, r[4].value
			continue
		# add region name to regions
		data['regions'].append(regionName)
		# add product to dictionary
		for i, p in enumerate(products):
			if p not in data['revenue']:
				data['revenue'][p] = []
			# add the product revenue of current region to the list for this product
			data['revenue'][p].append(r[i + 1].value)
	# we should have all the revenue data now
	return data

# function to plot a compound bar graph of all regions on x and product revenues on Y for the totals
def plotRevCBG(revenueDB):
	# get the region names
	regions = revenueDB['regions']
	# get the product names
	products = list(revenueDB['revenue'].keys())
	# sort the names
	products.sort()
	# number of x elements
	N = len(regions)
	# get the locations for the x-axis
	locs = np.arange(N)
	# width of bars
	width = 0.35
	largest = 0
	# plot basics
	plot.ylabel('Sales Revenue (KES)')
	plot.title('Monthly sales revenue for Foo Traders by Region and Product')
	xticks = regions
	plot.xticks(locs, xticks)
	# for stacking
	subPlots = []
	plotLayers = []
	# generate each layer of the stack, which is a simple bar plot of product revenue by region
	# =========================================================================================
	for row, product in enumerate(products):
		# get the value list
		plotLayer = tuple(revenueDB['revenue'][product])
		if row == 0:
			# this is the first one
			subPlot = plot.bar(locs, plotLayer, width)
		else:
			# put the sum of previous data as its floor
			floorValues = [sum(x) for x in zip(*plotLayers)]
			subPlot = plot.bar(locs, plotLayer, width, bottom=floorValues)
		# add values to plotLayers
		plotLayers.append(plotLayer)
		# add to the list
		subPlots.append(subPlot)
		# update the legend
		plot.legend(tuple([p[0] for p in subPlots]), tuple([n for n in products[:row + 1]]))
		# we can display the plot to show how it is progressing
		#plot.show()
	# =========================================================================================
	# show the plot
	plot.show()

if __name__ == '__main__':
	# get the file path from user
	#filePath = raw_input("Please enter the path to the Excel file: ")
	# get the data
	revenueData = getExcelData()
	# plot a compound bar graph
	plotRevCBG(revenueData)
	