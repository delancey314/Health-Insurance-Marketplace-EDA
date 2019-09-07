import pandas as pd 
import numpy as np

cost2014=pd.read_csv(f'data/2014/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
cost2015=pd.read_csv(f'data/2015/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
cost2016=pd.read_csv(f'data/2016/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
rules2014=pd.read_csv(f'data/2014/Business_Rules_PUF.csv',low_memory=False)
rules2015=pd.read_csv(f'data/2015/Business_Rules_PUF.csv',low_memory=False)
rules2016=pd.read_csv(f'data/2016/Business_Rules_PUF.csv',low_memory=False)


files = dict{1:'Benefits_Cost_Sharing_PUF.csv'\
            ,2:'Business_Rules_PUF.csv'\
            ,3:'Network_PUF.csv'\
            ,4:'Plan_Attributes_PUF_2014_2015-03-09.csv'\
            ,5:'Rate_PUF.csv'
            ,6: 'Service_Area_PUF.csv'\
            }
def file_selector():
    number_files =input("'A'll, 'Y'ear or 'F'iles or 'S'ingle? ->")
    if number_files=='F' or number_files == 'A':
        year =input('Which year?->')
    if number_files=='S':
        file = input(f"Which file? (choose #)\n {files}")
        df = pd.read_csv(f'data/{year}/{file}',low_memory=False)
    
    
    

    



#fileload_counter determines whether to send a welcome message when file_chooser() is called.
fileloader_counter = 0


#def make_attributes(year=2014,file='Benefits_Cost_Sharing_PUF.csv'):
year=2014
file='Benefits_Cost_Sharing_PUF.csv'
cost=pd.read_csv(f'data/{year}/{file}',low_memory=False)
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
'''
def file_chooser(num_files= 1, year=2014, file ='data/Benefits_Cost_Sharing_PUF.csv'):
     This function allows the user to select the years and files to use

    vars:



    fileloader_counter = 0 displays a welcome. Otherwise it goes to the selection portion.
    year = the user entered year
    file_list = the available files
    file = the user chosen file


    
    if fileloader_counter == 0:
        print('Welcome to the CMS Marketplace dataset. The first step is to load\n \
            files. There are 3 default years and 6 default files')
    fileloader_counter +=1
    while year != 'q':
        year = input("The default years are 2014, 2015, and 2016. Please enter \n\
            the year you wish to use as an integer or 'q' to quit->")

'''
