import os 
import re
import sys
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt

def tfidf():
	corpus = []	#存放语料
	file = codecs.open('token_result.txt','r', 'utf-8')
	line = file.readline()
	#读取文件内容到corpus中
	while line != "":
		#line = line.decode('utf-8', 'ignore')
		line = line.encode('utf-8').decode('utf-8', 'ignore')
		corpus.append(line.strip())
		try:
			line = file.readline()
			#line = line.encode('utf-8')
		except Exception as e:
			print('aaaaa')
			
	vectorizer = CountVectorizer()
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
	word = vectorizer.get_feature_names()
	weight = tfidf.toarray()
	
	resName = 'tfidf_Result.txt'
	result = codecs.open(resName, 'w', 'utf-8')
	for j in range(len(word)):
		result.write(word[j]+'\t')
	result.write('\r\n')
		
	#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重    
	for i in range(len(weight)):  
		#print("-------这里输出第",i,u"类文本的词语tf-idf权重------")
		for j in range(len(word)):  
			result.write(str(weight[i][j]) + '\t')  
		result.write('\r\n') 
	
	file.close()		
	#[print(c) for c in corpus]
	clf = KMeans(n_clusters=7)  
	s = clf.fit(weight)  
	print(clf)  
	#plt.clf()
	#print(clf.labels_)
	return clf.labels_
	#print(len(corpus))
#tfidf()