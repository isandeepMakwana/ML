# Natural Language Processing

import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# Cleaning text
import re
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
corpus = []

for i in range(0, 1000):    
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # including only alphabets
    review = review.lower() # changing alphabets to the lowercaste
    review = review.split() # converting text into list of each word
    ps = PorterStemmer() # creating PorterStemmer object
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] 
    # forming a list of words which do not contain any non usable words and replacing each word with its root word
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)  
X = cv.fit_transform(corpus).toarray() # Creating a sparse matrix of words in to columns and reviews in the column
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .20, random_state = 0)

# Fitting Classifier to the Training set 
#from sklearn.naive_bayes import GaussianNB
#classifier = GaussianNB()
#classifier.fit(X_train, y_train)

# Fitting Classifier to the Training set 
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(X_train, y_train)

# Predicting the results with Logistic regression model
y_pred = classifier.predict(X_test)

# Creating a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Checking the performance of the model
classifier.score(X_test, y_test)