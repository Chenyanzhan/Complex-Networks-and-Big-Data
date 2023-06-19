# -*- enconding: utf-8 -*-
# @ModuleName: author_data_extraction
# @Function:
# @Author: Yanzhan Chen
# @Time: 2023/6/8 5:39

import json
from tqdm import tqdm
import os

file_name_list = os.listdir('./mag_papers/')
print(file_name_list)
print(len(file_name_list))


# 存储author之间的cooperate关系
author_citation = {}
for name in file_name_list:
    print('Now is processing: '+name)
    file_path = os.path.join('./mag_papers/',name) # 指定txt文件的路径

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in tqdm(lines):
            try:
                dictionary = json.loads(line)
                # the author str exits?
                if 'authors' in dictionary.keys():
                    # the author's num in per paper
                    n_author = len(dictionary['authors'])

                    # iterate all author in this paper
                    for i in range(n_author):
                        # jutify the author id exists in author_citation keys
                        current_author_id = dictionary['authors'][i]['id']
                        other_author = [author['id'] for author in dictionary['authors'] if author['id'] != current_author_id]

                        if current_author_id in author_citation.keys():
                            for other_id in other_author:
                                author_citation[current_author_id].append(other_id)
                        else:
                            author_citation[current_author_id] = []
                            for other_id in other_author:
                                author_citation[current_author_id].append(other_id)


            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")

# filter the repeat co-authors
for key in author_citation:
    author_citation[key] = list(set(author_citation[key]))

# 保存数据
# 将字典转换为JSON格式的字符串
save_path = './author_net.txt'
json_data = json.dumps(author_citation)

# 将JSON字符串写入txt文件
with open(save_path, "w") as file:
    file.write(json_data)
