import json
from tqdm import tqdm
import os

import numpy as np
from scipy.optimize import least_squares
from collections import Counter
import matplotlib.pyplot as plt



def extract_degree_data():

    file_name_list = os.listdir('./extract_data/')
    print(file_name_list)
    print(len(file_name_list))


    num_dict = {}  # node and its degree
    num_list = []  # degree

    for name in tqdm(file_name_list):
        print('Now is processing: '+name)
        file_path = os.path.join('./extract_data/',name) # 指定txt文件的路径

        with open(file_path, "r", encoding='utf-8') as file:
            # line = file.read()
            # dictionary = eval(line)
            # for line in file.readlines():
            #     dictionary = json.loads(line)
            #     print('line 1?')
            dictionary = json.load(file)

            for key, value in dictionary.items():
                degree = len(value['references']) + value['n_citation']
                num_dict[key] = degree
                num_list.append(degree)



    # save the citation degree
    save_path = './citation_degree.txt'
    json_data = json.dumps(num_dict)

    # 将JSON字符串写入txt文件
    with open(save_path, "w") as file:
        file.write(json_data)

    return num_list

def target_function(params,x,y):
    a, b = params
    return a * x + b - y

# r_square
def calculate_r2():
    pass

if __name__ == '__main__':

    # num_list = extract_degree_data()
    # ege_num = 0
    # for i in num_list:
    #     ege_num += i
    # # caculate the degree distribution
    # frequent_dict = dict(Counter(num_list))
    #
    # degree_list = []
    # frequency_list = []
    # sum = 0
    # for key, value in frequent_dict.items():
    #     sum += value
    #
    #
    # for key, value in frequent_dict.items():
    #     degree_list.append(key)
    #     frequency_list.append(value/sum)
    #
    # print('The total paper num:' + str(len(num_list)))
    # print('The total edge num:' + str(int(ege_num/2)))
    #
    # plt.scatter(degree_list,frequency_list)
    # plt.xlabel('k')
    # plt.ylabel('P(x)')
    # plt.show()

    file_path = './citation_degree.txt'  # 指定txt文件的路径

    num_list = []
    key_list = []
    with open(file_path, "r", encoding='utf-8') as file:
        print('start read the paper degree!')
        dictionary = json.load(file)
        print('load success!')
        for key in tqdm(dictionary):
            key_list.append(key)
            degree = dictionary[key]
            num_list.append(degree)

    ege_num = 0
    for i in num_list:
        ege_num += i
    # caculate the degree distribution
    frequent_dict = dict(Counter(num_list))  # {degree:num}

    # sort
    sort_dic = sorted(frequent_dict.items(), key=lambda x: x[0])
    print('*' * 10)
    print(sort_dic[0:10])
    print('*' * 10)

    print('*' * 10)
    print(sort_dic[-10:])
    print('*' * 10)


    degree_list = []
    frequency_list = []
    degree_sum = 0
    for key, value in frequent_dict.items():
        degree_sum += value

    for key, value in frequent_dict.items():
        degree_list.append(key)
        frequency_list.append(value / degree_sum)

    print('The total paper num:' + str(len(num_list)))
    print('The sum degree:' + str(sum(num_list)))
    print('The total edge num:' + str(int(ege_num / 2)))
    print('The average degree:' + str(sum(num_list) / len(num_list)))

    #############################################################################
    # raw degree distribution
    #############################################################################
    plt.rcParams['font.family'] = 'Liberation Serif'
    plt.rcParams['font.size'] = 14
    plt.scatter(degree_list, frequency_list, s=4, c='green', alpha=0.7)
    plt.xlabel('k')
    plt.ylabel('P(x)')
    plt.show()

    #############################################################################
    # log degree linear box
    #############################################################################
    # fitting
    filtering_list = [(i, j) for i, j in zip(degree_list, frequency_list) if i > 0]
    filtering_degree_list = [i[0] for i in filtering_list]
    filtering_frequency_list = [i[1] for i in filtering_list]

    initial_params = [1, 1]
    result = least_squares(target_function, initial_params, args=(
    np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list))))
    a = result.x[0]
    b = result.x[1]
    print('a = ', a)
    print('b = ', b)

    # calculate r2
    y_mean = np.mean(np.log10(np.array(filtering_frequency_list)))
    ss_total = np.sum((np.log10(np.array(filtering_frequency_list)) - y_mean) ** 2)
    ss_residual = np.sum(result.fun ** 2)
    r2 = 1 - (ss_residual / ss_total)
    print('r2 = ', r2)

    max_degree = max(np.log10(np.array(filtering_degree_list)))
    x_fitting = np.linspace(0.001, max_degree, 1000)
    y_fitting = a * x_fitting + b

    plt.scatter(np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list)), s=4, c='green',
                alpha=0.7, zorder=2)
    plt.plot(x_fitting, y_fitting, c='black', linestyle='--')
    plt.xlabel('log(k)')
    plt.ylabel('P(x)')
    plt.show()

    #############################################################################
    # log degree log box
    #############################################################################

    min_degree = min(degree_list)
    max_degree = max(degree_list)
    max_degree_log10 = int(np.log10(max_degree))
    bins = np.logspace(0, max_degree_log10, 70)  # log box
    widths = (bins[1:] - bins[:-1])
    data = np.array(num_list)
    hist = np.histogram(data, bins=bins)
    hist_norm = hist[0] / sum(hist[0])

    # fitting
    # first need to filter the log(0)
    bins_list = bins[0:-1].tolist()
    hist_list = hist_norm.tolist()
    filtering_list = [(i, j) for i, j in zip(bins_list, hist_list) if (i > 0 and j > 0)]
    filtering_degree_list = [i[0] for i in filtering_list]
    filtering_frequency_list = [i[1] for i in filtering_list]

    initial_params = [1, 1]
    result = least_squares(target_function, initial_params, args=(
    np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list))))
    a = result.x[0]
    b = result.x[1]
    print('a = ', a)
    print('b = ', b)

    # calculate r2
    y_mean = np.mean(np.log10(np.array(filtering_frequency_list)))
    ss_total = np.sum((np.log10(np.array(filtering_frequency_list)) - y_mean) ** 2)
    ss_residual = np.sum(result.fun ** 2)
    r2 = 1 - (ss_residual / ss_total)
    print('r2 = ', r2)

    max_degree = max(np.log10(np.array(filtering_degree_list)))
    x_fitting = np.linspace(0.001, max_degree, 500)
    y_fitting = a * x_fitting + b

    plt.scatter(np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list)), s=4, c='green',
                alpha=0.7, zorder=2)
    plt.plot(x_fitting, y_fitting, c='black', linestyle='--')
    plt.xlabel('log(k)')
    plt.ylabel('P(x)')
    plt.show()

    #############################################################################
    # log degree accumulate
    #############################################################################

    # sort the dict
    sorted_data = sorted(frequent_dict.items(), key=lambda item: item[0], reverse=True)  # [(degree,frequency)]

    degree_list = []
    frequency_list = []
    accumulate_degree = 0
    for key, value in sorted_data:
        degree_list.append(key)
        accumulate_degree += value
        frequency_list.append(accumulate_degree)

    for i in range(len(frequency_list)):
        frequency_list[i] = frequency_list[i] / accumulate_degree

    # fitting
    filtering_list = [(i, j) for i, j in zip(degree_list, frequency_list) if (i > 0 and j > 10 ** (-5))]
    filtering_degree_list = [i[0] for i in filtering_list]
    filtering_frequency_list = [i[1] for i in filtering_list]

    initial_params = [1, 1]
    result = least_squares(target_function, initial_params, args=(
        np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list))))
    a = result.x[0]
    b = result.x[1]
    print('a = ', a)
    print('b = ', b)

    # calculate r2
    y_mean = np.mean(np.log10(np.array(filtering_frequency_list)))
    ss_total = np.sum((np.log10(np.array(filtering_frequency_list)) - y_mean) ** 2)
    ss_residual = np.sum(result.fun ** 2)
    r2 = 1 - (ss_residual / ss_total)
    print('r2 = ', r2)

    max_degree = max(np.log10(np.array(filtering_degree_list)))
    x_fitting = np.linspace(0.001, max_degree, 1000)
    y_fitting = a * x_fitting + b

    plt.scatter(np.log10(np.array(filtering_degree_list)), np.log10(np.array(filtering_frequency_list)), s=4,
                c='seagreen', alpha=0.7, zorder=2)
    plt.plot(x_fitting, y_fitting, c='black', linestyle='--')
    plt.xlabel('log(k)')
    plt.ylabel('P(x)')
    plt.ylim([-5, 0])
    plt.show()