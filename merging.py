import numpy as np 
import pandas as pd 
import csv
import folium
import pdb
'''
This python script loads the saved merged files for 2014-2017 CMS Marketplace
Data and cleans it. Cleaning includes dropping unnecessary columns and rows as well
as creating universal keys.
    At this point, there is a separate function for each filegroup because the cleaning
 process is different. A future project will be merging this with 'filemaker.py' as a
 class.
'''


def clean_files():
    '''contents moved to if name, main section due to time constraint'''

    """ area_all=pd.read_csv('data/merged/area_all.csv',low_memory=False)
    area_clean=clean_area(area_all)
    network_all=pd.read_csv('data/merged/network_all.csv',low_memory=False)
    network_clean=clean_network(network_all)
    cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
    cross_clean=clean_cross(cross_all)  """
    rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
    rules_cleaned=clean_rules(rules_all)





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
    crosswalk levels 0,1,2,&,3 mean the plan stayed the same across all 3 years.
    They varied by geographical level - national, state, county, zip code.
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


def create_cohabitation_dataframes(rules_cleaned):

    '''
    The rules filegroup includes a field on whether cohabitation is required to be
    on the insurance policy for various relationships to the policyholder. 
    relationship-YN is an indicator that policy allows that type of relative to 
    be included.
    ''' 
    cohabitation_df=cohabitation_matrix(rules_cleaned)
    cohabitation_df['DomParAsSpouse']= cohabitation_df['DomesticPartnerAsSpouseIndicator'].apply(lambda x: 1 if x=='Yes'  else 0)
    cohabitation_df['SameSexAsSpouse']= cohabitation_df['SameSexPartnerAsSpouseIndicator'].apply(lambda x: 1 if x=='Yes'  else 0) 
    depmaxage_df=cohabitation_df[cohabitation_df['DependentMaximumAgRule'] != 'Not Applicable']
    cohabitation_fields=list(cohabitation_df.columns.values)

    return cohabitation_df

    

def cohabitation_matrix(rules_cleaned):
    cohab = rules_cleaned.copy()
    cohabitation_fields=cohab_unique()
    cohab_new_matrix=hot_cat_cohabitation(cohabitation_fields,cohab)

    return cohab_new_matrix

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
    
    for idx in range(len(cohabitation_fields)):
        new_yes = cohabitation_fields[idx] +',Yes'
        new_no= cohabitation_fields[idx]+',No'
        new_cat=cohabitation_fields[idx]+'-YN'
        cohab[new_yes]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_yes)>=0))
        cohab[new_no] = cohab['CohabitationRule'].apply(lambda r: int(str(r).find(new_no)>=0))
        cohab[new_cat]=  np.where((cohab[new_yes] +  cohab[new_no]) >0, 1, 0)
    
    return cohab


