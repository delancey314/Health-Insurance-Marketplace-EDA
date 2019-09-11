import pandas as pd 
import csv
import numpy as np





def clean_cross(cleaning_file):

    cross_drop=['Unnamed: 0','MetalLevel_2015','MetalLevel_2016','IssuerID_AgeOff2016','MultistatePlan_AgeOff2016','ChildAdultOnly_AgeOff2016','MetalLevel_2014','AgeOffPlanID_2015','IssuerID_AgeOff2015','MultistatePlan_AgeOff2015','MetalLevel_AgeOff2015','ChildAdultOnly_AgeOff2015']
    cleaning_file.drop(cross_drop, axis=1, inplace = True)
    cleaning_file.sort_values('PlanID_2015', inplace=True)
    cleaning_file[cleaning_file.DentalPlan != 'Yes']
    """
    crosswalk levels 0,1,2&3 mean the plan stayed the same across all 3 years.
    They varied by geographical level - zip code up to national
    """
    cleaning_file[cleaning_file.CrosswalkLevel <4]





cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
cross_clean=clean_cross(cross_all)


"""  
def clean_cross(cleaning_file):
    cross_drop=['SourceName','VersionNum','ImportDate','IssuerId2',	'MarketCoverage','DentalOnly','Unnamed: 0','RowNumber']
    cleaning_file.drop(cross_drop, axis=1, inplace = True)
    cleaning_file.sort_values("StandardComponentId", inplace=True) 
    cleaning_file.drop_duplicates(keep=False,inplace=True) 
    cleaning_file[cross_all.DentalOnlyPlan != "Yes"]
    #Data Dictionary says to replace any blanks/NaN with No
    cleaning_file['DentalOnlyPlan'].fillna('No', inplace=True)
    cleaning_file.reset_index()
  """