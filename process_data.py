# -*- coding: utf-8 -*-
""" 
Created on 8/8/2021 5:24 PM
@author  : Kuro Kien
@File name    : process_data.py 
"""

import pandas as pd

all_data=pd.read_excel(r'F:\AI_FL\crawl_sele\All_data_us.xlsx')
# table1=pd.read_excel(r'F:\AI_FL\crawl_sele\table1_have_but_all_dont_have.xlsx')

# duplicate_data=pd.read_excel(r'C:\Users\DELL\Downloads\AI_FL\crawl_sele\duplicate_code_in_all_data.xlsx')
# # dup_sort = duplicate_data.sort_values('code',ascending=False)
# # print(dup_sort['code'])
# # print(len(duplicate_data))
# temp = duplicate_data[duplicate_data['code']==800003]
# print(temp.iloc[1,8])
# df1 = pd.DataFrame([[1,2,3]])
# df2 = pd.DataFrame([['a','b','d','c']])
# df3 = df1.append(df2)
# print(df3)


# xml_to_excel['ean']=xml_to_excel['ean'].fillna()

# list_code_table_1=list(table1['code']) #list ean của table 1
list_code_all_data=list(all_data['code']) # list ean của xml
#
#
# #
print(len(all_data))
# print(len(table1))
# #
new_all_data = all_data.drop_duplicates(subset=['code']) # ko dupli
print(len(new_all_data))
new_all_data.to_excel('dont_have_dupli_in_all_data_us.xlsx',index=False)
# # list_code_new_all_data=list(new_all_data['code'])
# # boolean = new_all_data['code'].duplicated().any()
# #
# list_code_not_dupilicate=list(all_data['code'])
# duplicate=table1['code'].isin(all_data)
# duplicate1=table1['code'].isin(all_data)
# #
# # print(boolean)
# # print(len(new_all_data))
# #
all_dup = all_data[all_data.duplicated(subset=['code'])]
print(len(all_dup))
# print(all_dup)
all_dup.to_excel('duplicate_code_in_all_data_us.xlsx',index=False)
#
# # xml have but excel dont have
# duplicate_data=table1[~duplicate]
# dont_duplicate_data=table1[duplicate]
# print(len(duplicate_data))
# print(len(dont_duplicate_data))
# duplicate_data.to_excel('duplicate_code_in_all_data.xlsx',index=False)

#  xml have and table 1 have
# table1_have_and_all_have=table1[duplicate1]
# print(len(table1_have_and_all_have))
# print("table1 have but all dont have: "  +str(len(table1) - len(all_and_table1_have)))
# table1_have_but_all_dont_have.to_excel('xml_and_table1_have.xlsx',index=False)
#
# table1_have_but_all_dont_have=table1[~duplicate1]
# print(len(table1_have_but_all_dont_have))
# print(list(table1))
# table1_have_but_all_dont_have.to_excel('table1_have_but_all_dont_have.xlsx',index=False,columns=list(table1))

# #excel and xml have
# duplicate=table1['ean'].isin(lis2)
# excel_and_xlm_have = table1[duplicate]
# print(len(excel_and_xlm_have))
# excel_and_xlm_have.to_excel('xml_and_table1_have.xlsx',index=False)
#
# #excel have and xml dont have
# excel_have_but_xlm_dont_have = table1[~duplicate]
# print(len(excel_have_but_xlm_dont_have))
# excel_have_but_xlm_dont_have.to_excel('excel_have_but_xlm_dont_have.xlsx',index=False)
