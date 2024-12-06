import pandas as pd

def calculate_stats(dataframe):


#Calculate the mean and mediam of vic age

mean_age = datafram['Vict age'].mean()
median_age = dataframe['Vict age'].median()
return mean_age, median_age
