#RMSE
import numpy
a=[2, 3, 5, 5, 9]
p=[3, 3, 8, 7, 6]
diff_list = numpy.subtract(a,p)
squred_diff=numpy.square(diff_list)
mse = numpy.sum(squred_diff)/len(a)
print(numpy.sqrt(mse))