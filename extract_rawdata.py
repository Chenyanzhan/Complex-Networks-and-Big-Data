# -*- enconding: utf-8 -*-
# @ModuleName: extract_rawdata
# @Function:
# @Author: Yanzhan Chen
# @Time: 2023/6/7 16:14
import json
from tqdm import tqdm
import os


file_path = "./mag_papers_1/1.txt"  # 指定txt文件的路径

dictionaries = []
# 存储论文之间的引用关系
paper_citation = {}

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in tqdm(lines):
        try:
            dictionary = json.loads(line)
            if 'references' in dictionary.keys():
                paper_citation[dictionary['id']] = dictionary['references']
            else:
                paper_citation[dictionary['id']] = []
            dictionaries.append(dictionary)
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")

# # 操作解析后的字典列表
# for dictionary in dictionaries:
#     # 处理每个字典
#     print(dictionary)
#     print(dictionary['id'])
#     break


# 保存数据
# 将字典转换为JSON格式的字符串
save_path = './citation_data.txt'
json_data = json.dumps(paper_citation)

# 将JSON字符串写入txt文件
with open(save_path, "w") as file:
    file.write(json_data)