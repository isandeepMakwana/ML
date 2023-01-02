import numpy
import matplotlib.pyplot
data = numpy.matrix(((10,20,30),(30,50,60)))
x = numpy.array(([0, 4, 5],[1,2,3]))
matplotlib.pyplot.plot(x, data)
matplotlib.pyplot.show()
