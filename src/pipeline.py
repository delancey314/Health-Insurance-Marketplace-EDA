import pandas as pd 
import numpy as np
import os.path 

def check_file_exists(path='/data/field_unique_values/attributes.xlsx'):
    '''
    default path is set to the last file created during project initialization so
    function can be used to confirm the initial files need to be made:
    '''
        if os.path.isfile(path):
    
            return False
        else: 
            return True

def initialize_datasets(delete_original_df='yes', keep_attributes='no'):
    '''
    vars:
    both variables are to determine whether to keep created in files
    after being written to .csv or delete from memory. 

    delete_original_df  = remove original df from memory after a merge. Defaults to 'yes'
    keep_attributes = keep the df used to save the attributes to file.  
                    Defaults to 'no'.  The attribute dictionary is kept in memory 

    Note: This function needs to be rewritten
    '''
   
        make_attributes(delete_original_df,keep_attributes)
        make_network(delete_original_df,keep_attributes)
        make_rules(delete_original_df,keep_attributes)
        make_rate(delete_original_df,keep_attributes)
        make_area(delete_original_df,keep_attributes)
        make_cross(delete_original_df,keep_attributes)
        


def create_csv_files(dataframe,delete_original_df='no', keep_attributes= None, init = None,\
                     location = None, name):
    #init is used to tell the function  to write the initial files. If != yes,
    #it writes to  the 'other' folder.

    if init=='yes':
        idx=0
        for frame in dataframe:
            if idx ==0:
                frame.to_csv(path=f'/data/combined/{name}.csv')
            elif idx == 1:
                frame.to_csv(path=f'/data/info/{name}_info.csv')
            else:
                df_to_excel(frame,name,path=f'/data/field_unique_values/attributes.xlsx')
            idx +=1
    else:
        frame.to_csv(path=f'/data/other/{name}_info.csv')
    pass

def df_to_excel(dataframe,name,path=f'/data/other/{name}.xlsx',mode= 'a'):
    writer = pd.ExcelWriter(path, engine='openpyxl')
    if path.isfile(path):
        with ExcelWriter(path, mode= mode) as writer:
              dataframe.to_excel(writer, sheet_name=name)
    else:
        with ExcelWriter(path) as writer:
              dataframe.to_excel(writer, sheet_name=name)
    

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
    attributes=df_unique(dataframe,name, path=)
    create_csv_files([dataframe,information,attributes]\
                      ,delete_original_df, keep_attributes,name,init='yes')
    pass

def df_info_save(dataframe,name):
    info=dataframe.info()
    info_df=DataFrame(info)
    info.to_csv(path='/data/info/{name}_info.csv')
    del info
        
    

def find_all_uniques(dataframe, name, init='no'):
    headers=list(dataframe.columns)
    uniques=[]

    for header in headers:
        col=df[header]
        uniques.append(col.unique())

    uniquedict=dict(zip(headers,uniques))
    if init == 'yes':
        unique_df=pd.DataFrame(uniquedict,name)
        df_to_excel(dataframe,name,path='/data/field_unique_values/{name}.xlsx',mode= 'a')
    return unique_df


def make_service_area(delete_original_df,keep_attributes):
   
    area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
    area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
    area2016=pd.read_csv('data/2016/ServiceArea_PUF_2015_12_08.csv',low_memory=False)
    area_all=combine_df([area2014,area2015,area2016],delete_original_df='yes')

    init_files=make_init_files(area_all, name='area_all', delete_original_df='no')

    
def make_rules(delete_original_df,keep_attributes):
    rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
    rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
    rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015_12_08.csv',low_memory=False)

    rulesall=pd.concat([rules2014,rules2015,rules2016],sort=False)

        

def make_cross(delete_original_df,keep_attributes):
    #ran out of time to finish pipeline
    pass 

 def make_network(delete_original_df,keep_attributes):
    #ran out of time to finish pipeline
    pass  
  def make_rate(delete_original_df,keep_attributes):
    #ran out of time to finish pipeline
    pass      
def make_attributes(delete_original_df,keep_attributes):
    #ran out of time to finish pipeline
    pass

def load_base_files():
    cost_all= pd.read_csv('data/merged/cost_all.csv',low_memory=False)
    rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
    network_all=pd.read_csv('data/merged/network_all.csv',low_memory=False)
    attribute_all=pd.read_csv('data/merged/attribute_all.csv',low_memory=False)
    rate_all=pd.read_csv('data/merged/rate_all.csv',low_memory=False)
    area_all=pd.read_csv('data/merged/area_all.csv',low_memory=False)
    cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
    machine16=pd.read_csv('data/merged/machine_all.csv',low_memory=False)

    cost_unique= pd.read_csv('data/field_unique_values/cost_unique.csv',low_memory=False)
    rules_unique=pd.read_csv('data/field_unique_values/rules_unique.csv',low_memory=False)
    network_unique=pd.read_csv('data/field_unique_values/network_unique.csv',low_memory=False)
    attribute_unique=pd.read_csv('data/field_unique_values/attribute_unique.csv',low_memory=False)
    rate_unique=pd.read_csv('data/field_unique_values/rate_unique.csv',low_memory=False)
    area_unique=pd.read_csv('data/field_unique_values/area_unique.csv',low_memory=False)
    cross_unique=pd.read_csv('data/field_unique_values/cross_unique.csv',low_memory=False)
    machine16_unique=pd.read_csv('data/field_unique_values/machine_unique.csv',low_memory=False)
   

if __name__ == "__main__":
    if check_file_exists == False:
        new_load=initialize_datasets()
    else:
        load_base_files()
