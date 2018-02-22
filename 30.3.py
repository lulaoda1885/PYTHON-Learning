import os

videolist_txt = open('E:/videolist.txt', 'x+')

search_path = input('请输入待查找的初始目录：')

dest = ['.mp4', '.rmvb', '.avi']   #需要查找的目标后缀名

for (r, d, f) in os.walk(search_path):
	for each in f:
		if os.path.splitext(each)[1] in dest:
			file_path = os.path.join(r, each)
			videolist_txt.writelines(file_path)   #将视频文件路径写入文本
			videolist_txt.writelines('\n')      #在文本中各行之间增加一行空行
			
videolist_txt.close()