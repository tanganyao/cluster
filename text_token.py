
#import nltk
from nltk.corpus import PlaintextCorpusReader
import codecs
import os
import sys
import jieba
import jieba.analyse
#import chardet

def preprocess():
	
	corpus_root = "H:\\Text_represent\\复旦新闻分类\\train\\"
	pathlists = PlaintextCorpusReader(corpus_root, '.*')
	token_result = "token_result.txt"	#保存分词结果文件
	f_filename = "f_filename.txt"
	if os.path.exists(token_result): #存在文件，删除后重新建
		os.remove(token_result)
	result = codecs.open(token_result, 'w', 'utf-8')
	filename_result = codecs.open(f_filename, 'w', 'utf-8')
	i = 0
	for path in pathlists.fileids():
		abs_path  = corpus_root + path.split('/')[0] + "\\" + path.split('/')[1]
		filename_result.write(path.split('/')[1]+ '\r\n')
		file = codecs.open(abs_path, 'r', 'gb2312')
		line = file.readline()
		#line = line.encode('utf-8')
		#print(type(line))
		if i:
			result.write("\r\n")
		i = 1	#每行都一个文件
		result.write(path.split('/')[1]+' ')
		while line != "":
			#line = str(line) 
			#chardet.detect(line)
			#line = line.encode('utf-8').decode('utf-8', 'ignore')
			seglist = jieba.cut(line,cut_all=False)	#精确模式  
			output = ' '.join(list(seglist))		#空格拼接  
			output = output.replace('\n','')  
			output = output.replace('\r','') 
			result.write(output)
			try:  
				line = file.readline()
			except Exception as e:  
				print("读取错误")
			
		else:
			file.close()
		#print(file)
		#break
	filename_result.close()	
	result.close()
preprocess()