import pandas as pd 
import numpy as np
import glob
chunksize = 10000

def filemaker(df_list, delete_original_df = 'no'):
    combined_df=pd.concat(df_list,sort=False)
    if delete_original_df=='yes':
        for original_df in df_list:
            del original_df
    return combined_df



cost2016=pd.read_csv('data/2016/Benefits_Cost_Sharing_PUF_2015_12_08.csv',low_memory=False, encoding ='latin1')
cost2014=pd.read_csv('data/2014/Benefits_Cost_Sharing_PUF.csv',low_memory=False)
cost2015=pd.read_csv('data/2015/Benefits_Cost_Sharing_PUF.csv',low_memory=False)

cost_all=filemaker([cost2016,cost2014,cost2015])
#cost_all.to_csv('data/merged/cost_all.csv')
cost_sample=cost_all(n=20000,random_state=913)


rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False)
rules2015=pd.read_csv('data/2015/Business_Rules_PUF_Reformat.csv',low_memory=False)
rules2016=pd.read_csv('data/2016/Business_Rules_PUF_2015_12_08.csv',low_memory=False)

rules_all=filemaker([rules2016,rules2014,rules2015])
#rules_all.to_csv('data/merged/rules_all.csv')
#rules_all=pd.concat([rules2014,rules2015,rules2016],sort=False)



network2014=pd.read_csv('data/2014/Network_PUF.csv',low_memory=False)
network2015=pd.read_csv('data/2015/Network_PUF.csv',low_memory=False)
network2016=pd.read_csv('data/2016/Network_PUF_2015_12_08.csv',low_memory=False)

#network_all=pd.concat([network2014,network2015,network2016],sort=False)
network_all=filemaker([network2016,network2014,network2015])
#network_all.to_csv('data/merged/network_all.csv')

attr2014=pd.read_csv('data/2014/Plan_Attributes_PUF_2014_2015_03_09.csv',low_memory=False)
attr2015=pd.read_csv('data/2015/Plan_Attributes_PUF.csv',low_memory=False)
attr2016=pd.read_csv('data/2016/Plan_Attributes_PUF_2015_2_08.csv',low_memory=False)

attr_all=filemaker([attr2016,attr2014,attr2015])
#attr_all.to_csv('data/merged/attr_all.csv')

#attr_all=pd.concat([attr2014,attr2015,attr2016], sort=False)



rate2014=pd.read_csv('data/2014/Rate_PUF.csv',low_memory=False)
rate2015=pd.read_csv('data/2015/Rate_PUF.csv',low_memory=False)
rate2016=pd.read_csv('data/2016/Rate_PUF_2015_12_08.csv',low_memory=False)

#rate_all=pd.concat([rate2014,rate2015,rate2016], sort=False)
rate_all=filemaker([rate2016,rate2014,rate2015])
#rate_all.to_csv('data/merged/rate_all.csv')


area2014=pd.read_csv('data/2014/Service_Area_PUF.csv',low_memory=False)
area2015=pd.read_csv('data/2015/Service_Area_PUF.csv',low_memory=False)
area2016=pd.read_csv('data/2016/ServiceArea_PUF_2015_12_08.csv',low_memory=False)

#area_all=pd.concat([area2014,area2015,area2016],sort=False)
area_all=filemaker([area2016,area2014,area2015])
#area_all.to_csv('data/merged/area_all.csv')

cross1415=pd.read_csv('data/2015/Plan_Crosswalk_PUF_2014_12_22.csv',low_memory=False)
cross2016=pd.read_csv('data/2016/Plan_ID_Crosswalk_PUF_2015_12_07.csv',low_memory=False)
cross_all=filemaker([cross2016,cross1415])
#cross_all.to_csv('data/merged/cross_all.csv')

#cross_all=pd.concat(cross1415,cross2016], sort = False)


machine16=pd.read_excel('data/2016/Machine_Readable_PUF_2015_12_21.xlsx')
#machine16.to_csv('data/merged/machine16.csv')

