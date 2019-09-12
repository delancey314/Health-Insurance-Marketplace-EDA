import pandas as pd 
import csv
import numpy as np
import_list=[]
import_dict={}
with open('cohabitation.csv', 'r') as csvfile:
    test_import = csv.reader(csvfile,delimiter=';')
    for line in test_import:
        for value in line:
            output_list =value.split(',')
            import_dict[output_list[0]]=output_list[1]
Cohabitation_hot=list(import_dict.keys())

for idx in range(len(Cohabitation_hot)):

    new_yes = Cohabitation_hot[idx] +', Yes'
    new_no= Cohabitation_hot[idx]+', No'
    new_cat=Cohabitation_hot[idx]+'-YN'
    cohab[new_yes]= cohab['CohabitationRule'].apply(lambda r: int(str(r).find('new_yes')>=0))
    cohab[new_no] = cohab['CohabitationRule'].apply(lambda r: int(str(r).find('new_no')>=0))
    cohab[new_cat]=  np.where(cohab[new_yes] ==1 or cohab[new_no]==1, 1, 0)


    
    




        

        


