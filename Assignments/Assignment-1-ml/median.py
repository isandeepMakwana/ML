import numpy
a = numpy.matrix(((10,20,30,40,50),(10,20,30,40,50),(10,20,30,40,50)))
print(numpy.median(a,axis=1))
print(numpy.median(a,axis=0))

