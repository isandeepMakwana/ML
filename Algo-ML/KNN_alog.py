import statistics
import math
import matplotlib.pyplot
import numpy

"""
#following Represents  A Class
matplotlib.pyplot.plot(10,20,"ro")
matplotlib.pyplot.plot(20,25,"ro")
matplotlib.pyplot.plot(15,20,"ro")
matplotlib.pyplot.plot(30,45,"ro")
matplotlib.pyplot.plot(10,10,"ro")
matplotlib.pyplot.plot(50,25,"ro")
matplotlib.pyplot.plot(30,55,"ro")
matplotlib.pyplot.plot(40,60,"ro")
#following Represents  B Class
matplotlib.pyplot.plot(100,120,"go")
matplotlib.pyplot.plot(120,125,"go")
matplotlib.pyplot.plot(115,120,"go")
matplotlib.pyplot.plot(130,145,"go")
matplotlib.pyplot.plot(100,100,"go")
matplotlib.pyplot.plot(150,125,"go")
matplotlib.pyplot.plot(130,155,"go")
matplotlib.pyplot.plot(140,160,"go")


# create a Black
queryX = 80
queryY = 100
matplotlib.pyplot.plot(queryX , queryY ,color="b" , marker ="o" , markersize=20)
"""
# KNN - ALGO - CODE


a = numpy.array(
    [
        [10, 20],
        [20, 25],
        [15, 20],
        [30, 45],
        [10, 10],
        [50, 25],
        [30, 55],
        [40, 60],
    ]
)
b = numpy.array(
    [
        [100, 120],
        [120, 125],
        [115, 120],
        [130, 145],
        [100, 100],
        [150, 125],
        [130, 155],
        [140, 160],
    ]
)

# but we need all the x an y on onle two [[],[]]

# what we can do transpose a and b

x, y = a.T

print(x)
matplotlib.pyplot.scatter(x, y, color="r")
x, y = b.T
print(y)
matplotlib.pyplot.scatter(x, y, color="g")

matplotlib.pyplot.grid(True)
queryX = 60
queryY = 100
matplotlib.pyplot.plot(queryX, queryY, color="b", marker="o", markersize=20)

# matplotlib.pyplot.show()

# KNN Alogrithm starts hear


distanceList = []
for p in a:
    xd = abs(p[0] - queryX)
    yd = abs(p[1] - queryY)
    d = math.sqrt(xd**2 + yd**2)
    distanceList.append(("A", int(d), p))


for p in b:
    xd = abs(p[0] - queryX)
    yd = abs(p[1] - queryY)
    d = math.sqrt(xd**2 + yd**2)
    distanceList.append(("B", int(d), p))


print("*" * 50)
print(distanceList)

distanceList.sort(key=lambda x: x[1])

print("*" * 50)
kFactor = int(math.sqrt(len(a) + len(b)))

if kFactor % 2 == 0:
    kFactor += 1
print("kFactor : ", kFactor)
kElementFromTop = distanceList[:kFactor]
print(kElementFromTop)
new_lst = []
for i in kElementFromTop:
    c = "g"
    c = "r" if i[0] == "A" else "g"
    matplotlib.pyplot.plot([i[2][0], queryX], [i[2][1], queryY], color=c)
# matplotlib.pyplot.plot(queryX, queryY, color="b", marker="o", markersize=20)
classes = [x[0] for x in kElementFromTop]
print(classes)
identifiedClass = statistics.mode(classes)
print(f"{queryX} , {queryY} belongs to {identifiedClass}")


matplotlib.pyplot.show()
