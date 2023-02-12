# Thompson Sampling

# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing the UCB algorithm 
import random
N = 10000
d = 10
ad_selected = []
num_of_rewards_1 = [0] * d
num_of_rewards_0 = [0] * d
total_rewards = 0

for n in range(0, N):
    max_random = 0
    ad = 0
    for i in range(0, d):
        random_beta = random.betavariate(num_of_rewards_1[i] + 1, num_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ad_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        num_of_rewards_1[ad] += 1
    else:
        num_of_rewards_0[ad] += 1
    total_rewards += reward

# Visualising the results
plt.hist(ad_selected)
plt.xlabel('Ads')
plt.ylabel('Numbers of times ad selected')
plt.title('Histogram of ads selection')
plt.show()
    