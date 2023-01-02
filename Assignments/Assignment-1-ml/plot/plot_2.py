import matplotlib.pyplot
import numpy
data = numpy.matrix(((10,20,30,5,60)))
matplotlib.pyplot.plot(data.tolist()[0])
matplotlib.pyplot.show()