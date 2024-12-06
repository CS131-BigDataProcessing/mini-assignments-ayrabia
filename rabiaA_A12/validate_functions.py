import pandas as pd

def validate_data(dataframe):


#Validate that the vic sex is either M or F and vic age is between 1 and 100


sex_valid = datafram['Vict sex'].isin(['M', 'F']).all()

age_valid = datafram['Vict age'].between(1,100).all()

no_null = dataframe[['Vict sex', 'Vict age']].notnull().all().all()

return sex_valid and age_valid and no_null


