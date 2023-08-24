import pandas as pd

data = pd.read_csv("C:/Users/SPTINT-10/Desktop/mpg.csv")
print(data)
print(" ")
stats = data.describe()
print(stats)
print(" ")
print(data[data ['cylinders']==8]['name'])
print(" ")

