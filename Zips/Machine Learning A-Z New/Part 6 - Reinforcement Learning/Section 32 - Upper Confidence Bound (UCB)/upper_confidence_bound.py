# Upper Confidence Bound

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing the UCB algorithm 
import math
N = 10000
d = 10
ad_selected = []
num_of_selections = [0] * d
sum_of_rewards = [0] * d
total_rewards = 0

for n in range(0, N):
    max_upper_bound = 0
    ad = 0
    for i in range(0, d):
        if num_of_selections[i] > 0:
            avg_reward = sum_of_rewards[i] / num_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / num_of_selections[i]) # delta_i(n)
            upper_bound = avg_reward + delta_i 
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ad_selected.append(ad)
    num_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sum_of_rewards[ad] += reward
    total_rewards += reward
    
# Visualising the results
plt.hist(ad_selected)
plt.xlabel('Ads')
plt.ylabel('Numbers of times ad selected')
plt.title('Histogram of ads selection')
plt.show()
