from pycinema import getColumnFromTable, imageFromMatplotlibFigure, isNumber
import matplotlib.pyplot as plt
import numpy as np

#
# This creates two plots of car data from data:
# https://data.wa.gov/api/views/f6w7-q2d2/rows.csv
#

# use offscreen backend
import matplotlib as mpl
mpl.use('Agg')

outputs = []

for cols, mark in zip([["Model Year", "Electric Range"], ["Model Year", "DOL Vehicle ID"]], ['x', 'o']):

    figure = plt.figure(figsize=(10,8), dpi=200)
    x = getColumnFromTable(inputs, cols[0])
    xvals = np.asarray(x, dtype='int')

    y = getColumnFromTable(inputs, cols[1])
    index = 0
    for v in y:
        if not isNumber(v): 
            # set a default value
            y[index] = 0
        index += 1

    yvals = np.asarray(y, dtype='int')

    plt.scatter(xvals, yvals, marker=mark)
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.title(cols[1] + " vs. " + cols[0])

    outputs.append( imageFromMatplotlibFigure(figure, 200) )

plt.close(figure)

