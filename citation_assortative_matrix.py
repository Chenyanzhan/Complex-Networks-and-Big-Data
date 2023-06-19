import json

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os


# Determine the size of the assortative_matix
def Calculate_size(num_list):
    return max(num_list)

def Calculate_matrix(ass_matrix,degree_dic):
    file_name_list = os.listdir('./extract_data/')
    print(file_name_list)
    print(len(file_name_list))

    for name in tqdm(file_name_list):
        print('Now is processing: ' + name)
        file_path = os.path.join('./extract_data/', name)  # 指定txt文件的路径

        with open(file_path, "r", encoding='utf-8') as file:
            dictionary = json.load(file)
            for key, value in dictionary.items():
                for c_id in value['references']:
                    try:
                        degree_key = int(degree_dic[key])
                    except KeyError:
                        continue
                    try:
                        degree_v = int(degree_dic[str(c_id)])
                    except KeyError:
                        continue

                    ass_matrix[degree_key - 1, degree_v - 1] += 1
                    ass_matrix[degree_v - 1, degree_key - 1] += 1
    return None




if __name__ == '__main__':

    # file_path = './citation_degree.txt'  # 指定txt文件的路径
    #
    # num_list = [] # record the degree
    # key_list = [] # record the author id
    # with open(file_path, "r", encoding='utf-8') as file:
    #     print('start read the citation degree!')
    #     dictionary = json.load(file)
    #     print('load success!')
    #     for key in tqdm(dictionary):
    #         key_list.append(key)
    #         degree = dictionary[key]
    #         num_list.append(degree)
    #     print('success fill the num_list!')
    #
    # # matrix size
    # matrix_size = Calculate_size(num_list)
    #
    # # create the assortative matrix
    # ass_matrix = np.zeros([matrix_size,matrix_size])
    #
    # # fill the matrix
    # Calculate_matrix(ass_matrix,dictionary)
    #
    # # save the matrix
    # # save the paritial to avoid too big file
    # limit_num = 70000
    # ass_matrix = ass_matrix[0:limit_num,0:limit_num]
    # np.save('citaion_assortative_matrix.npy',ass_matrix)

    file_name = './citaion_assortative_matrix.npy'
    matrix = np.load(file_name)
    print('load assortative matrix success!')

    control_size = 200
    matrix = matrix[0:control_size, 0:control_size]

    matrix_sum = np.sum(matrix)
    assortative_matrix = matrix / matrix_sum
    max_prob = np.max(assortative_matrix)

    plt.rcParams['font.family'] = 'Liberation Serif'
    plt.rcParams['font.size'] = 12
    plt.imshow(assortative_matrix, cmap='hot', vmin=0, vmax=0.00005)  # (vmax = 0.00005 # 1000)
    plt.colorbar()
    plt.show()


