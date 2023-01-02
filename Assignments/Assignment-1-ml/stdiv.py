import numpy
import statistics
a = numpy.matrix(((10,2,40,35),(10,2,40,35),(10,2,40,35),(10,2,40,35)))

b = numpy.matrix([[statistics.stdev(i)] for i in a.tolist()])
print(type(b))
print(b)

c = numpy.matrix([statistics.stdev(i) for i in a.transpose().tolist()])
print(type(c))
print(c)