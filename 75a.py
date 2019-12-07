#!/usr/bin/python

t = int(raw_input())

for _ in range(t):
	
	#read a line 
	text = list(raw_input())
	#determin which are correct
	if len(text) == 1:
		print text[0]
	else:
		#indexs
		indexs = [1 for _ in text]
		jump = 0
		for i in range(len(text)-1):
			if text[i] == text[i+1] and jump == 0:
				indexs[i] = 0
				indexs[i+1] = 0
				jump = 1
			else:
				jump = 0
		#output
		#res_list = [text[i] for i in len(text) if indexs[i] == 1]
		res_list = []
		for i in range(len(text)):
			if indexs[i] == 1:
				res_list.append(text[i])
		res_list = set(res_list)
		print ''.join(sorted(res_list))