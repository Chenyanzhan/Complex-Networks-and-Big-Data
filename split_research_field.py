# -*- enconding: utf-8 -*-
# @ModuleName: citation_data_extraction
# @Function: Big citation network to small field network
# @Author: Yanzhan Chen
# @Time: 2023/6/7 22:39

import json
from tqdm import tqdm
import os

field_list = ['physics','mathematics','computer science','biology','finance','statistics','electrical engineering','economics']
# field_list = ['physics','mathematics','computer science','biology']

file_name_list = os.listdir('./mag_papers/')
print(file_name_list)
print(len(file_name_list))

for name in file_name_list:
    print('Now is processing: '+name)
    file_path = os.path.join('./mag_papers/',name) # 指定txt文件的路径
    # 存储论文之间的引用关系
    paper_citation = [{} for i in range(len(field_list))]

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in tqdm(lines):
            try:
                dictionary = json.loads(line)
                if 'fos' in dictionary.keys():
                    is_filed = False
                    for field_id in range(len(field_list)):
                        justify_list = [field_list[field_id] in i['name'] for i in dictionary['fos']]
                        if any(justify_list):
                            f_index = field_id
                            is_filed = True
                            break
                    if is_filed:
                        paper_citation[f_index][dictionary['id']] = {}
                        if 'references' in dictionary.keys():
                            paper_citation[f_index][dictionary['id']]['references'] = dictionary['references']
                        else:
                            paper_citation[f_index][dictionary['id']]['references'] = []

                        if 'n_citation' in dictionary.keys():
                            paper_citation[f_index][dictionary['id']]['n_citation'] = dictionary['n_citation']
                        else:
                            paper_citation[f_index][dictionary['id']]['n_citation'] = 0

            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")


    # 保存数据
    # 将字典转换为JSON格式的字符串
    for i,field in enumerate(field_list):
        save_path = os.path.join('./split/',str(i)+'_'+name[:-3]+'txt')
        json_data = json.dumps(paper_citation[i])
        # 将JSON字符串写入txt文件
        with open(save_path, "w") as file:
            file.write(json_data)
