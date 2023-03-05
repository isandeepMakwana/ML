import sklearn.datasets
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.neighbors
# load iris data
iris_datasets = sklearn.datasets.load_iris()
features_dataset = iris_datasets.data[:,:2]
target_dataset = iris_datasets.target
print("features dataset : ")
print(features_dataset)
print("target dataset :  ")
print(target_dataset)

# test and train the dataset

# featureTrainingData , featureTestData = sklearn.model_selection.train_test_split(features_dataset , test_size=0.20) # randome ly split karta hi but target but same split karna hoga 

featureTrainingData , featureTestData , targetTrainingData , targetTestData = sklearn.model_selection.train_test_split(features_dataset , target_dataset,test_size=0.25) #if test_size == 0.25 then 25% test data

print("feature Training Data ")
print(featureTrainingData)
print("feature Test Data ")
print(featureTestData)
print(len(featureTrainingData),len(featureTestData))
print("taget Training Data ")
print(targetTrainingData)
print("target Test data")
print(targetTestData)
print(len(targetTrainingData),len(targetTestData))

# need a scalling

scaler = sklearn.preprocessing.StandardScaler().fit(featureTrainingData)
fetureTrainingData = scaler.transform(featureTrainingData)
featureTestData = scaler.transform(featureTestData)

print("scalled feature Traing data") 
print(featureTrainingData)
print("scaled festure test data")
print(featureTestData)

# pass to knn 
knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(featureTrainingData, targetTrainingData)
result = knn.predict(featureTestData)
print("The Result ")
print(result)
print("acturals")
print(targetTestData)

