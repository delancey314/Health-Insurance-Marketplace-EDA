import pandas as pd 

def file_cleaner():
    clean_rules(rules_all)


def clean_rules(cleaning_file):
    rules_drop=['SourceName','VersionNum','ImportDate','IssuerId2',	'MarketCoverage','DentalOnly','Unnamed: 0','RowNumber']
    cleaning_file.drop(rules_drop, axis=1, inplace = True)
    cleaning_file.sort_values("StandardComponentId", inplace=True) 
    cleaning_file.drop_duplicates(keep=False,inplace=True) 
    cleaning_file[rules_all.DentalOnlyPlan != "Yes"]
    #Data Dictionary says to replace any blanks/NaN with No
    cleaning_file['DentalOnlyPlan'].fillna('No', inplace=True)
    cleaning_file.reset_index()
    cohabitation_matrix(cleaning_file)
    return cleaning_file

   


def cohabitation_matrix(cleaning_file):
    cohab = cleaning_file
    cohab.drop('EnrolleeContractRateDeterminationRule','MinimumTobaccoFreeMonthsRule','DentalOnlyPlan')
    cohab_categories_yes=['Father or Mother, Yes']
    cohab_categories_no=[]
    for category in cohab_categories_yes:
        cohab[category]= cohab.apply(test_condition, axis=1)

def test_condition():
    if cohab[CohabitationRule].isin(category):
        return 1
    else:
        return 0

    
rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
rules_cleaned=clean_rules(rules_all)