import pandas as pd 
import csv
import_list=[]
import_dict={}
with open('cohabitation.csv', 'r') as csvfile:
    test_import = csv.reader(csvfile,delimiter=';')
    for line in test_import:
        for value in line:
            output_list =value.split(',')
            import_dict[output_list[0]]=output_list[1]
Cohabitation_hot=import_dict.keys()


        

        


