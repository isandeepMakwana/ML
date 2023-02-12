# Assignment genric with other example
import math
import matplotlib.pyplot  # not able to display other examples
import numpy
import statistics


def ClassifyByKNN(*args):
    if len(args) - 2 != len(args[len(args) - 1]):
        raise ValueError(f"{args}\n error: due to your datasets and identified classes not equal !!!!!!")
    classesAndColors = args[len(args) - 1]
    query = args[len(args) - 2]
    distanceList = []
    try:
        for i in range(len(args) - 2):
            for p in args[i]:
                sum_ = 0
                for pi in range(len(p)):
                    val = abs(p[pi] - query[pi])
                    val = val**2
                    sum_ += val
                distance = math.sqrt(sum_)
                distanceList.append((classesAndColors[i][0], distance))
    except:
        raise IndexError("error: due to query and dataset fetures not equal !!!!!!")
    print(distanceList)
    distanceList.sort(key=lambda x: x[1])
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


# ex1:


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

print("==" * 50)

# ex2:

# Student marks hindi , english , maths, computer
excellent_students = [
    (54, 94, 95, 75),
    (37, 57, 91, 56),
    (64, 76, 82, 72),
    (48, 52, 92, 67),
    (50, 72, 83, 57),
    (63, 89, 89, 37),
    (34, 85, 49, 46),
    (52, 35, 93, 66),
]
average_students = [
    (62, 68, 42, 64),
    (60, 52, 61, 44),
    (75, 42, 54, 73),
    (76, 52, 68, 39),
    (73, 60, 44, 47),
    (90, 64, 67, 34),
]
ok_students = [
    (30, 79, 46, 65),
    (25, 90, 47, 39),
    (36, 82, 78, 14),
    (32, 40, 69, 61),
    (53, 95, 87, 5),
    (58, 91, 79, 20),
    (36, 55, 99, 4),
    (46, 85, 80, 1),
    (61, 82, 84, 9),
    (33, 65, 49, 31),
    (70, 97, 75, 9),
    (44, 66, 74, 14),
    (38, 57, 54, 30),
    (43, 91, 5, 50),
    (30, 71, 37, 19),
    (54, 25, 64, 51),
    (54, 32, 29, 67),
    (96, 79, 66, 17),
    (54, 37, 67, 14),
    (70, 92, 3, 37),
    (88, 67, 51, 30),
    (78, 56, 22, 56),
    (42, 38, 24, 33),
    (79, 42, 38, 42),
    (38, 49, 5, 25),
    (79, 70, 37, 10),
    (78, 65, 11, 33),
    (40, 43, 3, 23),
    (56, 27, 31, 25),
    (71, 63, 25, 6),
    (73, 56, 29, 8),
    (40, 27, 18, 12),
    (72, 70, 5, 8),
    (86, 29, 25, 37),
    (50, 26, 15, 10),
    (83, 27, 9, 12),
]

c = ClassifyByKNN(excellent_students,average_students,ok_students,(56, 82, 51, 40, "b"),(("excellence", "r"), ("average", "g"), ("ok", "k")))
print(f"(56,82,51,40) belongs to {c}")


print("==" * 50)

# ex3:

study_hour = [3, 4, 5, 4, 5, 6, 2]
IQ = [100, 20, 40, 140, 40, 10, 20]
gfg_quetion_solved = [10, 20, 15, 5, 15, 15, 15]
package = [500000, 400000, 750000, 850000, 700000, 650000, 450000]

table = numpy.matrix((study_hour, IQ, gfg_quetion_solved, package)).T
print(table)

# Mean Normalization
# x-mean(set(x))/max(set(x))-min(set(x))

mean_arr = numpy.mean(table, axis=0)
max_arr = numpy.max(table, axis=0)
min_arr = numpy.min(table, axis=0)
print(mean_arr)
print(max_arr)
print(min_arr)


def get_mean_normalization(a):
    return [(a[x] - mean_arr[x]) / (max_arr[x] - min_arr[x]) for x in range(len(a))]


# mat=numpy.apply_along_axis(lambda a:[(a[x]-mean_arr[x])/(max_arr[x]-min_arr[x]) for x in range(len(a))],1,table)
mat = numpy.apply_along_axis(get_mean_normalization, 1, table)
scaled_table = numpy.matrix(mat)

lst = scaled_table.tolist()
happy = []
unhappy = []
for i in range(len(lst) - 1):
    if i in [2, 4]:unhappy.append(lst[i])
    else:happy.append(lst[i])

query_fetures = lst[-1]
print(query_fetures)
c = ClassifyByKNN(happy, unhappy, tuple(query_fetures), (("happy", "r"), ("unhappy", "g")))
print(f"(2,20,15,450000) belongs to {c}")
