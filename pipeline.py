import pandas as pd 
import numpy as np


def start_df(delete_original_df='yes', keep_info='no', keep_attributes='yes'):
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
    all three variables are to determine whether to keep created in files
    after being written to .csv or delete from memory. 

    delete_original_df  = remove original df from memory after a merge. Defaults to 'yes'
    keep_info = keep  df holding the df.info() in memory.  Defaults to 'no'. 
    keep_attributes = keep the df used to save the attributes to file.  
                    Defaults to 'yes'.  The attribute dictionary is kept in memory
    
    ''''
    try:
        #attributes.xlsx is tested  because it is the last file created.
        test=pd.read_excel(open('attributes.xlsx','rb'),\
            sheet_name='service_area_all')
    except:
        break
    else:
        make_rules(delete_original_df,keep_info,keep_attributes)
        make_network(delete_original_df,keep_info,keep_attributes)
        make_attributes(delete_original_df,keep_info,keep_attributes)
        make_rate(delete_original_df,keep_info,keep_attributes)
        make_service_area(delete_original_df,keep_info,keep_attributes)
        make_cross(delete_original_df,keep_info,keep_attributes)

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

def save_combined_df(combined_df):
    '''
    saves the combined dataframe for a group to the 'combined' folder
    '''



def make_service_area(delete_original_df,keep_info,keep_attributes):
    '''
    makes the service area dfs then sends them to be saved
    completes all the steps described in start_df for the 'Service Area' files
     vars:
    all three variables are to determine whether to keep created in files
    after being written to .csv or delete from memory. 

    delete_original_df  = keep the combined, merged database in memory. Defaults to 'yes'.
    keep_info = keep  df holding the df.info() in memory.  Defaults to 'no'. 
    keep_attributes = keep the df used to save the attributes to file.  
                    Defaults to 'yes'.  The attribute dictionary is kept in memory
    '''

    service_area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
    service_area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
    service_area2016=pd.read_csv('data/2016/ServiceArea_PUF_2015_12_08.csv',low_memory=False)
    service_area_all=combine_files([service_area2014,service_area2015,service_area2016])
    
    save_combined_df(service_area_all)
    create_attributes(service_area_all)
    create_info(service_area_all)

    rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
    rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
    rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015_12_08.csv',low_memory=False)

rulesall=pd.concat([rules2014,rules2015,rules2016],sort=False)
''' 
df=cost2014.copy(deep=True)
dfprop = df.info()
headers=list(df.columns)
uniques=[]
for header in headers:
    col=df[header]
    uniques.append(col.unique())

uniquedict=dict(zip(headers,uniques))
#df_unique= pd.DataFrame(uniquedict)
'''
if __name__ == "__main__":
    importdf(10)
    

'''
