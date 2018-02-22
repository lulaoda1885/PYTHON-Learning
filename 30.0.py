import os

temp_list = os.listdir('.')

dir_num = 0
file_num = 1
file_list = []

for i in temp_list:
	if os.path.isdir(i):        #统计文件夹数量
		dir_num += 1
	else:
		get_ext = os.path.splitext(i)
		file_list.append(get_ext[1])        #若为文件则提取文件扩展名，存入扩展名列表

temp_list = []     #清空临时列表，为统计各扩展名数量作准备

for each in file_list:
	if each not in temp_list:     #将每种扩展名添加到临时列表中
		temp_list.append(each)
		
for each in temp_list:
	print('该文件夹下共有类型为【%s】的文件 %d 个' % (each, file_list.count(each))   #打印扩展名信息
	
print('该文件夹下共有类型为【文件夹】的文件 %d 个' % dir_num)    #打印文件夹信息