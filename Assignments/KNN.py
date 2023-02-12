import matplotlib.pyplot
import statistics
import math
import numpy


class KNN:
    def __init__(self):
        self.someThingRelatedToClassificationAndRegrasion = (
            False  # False -> classification , True Regrasion
        )
        self.datasets = None
        self.datasetColors = None
        self.query = None
        self.queryMarker = None
        self.querySize = None
        self._distanceList = []

    def process(self):
        if self.datasets == None:
            raise ValueError("Dataset must required !!!!")
        if self.query == None:
            raise ValueError("query must required !!!!")

        for i in range(len(self.datasets)):
            for p in self.datasets[i]:
                sumOfSquares = 0
                qi = 0
                ep = len(self.query) - 2
                while qi <= ep:
                    qd = (p[qi] - self.query[qi]) ** 2
                    sumOfSquares += qd
                    qi += 1
                distance = math.sqrt(sumOfSquares)
                self._distanceList.append((self.datasetColors[i][0], distance))
        self._distanceList.sort(key=lambda x: x[1])
        # print(self._distanceList)

        kFactor = int(math.sqrt(len(self._distanceList)))
        if kFactor % len(self.datasetColors) == 0:
            kFactor += 1
        if kFactor % 2 == 0:
            kFactor += 1
        kElements = self._distanceList[:kFactor]
        classes = [x[0] for x in kElements]
        print(statistics.mode(classes))
        return statistics.mode(classes)

    def show(self):
        if self.querySize == None:
            self.querySize = 20
        if self.queryMarker == None:
            self.queryMarker = "o"
        matplotlib.pyplot.plot(
            0,
            0,
            color=self.query[len(self.query) - 1],
            marker=self.queryMarker,
            markersize=self.querySize,
            label="target",
        )
        dct = {}
        for i in self._distanceList:
            if i[0] not in dct.keys():
                dct[i[0]] = []
            dct[i[0]].append(i[1])
        print(dct)
        colorDict = {}
        for i in self.datasetColors:
            if i[0] not in colorDict.keys():
                colorDict[i[0]] = i[1]
        print(colorDict)
        k = 1
        for i, j in dct.items():
            matplotlib.pyplot.scatter(
                j, list(range(k, len(j) + k)), label=i, c=colorDict[i]
            )
            k += len(j)
        matplotlib.pyplot.legend()
        matplotlib.pyplot.grid(True)
        matplotlib.pyplot.show()


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


k = KNN()
k.someThingRelatedToClassificationAndRegrasion = False
k.datasets = (a, b)
k.datasetColors = (("A", "r"), ("B", "g"))
k.query = (80, 100, "b")
k.queryMarker = "o"
k.querySize = 20
k.process()
k.show()
