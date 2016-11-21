'''
聚类结果显示
'''
from sklearn.cluster import KMeans 
import tfidf
import codecs
import os

def cluster_result():
	cluster_labels = tfidf.tfidf()
	f_file_name = codecs.open('f_filename.txt', 'r', 'utf-8')
	list_name = []
	output_file = 'cluster_result.txt'
	if os.path.exists(output_file): #存在文件，删除后重新建
		os.remove(output_file)
	result = codecs.open(output_file, 'w', 'utf-8')
	output = ['']*7
	for line in f_file_name.readlines():
		list_name.append(line)
	#print(cluster_labels)
	for i in range(len(cluster_labels)):
		output[cluster_labels[i]] += list_name[i]
		
	for i in range(len(output)):
		result.write(str(i)+':\r\n'+output[i])
	result.close()
cluster_result()	