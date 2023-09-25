import pandas as pd
     

file_path = '/content/sample_data/california_housing_train.csv'
df = pd.read_csv(file_path, sep=',')
     

df['population'].min()
     
3.0

df[df['population'] < 500].median_house_value.mean()
     
206683.83635227982