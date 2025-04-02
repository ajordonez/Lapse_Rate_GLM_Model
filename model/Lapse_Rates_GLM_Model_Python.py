# This program will clean and analyze using a GLM to predict lapse rates using mortgage rates, 1 year CD rates, Treasury Yields, and HYSA 

# Collaborators: Tanna Henry, Alejandro Ordonez, Simon Zheng

import math
import numpy as np
import pandas as pd
import sklearn as sk


file = pd.read_csv("/Users/alexordonez/Documents/Uncleaned_Predictive_Analytics.csv")

df = pd.DataFrame(file)

print(df.head())