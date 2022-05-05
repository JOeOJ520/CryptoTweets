# Text Classification and Data Anaylsis on Cryptocurrency Related Tweets in PySpark Enviorment
## Disclaimer
This project is an improvement of the final project of upper year CS course "Data-Intensive Distributed Analytics" at the University of Waterloo by [Hugh Chung](https://github.com/hughyyyy) , [Joe Liang](https://github.com/JOeOJ520), and [Shawn Li](https://github.com/Shawn-Personal). The codes for setting up the Pyspark environments in this project are credited to [Ali Abedi](https://cs.uwaterloo.ca/~a2abedi/), the instructor in Winter 2022.

Data in this project is from the Kaggle post "Bitcoin Tweets" under CC0: Public Domain license. The data includes tweets that have #Bitcoin and #btc hashtags from 2016. It is a 13 dimension vector with 11804338 rows in total. Additional information about this dataset can be found [here](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets).

## Background
[Cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency) becomes a popular topic in social media and the financial market. On 30 November 2020, bitcoin hit a new all-time high of $19,860. NLP Analysis on the posts related to cryptocurrency in social media could be an interest area of study.  

The goal of this project is to demonstrate the ability to use Pyspark and big data computing in text data analysis and supervised learning: tweets text classification. And using the trained model to construct an automatic hash-tagging system for incoming tweets.

The environment and programming language of this project is [Pyspark](https://spark.apache.org/docs/latest/api/python/#:~:text=PySpark%20is%20an%20interface%20for,data%20in%20a%20distributed%20environment) with its RDD and Data Frame interface. Also, [Keras](https://keras.io/) in Tensorflow with [Pandas](https://pandas.pydata.org/) is used to train neural network models.
  
## File Descriptions
Report.ipynb: A juypter notebook file contains final presentation of data analysis and text classification with complete codes.

CommonEnglishWord.txt: a list of stopwords in English for tokenization in Nature Language Processing

otherstr.py: Support functions for RDD calculations in cetegorical variables analysis.


## Required packages
Recommend [Google Colab](https://colab.research.google.com/) to open or execuate the report. Installation of addtional requried pacakges are integerated in the Report.ipynb. 
### Pyspark
```bash
apt-get update -qq > /dev/null
apt-get install openjdk-8-jdk-headless -qq > /dev/null
wget -q https://downloads.apache.org/spark/spark-2.4.8/spark-2.4.8-bin-hadoop2.7.tgz
tar xf spark-2.4.8-bin-hadoop2.7.tgz
pip install -q findspark
```
Complete guide of installation and documentation of Pyspark can be found in the [offical website](https://spark.apache.org/docs/latest/api/python/#:~:text=PySpark%20is%20an%20interface%20for,data%20in%20a%20distributed%20environment)
### Keras (Tensorflow)
A Powerfull tool to support Neural Network Training
```bash
pip install tensorflow
from tensorflow import keras
from tensorflow.keras import layers
```
### NLTK
Nature Language Processing: stemmer, stopwords, and others
```bash
pip install nltk
from nltk.stem import PorterStemmer
```
### Matplotlib
A powerfull package for data visualization and plot
```bash
pip install matplotlib
import matplotlib.pyplot
```
### Pyecharts
Another powerfull package for interactive data visualization
```bash
pip install pyecharts
```
### Others
Also required some essential packages for data anaylsis, such as Pandas, NumPy, and others
