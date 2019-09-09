import pandas as pd
cost_all= pd.read_csv('data/merged/cost_all.csv',low_memory=False)
rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
network_all=pd.read_csv('data/merged/network_all.csv',low_memory=False)
attr_all=pd.read_csv('data/merged/attr_all.csv',low_memory=False)
rate_all=pd.read_csv('data/merged/rate_all.csv',low_memory=False)
area_all=pd.read_csv('data/merged/area_all.csv',low_memory=False)
cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
machine16=pd.read_csv('data/merged/machine16.csv',low_memory=False)


def find_all_uniques(df, file_name, init='no'):
    '''
    finds all uniques for each field in a df and assigns them to a new df.
    adds the df to an excel spreadsheet if a copy hasn't already been saved.
    '''
    headers=list(df.columns)
    uniques=[]
    for header in headers:
        col=df[header]
        uniques.append(col.unique())
    uniquedict=dict(zip(headers,uniques))
    unique_df=pd.DataFrame(uniquedict)
    if init == 'yes':
        df_to_excel(df,file_name,path='/data/attribute_files/{file_name}.xlsx',mode= 'a')
    return unique_df

def df_to_excel(dataframe,file_name,path='/data/other/{file_name}.xlsx',mode= 'a'):
    writer = pd.ExcelWriter(path, engine='openpyxl')
    if path.isfile(path):
        with ExcelWriter(path, mode= mode) as writer:
              dataframe.to_excel(writer, sheet_name=file_name)
    else:
        with ExcelWriter(path, mode= mode) as writer:
              dataframe.to_excel(writer, sheet_name=file_name)


cost_unique= find_all_uniques(cost_all, cost_all,init='yes')
rules_unique=find_all_uniques(rules_all, rules_all, init='yes')
network_unique=find_all_uniques(network_all,network_all, init='yes')
attr_unique=find_all_uniques(attr_all, attr_all, init='yes')
rate_unique=find_all_uniques(rate_all, rate_all, init='yes')
area_unique=find_all_uniques(area_all, area_all, init='yes')
cross_unique=find_all_uniques(cross_all, cross_all, init='yes')
machine16_unique=find_all_uniques(machine16, machine16, init='yes')