#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    replace_category.py
# @Author:      Kuro
# @Time:        8/25/2021 7:08 PM


import pandas as pd

df_table1=pd.read_excel('table_not_2.xlsx')
for index, row in df_table1.iterrows():
    #merge data except image and category
    # print(row['defaultImage'])
    if pd.isnull(row['categoryText1']):
        df_table1.at[index,'categoryText1'] = "Nezařazeno"
    else:
        for i in range(1,11):
            if not pd.isnull(df_table1.at[index,'categoryText'+str(i)]):
                print(i)
                category = df_table1.at[index,'categoryText'+str(i)]
                new_cate = "Sběratelské potřeby>Leuchtturm>" + category[category.find('>')+1:]
                df_table1.at[index,'categoryText'+str(i)] = new_cate
                # print(df_table1.at[index,'categoryText'+str(i)])
df_table1.to_excel('table1_not_in_XML_add_name_cate.xlsx',index=False)



