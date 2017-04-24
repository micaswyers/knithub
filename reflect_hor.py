# Takes a CSV knitting chart and does a horizontal reflection

f = open('filename.csv', 'r') # Insert CSV filename here
for line in f:
	cells = line.strip().split(',')
	cells = cells[::1]
	print ",".join(cells)
