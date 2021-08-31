#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    merge_2.py
# @Author:      Kuro
# @Time:        8/25/2021 8:37 PM

# -*- coding: utf-8 -*-
"""
Created on 8/10/2021 12:48 PM
@author  : Kuro Kien
@File name    : merger_data.py
"""
import pandas as pd
import numpy as np
import math
# pd.set_option("display.max_rows", None, "display.max_columns", None)

def process_category(categories_link):
    categories = categories_link[8:-1].split('/')
    return '>'.join(categories)

def process_default_image(default_image_link):
    end = default_image_link.find('/9df78eab')
    url_default_img = default_image_link[:57] + "image/1640x1640" + default_image_link[end:]
    return url_default_img

# df_info_table1_dont_fill = pd.DataFrame(columns=['code'])

# df_info_table1 = pd.DataFrame(columns=['code','pairCode','name','ean','defaultImage',
#                                        'image','image2','image3','image4','image5',
#                                        'image6','image7','image8',
#                                        'categoryText1','categoryText2','categoryText3',
#                                        'categoryText4','categoryText5','categoryText6',
#                                        'categoryText7','categoryText8','categoryText9',
#                                        'categoryText10','price','currency','stock',
#                                        'availabilityOutOfStock','availabilityInStock'])

df_table1=pd.read_excel('Table1-not-in-XML.xlsx')
df_info_table1 = df_table1
df_info_table1 = df_info_table1.replace(np.nan, '', regex=True)
# df_info_table1['categoryText1'] = df_info_table1['categoryText1'].astype(str)
df_info_table1 = df_info_table1.astype(str)

