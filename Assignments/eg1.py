# import matplotlib.pyplot as plot
# import numpy

# plot.plot(numpy.array([10, 20]).T, numpy.array([100, 120]).T, color="r", marker="o")
# plot.show()


# def abcd(*x):
#     print(x)

# abcd(10,20,"hello",(1,2,3,4),[1,2,3,4])


import statistics
import math
import numpy
import matplotlib.pyplot


def ClassifyByKNN(*args):
    print(args)
    # I am not applying validations
    classesAndColors = args[len(args) - 1]
    # print('classes and colors ',ClassesAndColors)
    queryX = args[len(args) - 2][0]
    queryY = args[len(args) - 2][1]
    for i in range(len(args) - 2):
        x, y = args[i].T
        matplotlib.pyplot.scatter(x, y, color=classesAndColors[i][1])
    matplotlib.pyplot.plot(
        queryX, queryY, color=args[len(args) - 2][2], marker="o", markersize=20
    )
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.show()

    distanceList = []
    for i in range(len(args) - 2):
        for p in args[i]:
            xd = abs(p[0] - queryX)
            yd = abs(p[i] - queryY)
            distance = math.sqrt(xd**2 + yd**2)
            distanceList.append((classesAndColors[i][0], distance))
    print(distanceList)
    distanceList.sort(key=lambda x: x[1])
    print("*" * 50)
    print(distanceList)
    kFactor = int(math.sqrt(len(distanceList)))
    if kFactor % len(classesAndColors) == 0:
        kFactor += 1
    if kFactor % 2 == 0:
        kFactor += 1
    kElements = distanceList[:kFactor]
    print("*" * 50)
    print(kElements)
    classes = [x[0] for x in kElements]
    return statistics.mode(classes)


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

c = ClassifyByKNN(a, b, (80, 100, "b"), (("A", "r"), ("B", "g")))
print(f"(80,100) belongs to {c}")
