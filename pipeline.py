import pandas as pd 
import numpy as np
import os.path 


def initialize_datasets(delete_original_df='yes', keep_attributes='no'):
    '''
    Helper function checks to see if files have been loaded into combined df. 
    If not it loads a related group of files as pandas df,
    merges them into a single combined df, 
    saves the combined df to the 'combined' folder,
    deletes the original file based dfs to release memory, 
    creates a dictionary of all unique attributes for each 
    field and writes it to the 'attributes' folder,
     assigns the df.info() to its own df
    then adds the df.info to the 'dataset_info.ods' file.
    This is repeated for all file groups.

    vars:
    both variables are to determine whether to keep created in files
    after being written to .csv or delete from memory. 

    delete_original_df  = remove original df from memory after a merge. Defaults to 'yes'
    keep_attributes = keep the df used to save the attributes to file.  
                    Defaults to 'no'.  The attribute dictionary is kept in memory 
    '''

    if os.path.isfile('/data/attribute_files/attributes.xlsx'):
        '''
         attributes.xlsx is tested for existence because it is the last one made.
          If it does, the init files already exist so the function is stopped.   
        '''
        return False
    
    else:
        #make_attributes(delete_original_df,keep_attributes)
        #make_network(delete_original_df,keep_attributes)
        #make_rules(delete_original_df,keep_attributes)
        #make_rate(delete_original_df,keep_attributes)
        make_service_area(delete_original_df,keep_attributes)
        #make_cross(delete_original_df,keep_attributes)
        
        return True


def create_csv_files(dataframe,delete_original_df='no', keep_attributes= None, init = None,\
                     location = None, name = None):
    if init=='yes':
        idx=0
        for frame in dataframe:
            if idx ==0:
                frame.to_csv(path='/data/combined/{name}.csv')
            elif idx == 1:
                frame.to_csv(path='/data/info/{name}_info.csv')
            else:
                df_to_excel(frame,name,path='/data/attributes/attributes.xlsx')
            idx +=1
    else:
        frame.to_csv(path='/data/other/{name}_info.csv')
    pass

def df_to_excel(dataframe,name,path='/data/other/{name}.xlsx',mode= 'a'):
    writer = pd.ExcelWriter(path, engine='openpyxl')
    if path.isfile(path):
        with ExcelWriter(path, mode= mode) as writer:
              dataframe.to_excel(writer, sheet_name=name)
    else:
        with ExcelWriter(path, mode= mode) as writer:
              dataframe.to_excel(writer, sheet_name=name)
    pass

def combine_df(df_list,delete_original_df='no'):
    '''
    Combines all df for a given group then returns the combined df.
    Deletes the individual df to free memory if requested. 
    
    vars:
    df_list = the list of files to combine
    delete_original_df= deletes the original df. Defaults to 'no'for normal use but
    'yes' is passed in for the first initialization of files.
    '''
    combined_df=pd.concat(df_list,sort=False)
    if delete_original_df=='yes':
        for original_df in df_list:
            del original_df
    return combined_df
    pass


def make_init_files(dataframe, delete_original_df,name):
    '''
    Saves the combined dataframe as '{name}.csv'
    Creates new df that stores the dataframes df.info() file that is
    saved as '{name}_info.csv'
    Creates a a dictionary and df that stores all unique attributes.
    the df is saved as '{name}_attributes.xlsx'.
    
    vars:
    dataframe = name of the combined dataframe
    delete_original_df = del combined df from memory once its saved to file
    keep_attributes = keep the attributes df from memory once its saved to file

    '''

    information = df_info_save(dataframe,name)
    attributes=df_unique(dataframe)
    create_csv_files([dataframe,information,attributes]\
                      ,delete_original_df, keep_attributes,name,init='yes')
    pass

def df_info_save(dataframe,name):
    info=dataframe.info()
    info_df=DataFrame(info)
    info.to_csv(path='/data/info/{name}_info.csv')
    del info
    
    pass

def find_all_uniques(dataframe, name, init='no'):
    headers=list(dataframe.columns)
    uniques
    pass

    
'''

headers=list(df.columns)
uniques=[]
for header in headers:
    col=df[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
#df_unique= pd.DataFrame(uniquedict)
'''












def make_service_area(delete_original_df,keep_attributes):
    '''
    makes the service area dfs then sends them to be saved
    completes all the steps described in initialize_datasets for the 'Service Area' files
     vars:
    all three variables are to determine whether to keep created in files
    after being written to .csv or delete from memory. 

    delete_original_df  = keep the combined, merged database in memory. 
                        Defaults to 'no'
    keep_attributes = keep the df used to save the attributes to file.  
                    Defaults to 'no'.  The attribute dictionary is kept in memory
    '''

    service_area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
    service_area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
    service_area2016=pd.read_csv('data/2016/ServiceArea_PUF_2015_12_08.csv',low_memory=False)
    service_area_all=combine_df([service_area2014,service_area2015,service_area2016],delete_original_df='yes')

    init_files=make_init_files(service_area_all, name='service_area_all', delete_original_df='no')

    
'''
    rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
    rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
    rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015_12_08.csv',low_memory=False)

    rulesall=pd.concat([rules2014,rules2015,rules2016],sort=False)
''' 


if __name__ == "__main__":
    new_load=initialize_datasets()
