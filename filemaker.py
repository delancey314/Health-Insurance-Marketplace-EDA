import pandas as pd 
import numpy as np
import glob
chunksize = 10000

#cost2016 has characters that can't be read =  can't find it.
cost2016=pd.read_csv('data/2016/Benefits_Cost_Sharing_PUF_2015_12_08.csv',low_memory=False, encoding ='latin1')
cost2014=pd.read_csv('data/2014/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
cost2015=pd.read_csv('data/2015/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
'''
rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015_12_08.csv',low_memory=False)

rulesall=pd.concat([rules2014,rules2015,rules2016],sort=False)
'''

'''
network2014=pd.read_csv('data/2014/Network_PUF.csv',low_memory=False)
network2015=pd.read_csv('data/2015/Network_PUF.csv',low_memory=False)
network2016=pd.read_csv('data/2016/Network_PUF_2015_12_08.csv',low_memory=False)

networkall=pd.concat([network2014,network2015,network2016],sort=False)
'''

'''
attr2014=pd.read_csv('data/2014/Plan_Attributes_PUF_2014_2015_03_09.csv',low_memory=False)
attr2015=pd.read_csv('data/2015/Plan_Attributes_PUF.csv',low_memory=False)
attr2016=pd.read_csv('data/2016/Plan_Attributes_PUF_2015_2_08.csv',low_memory=False)

attrall=pd.concat([attr2014,attr2015,attr2016], sort=False)
'''

'''
rate2014=pd.read_csv('data/2014/Rate_PUF.csv',low_memory=False)
rate2015=pd.read_csv('data/2015/Rate_PUF.csv',low_memory=False)
rate2016=pd.read_csv('data/2016/Rate_PUF_2015_12_08.csv',low_memory=False)

rateall=pd.concat([rate2014,rate2015,rate2016], sort=False)
'''

'''
area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
area2016=pd.read_csv('data/2016/ServiceArea_PUF_2015_12_08.csv',low_memory=False)

areaall=pd.concat([area2014,area2015,area2016],sort=False)
'''
'''
cross1415=pd.read_csv('data/2015/Plan_Crosswalk_PUF_2014_12_22.csv',low_memory=False)
cross2016=pd.read_csv('data/2015/Plan_Crosswalk_PUF_2015_12_07.csv',low_memory=False)

crossall=pd.concat(cross1415,cross2016], sort = False)
'''

# machine16=pd.read_excel('data/2015/Machine_Readable_PUF_2015_12_21.xlsx',low_memory=False)#



#files = ['data/2014/Service_Area_PUF.csv','data/2015/Service_Area_PUF.csv','data/2016/Service_Area_PUF.csv']


#result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

'''
for i in range(3):
   .....:     data = pd.DataFrame(np.random.randn(10, 4))
   .....:     data.to_csv('file_{}.csv'.format(i))


#cost2014=pd.read_csv('data/2014/Benefits_Cost_Sharing_PUF.csv',chunksize=chunksize)
#cost2015=pd.read_csv('data/2015/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
#cost2016=pd.read_csv('data/2016/Benefits_Cost_Sharing_PUF_2015-12-08.csv',low_memory=False)
costall1=pd.concat([cost2014, 2015], axis=1)
del cost2014
del cost2015

chunksize = 10000
chunks = []
for chunk in pd.read_csv('data/2016/Benefits_Cost_Sharing_PUF_2015-12-08.csv', chunksize=chunksize):
    # Do stuff...
    costall = pd.concat([costall,chunks] axis=1)

files = [cost2014,cost2015,cost2016]
original = pandas.DataFrame({
    'Age':[10, 12, 13], 
    'Gender':['M','F','F']})

# Note this column has 4 rows of values:
additional = pandas.DataFrame({
    'Name': ['Nate A', 'Jessie A', 'Daniel H', 'John D']
})

new = pandas.concat([original, additional], axis=1) 
# Identical:
# new = pandas.concat([original, additional], ignore_index=False, axis=1) 

print(new.head())

#          Age        Gender        Name
#0          10             M      Nate A
#1          12             F    Jessie A
#2          13             F    Daniel H
#3         NaN           NaN      John D

df=cost2014.copy(deep=True)
#dfprop = df.info()
headers=list(df.columns)
uniques=[]
for header in headers:
    col=df[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
import xlsxwriter

workbook = xlsxwriter.Workbook('data/attribute_files/cost2014_attr.xlsx',{'nan_inf_to_errors': True,'constant_memory': True} )
worksheet = workbook.add_worksheet()


row = 0
col = 0
order=sorted(uniquedict.keys())

for key in order:
    row += 1
    worksheet.write(row, col,     key)
    i =1
    for item in uniquedict[key]:
        worksheet.write(row, col + i, item)
        i += 1

workbook.close()
'''



