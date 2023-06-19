import json

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os

def extract_degree_data():
    file_path = './author_net.txt'# 指定txt文件的路径

    with open(file_path, "r", encoding='utf-8') as file:
        print('start read the author net!')
        dictionary = json.load(file)
        print('load success!')
    return dictionary


# Determine the size of the assortative_matix
def Calculate_size(num_list):
    return max(num_list)

def Calculate_matrix(ass_matrix,degree_dic):
    graph_dic = extract_degree_data()  # {id:[id,id} str:int
    for key in tqdm(graph_dic):
        for v in graph_dic[key]:
            degree_key = int(degree_dic[key])
            degree_v = int(degree_dic[str(v)])
            ass_matrix[degree_key-1,degree_v-1] += 1
            ass_matrix[degree_v-1,degree_key-1] += 1
    return None



if __name__ == '__main__':

    # file_path = './author_degree.txt'  # 指定txt文件的路径
    #
    # num_list = [] # record the degree
    # key_list = [] # record the author id
    # with open(file_path, "r", encoding='utf-8') as file:
    #     print('start read the author degree!')
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
    # np.save('assortative_matrix.npy',ass_matrix)
    #
    # # plot the matrix
    # fig, ax = plt.subplots()
    # im = ax.imshow(ass_matrix)
    # plt.show()

    file_name = './assortative_matrix.npy'
    matrix = np.load(file_name)

    control_size = 200
    matrix = matrix[0:control_size,0:control_size]
    print('load assortative matrix success!')
    matrix_sum = np.sum(matrix)
    assortative_matrix = matrix/matrix_sum
    max_prob = np.max(assortative_matrix)

    plt.rcParams['font.family'] = 'Liberation Serif'
    plt.rcParams['font.size'] = 12
    plt.imshow(assortative_matrix,cmap='viridis',vmin=0,vmax=0.00005)  # (vmax = 0.00005 # 1000)
    plt.colorbar()
    plt.show()


