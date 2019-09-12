import pandas as pd 
import csv
import numpy as np

def cohab_unique():
    with open('cohabitation.csv', 'r') as csvfile:
        test_import = csv.reader(csvfile,delimiter=';')
        import_dict={}
        for line in test_import:
            for value in line:
                output_list =value.split(',')
                import_dict[output_list[0]]=output_list[1]
        return list(import_dict.keys())
        
def hot_cat_cohabitation(cohabitation_fields,cohab):
    index=len(cohabitation_fields)
    for idx in range(index):
        new_yes = cohabitation_fields[idx] +',Yes'
        new_no= cohabitation_fields[idx]+',No'
        new_cat=cohabitation_fields[idx]+'-YN'
        cohab[new_yes]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_yes)>=0))
        cohab[new_no] = cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_no)>=0))
        cohab[new_cat]=  np.where((cohab[new_yes] +  cohab[new_no]) >0, 1, 0)
    return cohab

def file_cleaner():
    clean_rules(rules_all)


def clean_rules(rules_all):
    cleaning_file=rules_all.copy()
    rules_drop=['SourceName','VersionNum','ImportDate','IssuerId2',	'MarketCoverage','DentalOnly','Unnamed: 0','RowNumber']
    cleaning_file.drop(rules_drop, axis=1, inplace = True)
    cleaning_file.sort_values("StandardComponentId", inplace=True) 
    cleaning_file.drop_duplicates(keep=False,inplace=True) 
    cleaning_file[cleaning_file['DentalOnlyPlan'] != "Yes"]
    #Data Dictionary says to replace any blanks/NaN with No
    cleaning_file['DentalOnlyPlan'].fillna('No', inplace=True)
    cleaning_file.reset_index()
  
    
    
    return cleaning_file

   

def cohabitation_matrix(rules_cleaned):
    cohab = rules_cleaned.copy()
    #cohab.drop('EnrolleeContractRateDeterminationRule','MinimumTobaccoFreeMonthsRule','DentalOnlyPlan')
    cohabitation_fields=cohab_unique()
    cohab_new_matrix=hot_cat_cohabitation(cohabitation_fields,cohab)

    return cohab_new_matrix



'''
cohab_list=[]
cohab_dict={}
for item in test_lst:
        output_list =str(item).split(',')
        cohab_dict[output_list[0]]=output_list[1]
cohabitation_fields=cohab_dict.keys()

index=len(cohabitation_fields)
'''
    

rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
rules_cleaned=clean_rules(rules_all)



cohabitation_df=cohabitation_matrix(rules_cleaned)
cohabitation_df['DomParAsSpouse']= cohabitation_df['DomesticPartnerAsSpouseIndicator'].apply(lambda x: 1 if x=='Yes'  else 0)
cohabitation_df['SameSexAsSpouse']= cohabitation_df['SameSexPartnerAsSpouseIndicator'].apply(lambda x: 1 if x=='Yes'  else 0) 
depmaxage_df=cohabitation_df[cohabitation_df['DependentMaximumAgRule'] != 'Not Applicable']


