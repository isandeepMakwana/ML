import numpy
import statistics
a=numpy.matrix(((30,20,30,30,20,30,10,30,30,10,20,20,20,10,30),(30,20,30,30,20,30,10,30,30,10,20,20,20,10,30),(30,20,30,30,20,30,10,30,30,10,20,20,20,10,30)))
b = numpy.matrix([statistics.mode(i) for i in a.transpose().tolist()])
print(type(b))
print(b)


c = numpy.matrix([[statistics.mode(i)] for i in a.tolist()])
print(type(c))
print(c)
