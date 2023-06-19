# -*- enconding: utf-8 -*-
# @ModuleName: citation_data_extraction
# @Function:
# @Author: Yanzhan Chen
# @Time: 2023/6/7 22:39

import json
from tqdm import tqdm
import os

file_name_list = os.listdir('./mag_papers/')
print(file_name_list)
print(len(file_name_list))
for name in file_name_list:
    print('Now is processing: '+name)
    file_path = os.path.join('./mag_papers/',name) # 指定txt文件的路径
    dictionaries = []
    # 存储论文之间的引用关系
    paper_citation = {}

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in tqdm(lines):
            try:
                dictionary = json.loads(line)
                paper_citation[dictionary['id']] = {}
                if 'references' in dictionary.keys():
                    paper_citation[dictionary['id']]['references'] = dictionary['references']
                else:
                    paper_citation[dictionary['id']]['references'] = []

                if 'n_citation' in dictionary.keys():
                    paper_citation[dictionary['id']]['n_citation'] = dictionary['n_citation']
                else:
                    paper_citation[dictionary['id']]['n_citation'] = 0


                dictionaries.append(dictionary)
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")


    # 保存数据
    # 将字典转换为JSON格式的字符串
    save_path = os.path.join(name[:-3]+'txt')
    json_data = json.dumps(paper_citation)

    # 将JSON字符串写入txt文件
    with open(save_path, "w") as file:
        file.write(json_data)
