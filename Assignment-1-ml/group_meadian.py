import numpy
import statistics
a = [100,200,300,100,200,300,400,500,300,700,800,900,1000,800]
print(statistics.median_grouped(a))
a = numpy.matrix(((100,200,300,100,200,300,400,500,300,700,800,900,1000,800),(100,200,300,100,200,300,400,500,300,700,800,900,1000,800)))

b = numpy.matrix([[statistics.median_grouped(i)] for i in a.tolist()])
print(type(b))
print(b)


c = numpy.matrix([statistics.median_grouped(i) for i in a.transpose().tolist()])
print(type(c))
print(c)
