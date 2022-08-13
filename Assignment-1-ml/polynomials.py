import numpy
coefficent = numpy.matrix(((2,3,4,5,10),(2,3,4,5,10),(2,3,4,5,10)))
p = [numpy.poly1d(i) for i in coefficent.tolist()]
for i in p:print(i)