# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing Dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values # Independent Variable(Input)
y = dataset.iloc[:, 4].values # Dependent Variable(Output)


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # LabelEncoder for encoding categorical variables into numbers & OneHotEncoder for dummy encoding
from sklearn.compose import ColumnTransformer
# label encoder for x(input/independent variables)
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
# OneHotEncoder for categorical feature for creating dummies

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [3])],   # The column numbers to be transformed (here is [3] but can be [0, 1, 3])
    remainder='passthrough'                                         # Leave the rest of the columns untouched
)
X = ct.fit_transform(X)

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) # regressor learned correlations of the train set


# Predicting the Test set results
y_pred = regressor.predict(X_test)


# Building the optimal model using Backward Elimination
import statsmodels.regression.linear_model as sm
X = np.append(arr=np.ones((50,1)).astype(int), values=X, axis=1)


# Doing backward elimination in steps using OLS
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 1, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


# Using function
def backwardElimination(x, sl):
    numVars = len(x[0])
    
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(endog=y, exog=x).fit() # endog :- The dependent variable, exog :- Independent variables with intercept included by the user
        maxVar = max(regressor_OLS.pvalues).astype(float)
        prev_rsq_adj = 0
        if maxVar > sl: # p values greater than significant level
            for j in range(0, numVars - i):
                if ((regressor_OLS.pvalues[j]).astype(float) == maxVar) and (regressor_OLS.rsquared_adj > prev_rsq_adj):
                    prev_rsq_adj = regressor_OLS.rsquared_adj
                    x = np.delete(x, j, 1)

    print(regressor_OLS.summary())
    return x

# with adj R sq
def backwardElimination(x, SL): 
    numVars = len(x[0])  # number of columns 
    temp = np.zeros((50,6)).astype(int) # creating an empty matrix of size (50, 6)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()  # fitting the model with OLS regressor 
        maxVar = max(regressor_OLS.pvalues).astype(float)  # finding max p-value
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:, j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
                    
    regressor_OLS.summary()
    return x 

SL = 0.05
X_opt = X[:, [0,1,2,3,4,5]] # Optimal matrix feature
X_opt = np.array(X_opt, dtype=float)
X_Modeled = backwardElimination(X_opt, SL)


# Custom test set
single_observation = pd.DataFrame(R.D.Spend = 10000, Administrator = 20000, Marketing.Spend = 30000)
y_predC = predict(regressor, newdata=single_observation)