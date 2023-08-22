import pandas as pd
d = {'days': [1,2,3,4,5,6,7,8,9,10],
     'steps': [4335,9335,7332,4504,5335,7552,8332,6504,8965,7689]}
df = pd.DataFrame(d)
print(df)
df['steps']=df['steps']+1000
print(df)
dayseven=df[df['steps']>7000]['days']
print(list(dayseven))
