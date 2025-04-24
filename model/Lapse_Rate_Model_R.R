# Lapse Rate GLM model 

# Collaborators: Simon Zheng, Tanna Henry, Alejandro Ordonez

# If not installed: install.packages("tidyverse")
library(tidyverse)

raw_file = read.csv("https://raw.githubusercontent.com/ajordonez/Lapse_Rate_GLM_Model/refs/heads/main/data/Uncleaned_Predictive_Analytics.csv")

lapse_data = data.frame(raw_file)

lapse_data = lapse_data %>% filter("")