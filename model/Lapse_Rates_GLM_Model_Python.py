# This program will clean and analyze using a GLM to predict lapse rates using mortgage rates, 1 year CD rates, Treasury Yields, and HYSA 

# Collaborators: Tanna Henry, Alejandro Ordonez, Simon Zheng

import math
import numpy as np
import pandas as pd
import sklearn as sk 

# We will take the url in our github for the raw csv files
url = "https://raw.githubusercontent.com/ajordonez/Lapse_Rate_GLM_Model/refs/heads/main/data/Uncleaned_Predictive_Analytics.csv"

# We will use pandas to turn this data into a dataframe
df = pd.read_csv(url)

# Print head of data
print("New Line\n")
print(df.head())


# We need to clean the data of blanks and ND

print(df.columns)

df = df.dropna()


