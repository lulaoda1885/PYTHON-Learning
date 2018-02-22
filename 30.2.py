import os

search_path = input('请输入待查找的初始目录：')
file_name = input('请输入需要查找的目标文件：')

for (r, d, f) in os.walk(search_path):
	for each in f:
		if each == file_name:
			print(os.path.join(r, each))