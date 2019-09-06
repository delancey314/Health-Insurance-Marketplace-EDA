import pandas as pd 

cost=pd.read_csv('data/2014/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
headers=list(cost.columns)
uniques=[]
for header in headers:
    col=cost[header]
    uniques.append(col.unique())

uniquevals=dict(zip(headers,uniques))

uniquedict=dict(zip(headers,uniques))
print(headers)



