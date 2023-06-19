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
    print('data len:' + str(len(dictionary)))
    return dictionary

def Calculate_clustering_cofficient(max_degree):

    graph_dic = extract_degree_data()  # {id:[id,id} str:int
    coff_dic = {}
    for key in tqdm(graph_dic):
        coop_author = graph_dic[key]
        degree = len(coop_author)
        if (degree > 1 and degree < max_degree):
            link_num = 0
            # (n*n-1)/2
            for i in range(degree):
                author_list_with_i = graph_dic[str(coop_author[i])]
                for j in range(i+1,degree):
                    if coop_author[j] in author_list_with_i:
                        link_num += 1
            # for v in coop_author:
            #     another_author_list = [a for a in coop_author if a != v]
            #     for a in another_author_list:
            #         if a in graph_dic[str(v)]:
            #             link_num += 1

            clustering_cofficient = 2 * link_num/(degree*(degree-1))
            coff_dic[int(key)] = clustering_cofficient

    # save the data
    save_path = './author_clustering_cofficient.txt'
    json_data = json.dumps(coff_dic)

    # 将JSON字符串写入txt文件
    with open(save_path, "w") as file:
        file.write(json_data)

    return None


if __name__ == '__main__':

    # max_degree = 50
    # Calculate_clustering_cofficient(max_degree)
    file_path = './author_clustering_cofficient.txt'  # 指定txt文件的路径

    coff_list = []
    key_list = []
    author_id_list = ['2096889784','2658566389','2097312735','2366747757','2133865736','2057957566','2637120630','2675096063','2644780358','2677144358','2629948182','749666097','2148655407'] # [degree is 9]

    with open(file_path, "r", encoding='utf-8') as file:
        print('start read the  clustering coefficient!')
        dictionary = json.load(file)
        print('load success!')
        for key in tqdm(dictionary):

            if key in author_id_list:
                print(key + ' : ' + str(dictionary[key]/2))

            key_list.append(key)
            coff = dictionary[key]
            coff_list.append(coff/2)

    # print(coff_list[0:50])
    # print('The average clustering coefficient: ' + str(sum(coff_list) / len(coff_list)))
    #
    # # split the coff_list to 25 cells, and count the frequency
    # split_list = np.linspace(0,1,25).tolist()
    # cell_list = [[split_list[i],split_list[i+1]] for i in range(len(split_list)-1)]
    #
    # frequency_list = [0 for i in range(len(cell_list))]
    #
    # for coff in tqdm(coff_list):
    #     for i,cell in enumerate(cell_list):
    #         if coff > cell[0] and coff <= cell[1]:
    #             frequency_list[i] += 1
    #             break
    #
    #
    # frequency_sum = sum(frequency_list)
    #
    # for i in range(len(frequency_list)):
    #     frequency_list[i] = frequency_list[i] / frequency_sum
    #
    #
    # # plot
    # x = [item[0]-0.02-0.004 for item in cell_list]
    # y = [item[1]-item[0]-0.004 for item in cell_list]
    #
    # plt.rcParams['font.family'] = 'Liberation Serif'
    # plt.rcParams['font.size'] = 12
    #
    # plt.bar(x,frequency_list,width=y,align='edge')
    # plt.ylabel('Cumulative Probability')
    # plt.xlabel('Clustering Coefficient')
    # plt.show()
    #
    # plt.bar(x, frequency_list, width=y, align='edge',edgecolor='black',linewidth=1,alpha=0.7)
    # plt.ylim([0,0.2])
    # plt.ylabel('Cumulative Probability')
    # plt.xlabel('Clustering Coefficient')
    # plt.show()
    #
    # plt.bar(x, frequency_list, width=y, align='edge', edgecolor='black', linewidth=1, alpha=0.7)
    # plt.ylim([0, 0.000002])
    # plt.ylabel('Cumulative Probability')
    # plt.xlabel('Clustering Coefficient')
    # plt.show()
    #
    #
    #
    # # twin plot
    # cumulative_freq = []
    # sum_fre = 0
    # for fre in frequency_list:
    #     sum_fre += fre
    #     cumulative_freq.append(sum_fre)
    #
    # cumulative_x = [item[0] for item in cell_list]
    #
    # fig, ax1 = plt.subplots()
    #
    # # plot bar
    # ax1.bar(x, frequency_list, width=y, align='edge',edgecolor='black',linewidth=1,alpha=0.7,label='Probability')
    # ax1.set_ylabel('Probability')
    #
    #
    # # plt curve
    # ax2 = ax1.twinx()
    # ax2.plot(cumulative_x,cumulative_freq,c='r',linestyle='-',marker='*',markersize=5,label='Cumulative Probability')
    # ax2.set_ylabel('Cumulative Probability')
    # ax2.set_xlabel('Clustering Coefficient')
    #
    # ax1.legend(loc = 'best')
    # ax2.legend(loc = 'best')
    #
    # plt.tight_layout()
    # plt.show()






