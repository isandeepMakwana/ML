# Artificial Neural Network

# Install theano, tenserflow and keras using:> conda install -c conda-forge "package-name"

# Part 1 - Data Preprocessing

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values  # Independent Variable(Input)
y = dataset.iloc[:, 13].values  # Dependent Variable(Output)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
ct = ColumnTransformer([('onehotencoder', OneHotEncoder(categories='auto'), [1])],  # The column numbers to be transformed (here is [1] but can be [0, 1, 3])
                       remainder='passthrough'                           # Leave the rest of the columns untouched
                       )
X = ct.fit_transform(X)
X = X[:, 1:] # Preventing dummy variable trap

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Part 2 - Now let's make the ANN

# Importing the Keras libraries and packages
import keras 
from keras.models import Sequential # Initialise neural network
from keras.layers import Dense # Used to create layers in ANN

# Initialising the ANN
classifier = Sequential() # Main structure

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11)) # Adding sections/parts to the main structure

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, activation = 'sigmoid', kernel_initializer = 'uniform'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Part 3 - Making the predictions and evaluating the model

# Predicting the test results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > .5)
 
# Creating a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
