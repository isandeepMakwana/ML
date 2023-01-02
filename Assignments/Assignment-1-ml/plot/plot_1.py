import numpy
import matplotlib.pyplot
a=numpy.matrix(numpy.random.randint(50,size=[10,2]))
b=numpy.matrix(numpy.random.randint(50,size=[10,2]))
print(type(a))
matplotlib.pyplot.plot(a,b)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(a.transpose(),b.transpose())
matplotlib.pyplot.show()