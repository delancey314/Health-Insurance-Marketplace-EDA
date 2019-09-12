import numpy as np 
import pandas as pd 
import csv





def clean_area(area_all):
    cleaning_data=area_all.copy()
    drop_list=['Unnamed: 0','SourceName','VersionNum','ImportDate','IssuerId2',\
    'StateCode2','PartialCountyJustification','RowNumber','MarketCoverage',\
    'DentalOnlyPlan','DentalOnly']
    cleaning_data.drop(drop_list,axis=1,inplace=True)
    cleaning_data['CoverEntireState']=  np.where(cleaning_data['CoverEntireState']=='Yes', 1, 0)
    cleaning_data['PartialCounty']=  np.where(cleaning_data['PartialCounty']=='Yes', 1, 0)
    cleaning_data['ProductId']=  cleaning_data['IssuerId'].map(str)+cleaning_data['ServiceAreaId']
    
    return cleaning_data
    
    
    #ataframe["period"] = dataframe["Year"].map(str) + dataframe["quarter"]
def clean_network(network_all):
    cleaning_data=network_all.copy()
    drop_list=['Unnamed: 0','SourceName','VersionNum','ImportDate','IssuerId2',\
    'StateCode2','NetworkURL','RowNumber','MarketCoverage',\
    'DentalOnlyPlan','DentalOnly']
    cleaning_data.drop(drop_list,axis=1,inplace=True)
    cleaning_data['IssuerId'].map(str)+cleaning_data['NetworkId']

    return cleaning_data

def clean_cross(cross_all):
    cleaning_file=cross_all.copy()
    cleaning_file.drop(cleaning_file.iloc[:, 12:], inplace = True, axis = 1) 
    cross_drop=['Unnamed: 0','MetalLevel_2015','DentalPlan']
    cleaning_file.drop(cross_drop, axis=1, inplace = True)
    cleaning_file.sort_values('PlanID_2015', inplace=True)
    """
    crosswalk levels 0,1,2&3 mean the plan stayed the same across all 3 years.
    They varied by geographical level - zip code up to national
    """
    cleaning_file[cleaning_file['CrosswalkLevel']<4]

    return cleaning_file

def clean_rules(rules_all):
    cleaning_file=rules_all.copy()
    rules_drop=['SourceName','VersionNum','ImportDate','IssuerId2',	'MarketCoverage','DentalOnly','Unnamed: 0','RowNumber']
    cleaning_file.drop(rules_drop, axis=1, inplace = True)
    cleaning_file.sort_values("StandardComponentId", inplace=True) 
    cleaning_file.drop_duplicates(keep=False,inplace=True) 
    cleaning_file[cleaning_file['DentalOnlyPlan'] != "Yes"]
    #Data Dictionary says to replace any blanks/NaN with No
    cleaning_file['DentalOnlyPlan'].fillna('No', inplace=True)
    

    return cleaning_file



def cohabitation_matrix(rules_cleaned):
    cohab = rules_cleaned.copy()
    cohabitation_fields=cohab_unique()
    cohab_new_matrix=hot_cat_cohabitation(cohabitation_fields,cohab)

    return cohab_new_matrix

def cohab_unique():
    with open('cohabitation.csv', 'r') as csvfile:
        test_import = csv.reader(csvfile,delimiter=';')
        import_dict={}
        for line in test_import:howdy DentalOnly
            for value in line:
                output_list =value.split(',')
                import_dict[output_list[0]]=output_list[1]
        return list(import_dict.keys())
        
def hot_cat_cohabitation(cohabitation_fields,cohab):
    
    for idx in range(len(cohabitation_fields)):
        new_yes = cohabitation_fields[idx] +',Yes'
        new_no= cohabitation_fields[idx]+',No'
        new_cat=cohabitation_fields[idx]+'-YN'
        cohab[new_yes]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_yes)>=0))
        cohab[new_no] = cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_no)>=0))
        cohab[new_cat]=  np.where((cohab[new_yes] +  cohab[new_no]) >0, 1, 0)
    
    return cohab


area_all=pd.read_csv('data/merged/area_all.csv',low_memory=False)
area_clean=clean_area(area_all)
network_all=pd.read_csv('data/merged/network_all.csv',low_memory=False)
network_clean=clean_network(network_all)
cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
cross_clean=clean_cross(cross_all)
rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
rules_cleaned=clean_rules(rules_all)