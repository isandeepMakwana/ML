# Eclat

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  Importing the dataset 
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None )
transactions = [[str(dataset.values[i,j]) for j in range(0, dataset.shape[1]) 
                 if str(dataset.values[i,j]) != 'nan'] for i in range(0, dataset.shape[0])]

# Generate a list of unique items in the transactions
items = list()
for t in transactions:
    for x in t:
        if (not x in items):
            items.append(x)
            
# Generate a list of pairs of items with relevant support value 
# [[(item_a, item_b) , support_value]] 
# support_value is initialized to 0 for all pairs 
eclat = list() 
for i in range(0, len(items)):
    for j in range(i+1, len(items)):
        eclat.append([(items[i],items[j]),0])

# Compute support value for each pair by looking for transactions with both items
for p in eclat:
    for t in transactions:
        if(p[0][0] in t) and (p[0][1] in t):
            p[1] += 1
            p[1] = p[1]/len(transactions)
            
# Converts eclat in sorted DataFrame to be visualized in variable explorer
eclatDataFrame = pd.DataFrame(eclat, columns = ['rule','support']).sort_values(by = 'support', ascending = False)