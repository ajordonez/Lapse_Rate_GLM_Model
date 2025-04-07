# This program will clean and analyze using a GLM to predict lapse rates using mortgage rates, 1 year CD rates, Treasury Yields, and HYSA 

# Collaborators: Tanna Henry, Alejandro Ordonez, Simon Zheng

import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


# We will take the url in our github for the raw csv files
url = "https://raw.githubusercontent.com/ajordonez/Lapse_Rate_GLM_Model/refs/heads/main/data/Uncleaned_Predictive_Analytics.csv"

# We will use pandas to turn this data into a dataframe
df = pd.read_csv(url)



# We need to clean the data of blanks and ND 

df.replace("ND", np.nan, inplace=True)
df = df.iloc[:,0:8]
df = df.dropna()
print(df)


'''
# The following will show how we intend to use the data provided to make a GLM using either Poisson or Negative Binomial distribution

# Preparing the data

X = df[['predictor1', 'predictor2']]
y = df['binary_outcome']
# Adding a constant to the predictor variable set
X = sm.add_constant(X)
# Logistic Regression model
model = sm.GLM(y, X, family=sm.families.NegativeBinomial()).fit()
# or 
# Poisson Regression model
model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

# Model summary
print(model.summary())


# For testing if the model works try the below methods for a poisson model

# Calculate deviance
deviance = model.deviance
print(f"Deviance: {deviance}")


'''