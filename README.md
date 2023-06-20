[English](README.md) | [简体中文](README.zh-CN.md)

This is a project aimed at completing the course on Complex Networks and Big Data. In this project, our main focus was on researching the various properties of academic collaboration networks and paper citation networks. The code primarily involves data preprocessing, analysis of network properties, and paper topic classification based on natural language processing.

Please note that the original dataset is approximately over 500GB, and even after processing, the data still amounts to several tens of gigabytes. Therefore, it is not feasible to upload it to Github. Additionally, the trained model for BERT has not been uploaded as our team intends to submit it to a Chinese journal. If you are interested in the dataset, please feel free to private message me.

You can get started with:

```commandline
pip install numpy
pip install matplotlib
pip install pytorch
pip install networkX
```

Then, you can run data processing and get the results with:

```
python author_data_extraction.py
python author_degree_distribution.py
python author_assortative_matrix.py
python author_vis.py
```

Finally, some results are shown below:

![](C:\Users\Winner\Desktop\src\results\1.svg)

![](C:\Users\Winner\Desktop\src\results\2.svg)

![](C:\Users\Winner\Desktop\src\results\3.svg)

![](C:\Users\Winner\Desktop\src\results\4.svg)
