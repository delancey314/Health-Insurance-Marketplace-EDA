import pandas as pd 
import numpy as np
year=[2014,2015,2016]
files=[]

def make_attributes(year=2014,file='Benefits_Cost_Sharing_PUF.csv'):
    read_file=pd.read_csv(f'data/{year}/{file}',low_memory=False)
    new_fields=list(read_file.columns)
    uniques=[]
    for field in new_fields:
        col=new_fields[field]
        uniques.append(col.unique())

    uniquedict=dict(zip(headers,uniques))
'''
for header in headers:
    attr=uniquedict[header]   
    np.sort(attr) 
    print(header)
    
    pauser=input('COPY AND PASTE!')
'''

attr=uniquedict['SourceName']   
np.sort(attr) 

















cost=pd.read_csv(f'data/{year}/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
headers=list(cost.columns)
uniques=[]
for header in headers:
    col=cost[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
'''
for header in headers:
    attr=uniquedict[header]   
    np.sort(attr) 
    print(header)
    
    pauser=input('COPY AND PASTE!')
'''

attr=uniquedict['SourceName']   
np.sort(attr) 

