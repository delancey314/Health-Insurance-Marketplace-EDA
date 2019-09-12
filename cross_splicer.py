import pandas as pd 
import csv
import numpy as np







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