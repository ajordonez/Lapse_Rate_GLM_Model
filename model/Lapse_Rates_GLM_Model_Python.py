# This program will clean and analyze using a GLM to predict lapse rates using mortgage rates, 1 year CD rates, Treasury Yields, and HYSA 

# Collaborators: Tanna Henry, Alejandro Ordonez, Simon Zheng

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


# We will take the url in our github for the raw csv files
url_1 = "https://raw.githubusercontent.com/ajordonez/Lapse_Rate_GLM_Model/refs/heads/main/data/Uncleaned_Predictive_Analytics.csv"

url_2 = "https://raw.githubusercontent.com/ajordonez/Lapse_Rate_GLM_Model/refs/heads/main/data/Historical_GDP.csv"

# We will use pandas to turn both our data into a dataframe
df = pd.read_csv(url_1)

df_gdp_only = pd.read_csv(url_2)


# We have to join the two together so that we can use the historical GDP in the GLM
df = df.merge(df_gdp_only, on='Year', how='left')


# We need to clean the data of blanks and ND 
df.replace("ND", np.nan, inplace=True)
df = df.dropna()


# Setting our predictor and outcome variables for the GLM

X = df[['3 month CD Rates','10-Year Treasury']]
y = df['GDPC1']

# Add the intercept
X = sm.add_constant(X)

X = X.apply(pd.to_numeric, errors='coerce')
y = pd.to_numeric(y, errors='coerce')



# Linear regression
model = sm.GLM(y, X, family=sm.families.Gaussian())

results = model.fit()


# Model summary
print(results.summary())


# Calculate deviance
print(f"Null Deviance: {results.null_deviance}")
print(f"Model Deviance: {results.deviance}")

# Calculate VIF for the predictors
vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)



