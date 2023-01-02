import numpy
import statistics
a=numpy.matrix(((10,20,30,5,7),(10,20,30,5,7),(10,20,30,5,7)))
#row
print(numpy.cumsum(a,axis=1))

#c
print(numpy.cumsum(a,axis=0))
