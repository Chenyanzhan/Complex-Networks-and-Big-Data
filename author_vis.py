from pyvis.network import Network
import json
from tqdm import tqdm
import time


def extract_degree_data():
    file_path = './author_net.txt'# 指定txt文件的路径
    start_time = time.time()
    with open(file_path, "r", encoding='utf-8') as file:
        print('start read the author net!')
        dictionary = json.load(file)
        print('load success!')
    end_time = time.time()
    print('data len:' + str(len(dictionary)))
    print('The read time:' + str(end_time - start_time))
    return dictionary

# author_id net
def vis_some_author(author_id_list): # str

    dictionary = extract_degree_data()

    for author_id in author_id_list:
        net = Network() # create a graph
        net.add_nodes([int(author_id)],color=['#00ff1e'])

        other_author_list = [str(a) for a in dictionary[author_id]]
        net.add_nodes([int(i) for i in other_author_list],color=['#162347' for i in other_author_list])

        # add the edge
        for other_author in other_author_list:
            net.add_edge(int(author_id),int(other_author),weight=1)


        # the deeper relationship among other authors
        for author in tqdm(other_author_list):

            second_author_list = [str(a) for a in dictionary[author]]
            net.add_nodes([int(i) for i in second_author_list],color=['#dd4b39' for i in second_author_list])

            for second_a in second_author_list:
                net.add_edge(int(author),int(second_a),weight=1)

        net.show_buttons(filter_=['physics'])
        net.save_graph('./Network_Vis/'+author_id+'_network.html')

if __name__ == '__main__':
    # author_id = '2304463073'
    # author_id_list = ['2939603420','1656308615','2195303297','2266067964','2163167345']  # [100,200]
    # author_id_list = ['2100824496','299661368','1520439318','2628645320','2045125008'] #[40,50]
    # author_id_list = ['2125147041','2636220891','2683484130','2636841559','2084787745','94621996'] #[19]
    author_id_list = ['2096889784','2658566389','2097312735','2366747757','2133865736','2057957566','2637120630','2675096063','2644780358','2677144358','2629948182','749666097','2148655407'] #[9]
    vis_some_author(author_id_list)