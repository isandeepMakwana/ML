import numpy
import statistics

a = numpy.matrix(((10,20,30,40,50),(10,20,30,40,50),(10,20,30,40,50)))

b = numpy.matrix([statistics.harmonic_mean(i) for i in a.transpose().tolist()])
print(type(b))
print(b)



c = numpy.matrix([[statistics.harmonic_mean(i)] for i in a.tolist()])
print(type(c))
print(c)
