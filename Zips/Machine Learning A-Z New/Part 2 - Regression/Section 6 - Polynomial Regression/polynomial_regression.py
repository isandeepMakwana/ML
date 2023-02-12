# Polynomial regression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values  # Independent Variable(Input)
y = dataset.iloc[:, 2].values  # Dependent Variable(Output)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # degreee shows the degree of the polynomial equation
X_poly = poly_reg.fit_transform(X) # Transforms the matrix of feature x into new matrix of feature called new poly
    # Creating Polynomial regressor
poly_reg.fit(X_poly, y) # Training the polynomial regression model with respected inputs and outputs

lin_reg2 = LinearRegression() # Include the fit of the poly_reg object into linear regression model
lin_reg2.fit(X_poly, y)

# Plotting the linear Regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Plotting the Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1)) # Inputing custom dataset
plt.scatter(X, y, color='red') # Plotting the points from the data
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='blue') # Plotting the regression curve
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting new results with Linear Regression Model
lin_reg.predict(np.array(6.5).reshape(1, -1)) # predicting salary for level 6.5

# Predicting new results with Polynomial Regression Model
lin_reg2.predict(poly_reg.fit_transform(np.array(6.5).reshape(1, -1))) # predicting salary for level 6.5