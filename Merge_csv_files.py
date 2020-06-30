# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:14:05 2020

@author: Issstezac1
"""

import csv
import pandas as pd 

path1 = "C:/Users/Issstezac1/Desktop/DropboxTest/test.csv"
path2 = "C:/Users/Issstezac1/Downloads/dataFrames.csv"

df1 = pd.read_csv(path1, delimiter =',')
df2= pd.read_csv(path2, delimiter =',')

data = (df2.assign(Id=df2.Id.eq(0).cumsum()-1)
    .merge(df1, on='Id')
    .groupby('Id')
    .agg({'Cam_id':'first','Image':'first','Timestamp':'first',          
          'Detection_Class':list, 'Detection_Score':list})
    .reset_index()
)

data.to_csv("C:/Users/Issstezac1/Desktop/DropboxTest/final.csv",
            mode = 'a',
            sep = '.,',
            ignore_index = True)
