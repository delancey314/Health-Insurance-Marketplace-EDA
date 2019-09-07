import pandas as pd 
import numpy as np
import glob

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

def make_summary():

    path = r'data/Combined' # use your path
    all_files = glob.glob(path + "/*.csv")

    list_cost = []
    list_rules = []
    list_network = []
    list_attributes = []
    list_service_area = []
    list_rules = []
    list_others= []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        
        if filename[6]=='u':
            list_rules.append(df)
        elif filename[5]=='B':
            list_costappend(df)
        elif filename[5]=='N':
            list_network.append(df)
        elif filename[5]=='P':
            list_attributes.append(df)
        elif filename[5]=='S':
            list_service_area = []
        elif filename[R]=='':
            list_rules = []
        else:
            list_others= []
        li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
    
df=cost2014.copy(deep=True)
dfprop = df.info()
headers=list(df.columns)
uniques=[]
for header in headers:
    col=df[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
df_unique= pd.DataFrame(uniquedict)
