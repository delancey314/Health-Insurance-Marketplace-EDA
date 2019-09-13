import pandas as pd
import numpy as np 
import csv


def make_samples(names):
    for name in names:
        temp_df=pd.read_csv(f'data/merged/{name}_all.csv',low_memory=False)
        sample_df=temp_df.sample(10000,random_state=130919)
        sample_df.to_csv(f'data/{name}_sample.csv')

file_list=['area','attribute','cost','cross','network','rate','rules']
make_samples(file_list)