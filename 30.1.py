import os

temp_list = [x for x in os.listdir() if os.path.isfile(x)]

for each in temp_list:
	print('%s 【%dBytes】' %(each, os.path.getsize(each)))