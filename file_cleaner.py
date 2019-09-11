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

   


""" def cohabitation_matrix(cleaning_file):
    cohab = cleaning_file
    #cohab.drop('EnrolleeContractRateDeterminationRule','MinimumTobaccoFreeMonthsRule','DentalOnlyPlan')
    cohab_categories_yes=['Father or Mother']
    
    for category in cohab_categories_yes:
        cohab[category]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find(category)>=0))
    return cohab

    import_list=[]
    import_dict={}
    with open('cohabitation.csv', 'r') as csvfile:
        test_import = csv.reader(csvfile,delimiter=';')
        for line in test_import:
            for value in line:
                output_list =value.split(',')
                import_dict[output_list[0]]=output_list[1]
    Cohabitation_hot=import_dict.keys()
    cohab_list=[]
    index=len(Cohabitation_hot)
f   or idx in index:

        new_yes = Cohabitation_hot[idx] +', Yes'
        new_no= Cohabitation_hot[idx]+', No'
        new_cat=Cohabitation_hot[idx]+'-YN'
        cohab[new_yes]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find('new_yes')>=0))
        cohab[new_no] = cohab['CohabitationRule'].apply(lambda r: int(str(r).find('new_no')>=0))
        cohab[new_cat]=  np.where(cohab[new_yes] ==1 or cohab[new_no]==1, 1, 0)
    
""" 
rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
test_arr = rules_all['CohabitationRule'].unique()
test_lst = test_arr.tolist()
#rules_cleaned=clean_rules(rules_all)

cohab_list=[]
cohab_dict={}
for item in test_lst:
        output_list =str(item).split(',')
        cohab_dict[output_list[0]]=output_list[1]
Cohabitation_hot=cohab_dict.keys()

index=len(Cohabitation_hot)