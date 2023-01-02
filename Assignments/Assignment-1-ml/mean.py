import statistics
import numpy

a = numpy.matrix(((10,20,30,40,50),(10,20,30,40,50),(10,20,30,40,50)))

# print(statistics.mean(a))
print(numpy.mean(a,axis=1))
print(numpy.mean(a,axis=0))
