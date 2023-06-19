# -*- enconding: utf-8 -*-
# @ModuleName: citation_data_extraction
# @Function: find the paper with max degree
# @Author: Yanzhan Chen
# @Time: 2023/6/7 22:39


import json
from tqdm import tqdm
import os

file_name_list = os.listdir('./mag_papers/')
print(file_name_list)
print(len(file_name_list))

the_max_degree_id = '1775749144'

break_flag = False
for name in file_name_list:
    print('Now is processing: '+name)
    file_path = os.path.join('./mag_papers/',name) # 指定txt文件的路径


    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in tqdm(lines):
            try:
                dictionary = json.loads(line)

                if str(dictionary['id']) == the_max_degree_id:
                    print(dictionary['title'])
                    break_flag = True
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")

    if break_flag:
        break


