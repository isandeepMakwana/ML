import matplotlib.pyplot
import numpy
a=numpy.random.randint(20,100,size=[2,4])
a=numpy.matrix(a)
print(a)
matplotlib.pyplot.hist(a,10)
matplotlib.pyplot.show()


matplotlib.pyplot.hist(a.transpose(),10)
matplotlib.pyplot.show()