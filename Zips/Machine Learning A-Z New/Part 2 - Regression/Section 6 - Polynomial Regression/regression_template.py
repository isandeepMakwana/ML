# Polynomial regression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values  # Independent Variable(Input)
y = dataset.iloc[:, 2].values  # Dependent Variable(Output)

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""

# Fitting the Regression to the dataset
# Create Your regressor here

# Predicting new results with Polynomial Regression Model
y_pred = regressor.predict([[6.5]])

# Visualizing the Regression results
plt.scatter(X, y, color='red') # Plotting the points from the data
plt.plot(X, regressor.predict(X_grid), color='blue') # Plotting the regression curve
plt.title('Truth or Bluff (Regression Models)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1)) # Inputing custom dataset
plt.scatter(X, y, color='red') # Plotting the points from the data
plt.plot(X_grid, regressor.predict(X_grid), color='blue') # Plotting the regression curve
plt.title('Truth or Bluff (Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
