import numpy
import matplotlib.pyplot
data=numpy.matrix(((10,20,30,40),(15,25,35,45)))
print('data\n',data)
matplotlib.pyplot.plot(data)
matplotlib.pyplot.show()


data=numpy.matrix(((10,20,30,40),(15,25,35,50)))
print('data\n',data)
print('row wasie show')
matplotlib.pyplot.plot(data.transpose())
matplotlib.pyplot.show()