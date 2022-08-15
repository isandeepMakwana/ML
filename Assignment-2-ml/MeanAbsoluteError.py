#MAE
import numpy
a=[100,200,300,100,200,300,400,500,300,700,800,900,1000,800]
p=[100,150,300,100,199,300,400,450,300,700,800,800,900,1000]

diff_list = [abs(a[i]-p[i]) for i in range(len(a))]
mae=numpy.sum(diff_list)/len(a)
print(mae)