'''
The functions below should also be moved into their own class.  They take a list
fields, map them on US and state maps, and save the maps
'''
def map_maker(dataframe, input_fields= ['Spouse,Yes'],years=[2014,2015,2016,'all']\
            , map_area = 'US'):

    #The list below is a manually cleaned version of cohabitation_fields
    default_fields =['Spouse,Yes','Spouse,No','Spouse-YN', 'Adopted Child,Yes',\
    'Adopted Child,No', 'Adopted Child-YN','Stepson or Stepdaughter,Yes',\
    'Stepson or Stepdaughter,No','Stepson or Stepdaughter-YN','Self,Yes',\
    'Self,No','Self-YN','Child,Yes','Child,No','Child-YN','Life Partner,Yes',\
    'Life Partner,No','Life Partner-YN','Grandson or Granddaughter,Yes',\
    'Grandson or Granddaughter,No','Grandson or Granddaughter-YN','Ward,Yes',\
    'Ward,No','Ward-YN','Dependent on a Minor Dependent,Yes',\
    'Dependent on a Minor Dependent,No','Dependent on a Minor Dependent-YN',\
    'Guardian,Yes','Guardian,No','Guardian-YN','Court Appointed Guardian,Yes',\
    'Court Appointed Guardian,No','Court Appointed Guardian-YN',\
    'Sponsored Dependent,Yes','Sponsored Dependent,No','Sponsored Dependent-YN',\
    'Foster Child,Yes','Foster Child,No','Foster Child-YN',\
    'Son-in-Law or Daughter-in-Law,Yes','Son-in-Law or Daughter-in-Law,No',\
    'Son-in-Law or Daughter-in-Law-YN','Ex-Spouse,Yes','Ex-Spouse,No',\
    'Ex-Spouse-YN','Brother or Sister,Yes','Brother or Sister,No',\
    'Brother or Sister-YN','Nephew or Niece,Yes','Nephew or Niece,No',\
    'Nephew or Niece-YN','Collateral Dependent,Yes','Collateral Dependent,No',\
    'Collateral Dependent-YN','Annultant,Yes','Annultant,No','Annultant-YN',\
    'Other Relationship,Yes','Other Relationship,No','Other Relationship-YN',\
    'Father or Mother,Yes','Father or Mother,No','Father or Mother-YN',\
    'Other Relative,Yes','Other Relative,No','Other Relative-YN',
    'Stepparent,Yes','Stepparent,No','Stepparent-YN',\
    'Grandfather or Grandmother,Yes','Grandfather or Grandmother,No',\
    'Grandfather or Grandmother-YN','Uncle or Aunt,Yes','Uncle or Aunt,No',\
    'Uncle or Aunt-YN','Cousin,Yes','Cousin,No','Cousin-YN',\
    'Brother-in-Law or Sister-in-Law,Yes','Brother-in-Law or Sister-in-Law,No',\
    'Brother-in-Law or Sister-in-Law-YN','Father-in-Law or Mother-in-Law,Yes',\
    'Father-in-Law or Mother-in-Law,No','Father-in-Law or Mother-in-Law-YN',\
    'Trustee,Yes','Trustee,No','Trustee-YN','DomParAsSpouse','SameSexAsSpouse']
    
    if not len(input_fields)>0:
        input_fields = default_fields.copy()
    

    for field in input_fields:
        map_design=initialize_map_conditions(map_area)
        map_list=map_series(dataframe,field,years,map_design)
        


def initialize_map_conditions(map_area='US'):
    
    '''
    returns the longitude and latitude and zoom level for each map. 
    More areas will be added.
    '''
    aliases =['United States','USA','America','United States of America']
    if map_area in aliases:
        map_area = 'US'
    map_dict={'US':'[48, -102], zoom_start=3',\
                'CO':'[39, -106], zoom_start=6'}

    return map_dict[map_area]

def map_series(dataframe,field,years,location=[48, -102], zoom_start=3):
    
    url ='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
    state_geo= f'{url}/us-states.json'
    for year in years:
        m= folium.Map(location=[48, -102], zoom_start=3)
        if year == 'all':
            temp_df=dataframe.copy()

        else:
            #pdb.set_trace()
            temp_df=dataframe[dataframe['BusinessYear']==year]
            map_columns=temp_df.groupby('StateCode').sum()
            map_columns.reset_index(inplace=True)
            
            
        folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=map_columns,
        columns=['StateCode', field],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f'Cohabitation Criteria for {year}-{field}').add_to(m)
        folium.LayerControl().add_to(m)
        m
        #m.save(f'/images/cohabitation {year}-{field}.html')
      
      
   



if __name__ == "__main__":

    """ area_all=pd.read_csv('data/merged/area_all.csv',low_memory=False)
    area_clean=clean_area(area_all)
    network_all=pd.read_csv('data/merged/network_all.csv',low_memory=False)
    network_clean=clean_network(network_all)
    cross_all=pd.read_csv('data/merged/cross_all.csv',low_memory=False)
    cross_clean=clean_cross(cross_all)  """
    rules_all=pd.read_csv('data/merged/rules_all.csv',low_memory=False)
    rules_cleaned=clean_rules(rules_all)
    #clean_files()
    cohabitation_data=create_cohabitation_dataframes(rules_cleaned)
    make_maps=map_maker(cohabitation_data)

    
