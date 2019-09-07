import pandas as pd 
import numpy as np

cost2014=pd.read_csv('data/2014/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
'''
cost2015=pd.read_csv('data/2015/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
cost2016=pd.read_csv('data/2016/Benefits_Cost_Sharing_PUF_2015-12-08.csv',low_memory=False)
rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015-12-08.csv',low_memory=False)
network2014=pd.read_csv('data/2014/Network_PUF.csv',low_memory=False)
network2015=pd.read_csv('data/2015/Network_PUF.csv',low_memory=False)
network2016=pd.read_csv('data/2016/Network_PUF.csv',low_memory=False)
attr2014=pd.read_csv('data/2014/Plan_Attributes_PUF_2014_2015-03-09.csv',low_memory=False)
attr2015=pd.read_csv('data/2015/Plan_Attributes_PUF.csv',low_memory=False)
attr2016=pd.read_csv('data/2016/Plan_Attributes_PUF.csv',low_memory=False)
rate2014=pd.read_csv('data/2014/Rate_PUF.csv',low_memory=False)
rate2015=pd.read_csv('data/2015/Rate_PUF.csv',low_memory=False)
rate2016=pd.read_csv('data/2016/Rate_PUF.csv',low_memory=False)
area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
area2016=pd.read_csv('data/2016/Service_Area_PUF.csv',low_memory=False)
cross1415=pd.read_csv('data/2015/Plan_Crosswalk_PUF_2014-12-22.csv',low_memory=False)
machine16=pd.read_excel('data/2015/Machine_Readable_PUF_2015-12-21.xlsx',low_memory=False)
'''
df=cost2014.copy(deep=True)
dfprop = df.info()
headers=list(df.columns)
uniques=[]
for header in headers:
    col=df[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
 