# print(df_info_table1)
df_dont_duplicate = pd.read_excel('dont_have_dupli_in_all_data.xlsx')
df_duplicate = pd.read_excel('duplicate_code_in_all_data.xlsx')
df_dont_duplicate_us = pd.read_excel('dont_have_dupli_in_all_data_us.xlsx')
df_duplicate_us = pd.read_excel('duplicate_code_in_all_data_us.xlsx')
# print(df_table1)
count = 0
code_dont_have = []
for index, row in df_table1.iterrows():
    print(index)
    # merge data except image and category
    # df_info_table1.at[index,'code'] = row['code']
    # df_info_table1.at[index,'pairCode'] = row['pairCode']
    # df_info_table1.at[index, 'name'] = row['name']
    # df_info_table1.at[index, 'ean'] = row['ean']
    # df_info_table1.at[index, 'price'] = row['price']
    # df_info_table1.at[index, 'currency'] = "CZK"
    # df_info_table1.at[index, 'stock'] = "0"
    # df_info_table1.at[index, 'availabilityOutOfStock'] = "Skladem"
    # df_info_table1.at[index, 'availabilityInStock'] = "do 14 dnů"

    #merge category and image
    #dont duplicate
    row_data_dont_duplicate = df_dont_duplicate[df_dont_duplicate['code'] == row['code']]

    if not row_data_dont_duplicate.empty:
        #category
        count+=1
        # print(row_data_dont_duplicate)
        category = process_category(row_data_dont_duplicate.iloc[0,0])
        # print(category)
        df_info_table1.at[index, 'categoryText1'] = category
        #image
        default_image = process_default_image(row_data_dont_duplicate.iloc[0, 3])
        # print(default_image)
        df_info_table1.at[index, 'defaultImage'] = default_image
        df_info_table1.at[index, 'image'] = default_image
        images = []
        for idx_image in range(5,12):
            images.append(row_data_dont_duplicate.iloc[0, idx_image])
        if isinstance(images[0], str):
            for idx_image in range(2,len(images)+2):
                df_info_table1.at[index, 'image'+str(idx_image)] = images[idx_image-2]
        continue
    # dont duplicate_us
    row_data_dont_duplicate_us = df_dont_duplicate_us[df_dont_duplicate_us['code'] == row['code']]

    if not row_data_dont_duplicate_us.empty:
        # category
        count+=1
        print(row_data_dont_duplicate)
        category = process_category(row_data_dont_duplicate_us.iloc[0, 0])
        print(category)
        df_info_table1.at[index, 'categoryText1'] = category
        # image
        default_image = process_default_image(row_data_dont_duplicate_us.iloc[0, 3])
        # print(default_image)
        df_info_table1.at[index, 'defaultImage'] = default_image
        df_info_table1.at[index, 'image'] = default_image
        images = []
        for idx_image in range(5, 12):
            images.append(row_data_dont_duplicate_us.iloc[0, idx_image])
        if isinstance(images[0], str):
            for idx_image in range(2, len(images) + 2):
                df_info_table1.at[index, 'image' + str(idx_image)] = images[idx_image - 2]
        continue

    #duplicate
    row_data_duplicate = df_duplicate[df_duplicate['code'] == row['code']]
    if not row_data_duplicate.empty:
        # category
        count += 1
        categores_list = []
        for idx_cate in range(len(row_data_duplicate.iloc[:, 2])):
            categores_list.append(row_data_duplicate.iloc[idx_cate,0])
            # print(row_data_duplicate.iloc[idx_cate,0])
        # print(len(row_data_duplicate.iloc[:, 2]))
        # print(categores_list)
        #fill full 10 category
        for i in range(len(categores_list),10):
            categores_list.append("")
        for i in range(1,len(categores_list)+1):
            if categores_list[i-1]!='':
                category = process_category(categores_list[i-1])
            else:
                category=''
            df_info_table1.at[index, 'categoryText'+str(i)] = category
        #images
        default_image = process_default_image(row_data_duplicate.iloc[0, 3])
        # print(default_image)
        df_info_table1.at[index, 'defaultImage'] = default_image
        df_info_table1.at[index, 'image'] = default_image
        images = []
        for idx_image in range(5, 12):
            images.append(row_data_duplicate.iloc[0, idx_image])
        if isinstance(images[0], str):
            for idx_image in range(2, len(images) + 2):
                df_info_table1.at[index, 'image' + str(idx_image)] = images[idx_image - 2]
        continue

    #duplicate us
    row_data_duplicate_us = df_duplicate_us[df_duplicate_us['code'] == row['code']]
    if not row_data_duplicate_us.empty:
        # category
        count += 1
        categores_list = []
        for idx_cate in range(len(row_data_duplicate_us.iloc[:, 2])):
            categores_list.append(row_data_duplicate_us.iloc[idx_cate,0])
            # print(row_data_duplicate.iloc[idx_cate,0])
        # print(len(row_data_duplicate.iloc[:, 2]))
        # print(categores_list)
        #fill full 10 category
        for i in range(len(categores_list),10):
            categores_list.append("")
        for i in range(1,len(categores_list)+1):
            if categores_list[i-1]!='':
                category = process_category(categores_list[i-1])
            else:
                category=''
            df_info_table1.at[index, 'categoryText'+str(i)] = category
        #images
        default_image = process_default_image(row_data_duplicate_us.iloc[0, 3])
        # print(default_image)
        df_info_table1.at[index, 'defaultImage'] = default_image
        df_info_table1.at[index, 'image'] = default_image
        images = []
        for idx_image in range(5, 12):
            images.append(row_data_duplicate_us.iloc[0, idx_image])
        if isinstance(images[0], str):
            for idx_image in range(2, len(images) + 2):
                df_info_table1.at[index, 'image' + str(idx_image)] = images[idx_image - 2]
        continue
    code_dont_have.append(row['code'])




# print(df_info_table1)
# print(len(code_dont_have))
# for i in range(len(code_dont_have)):
#     df_info_table1_dont_fill.at[i,'code'] = code_dont_have[i]
# df_info_table1_dont_fill.to_excel('code_table_1_need_crawl.xlsx',index=False)
df_info_table1.to_excel('table_not_2.xlsx',index=False)
# print(len(df_dont_duplicate))


    # print(row['code'], row['pairCode'], row['name'], row['ean'])

# print(df_info_table1.head())



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


