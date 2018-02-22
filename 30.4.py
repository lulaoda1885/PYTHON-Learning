import os

def seek_keyword(full_path, keyword):
	
	f = open(full_path)
	
	line_num = 1
	seq_num = []
	
	if keyword in f:
		print('在文件【%s】中找到关键字【%s】' % (full_path, keyword))
		
	for each_line in f:
		if keyword in each_line:        #逐行遍历关键字
			seq = 1
			for each_word in each_line:    #逐字遍历关键字
				if each_word == keyword:
					seq_num.append(seq)
				seq += 1
			print('关键字出现在第 %d 行，第 ' % line_num, seq_num, ' 个位置')
		line_num += 1
	
	f.close()


cur_dir = os.getcwd()    #获取当前工作路径
OK = ['YES', 'yes', 'Yes']
file_type = ['.txt', '.TXT']

keyword = input('请将该脚本放于待查找的文件夹内，请输入关键字：')

print('请问是否需要打印关键字【%s】在文件夹中的具体位置（YES/NO）' % keyword)

if input() in OK:
	
	print('=====================================')
	
	for (r, d, f) in os.walk(cur_dir):
		for each_file in f:
			if os.path.splitext(each_file)[1] in file_type:      #判断是否文本文件
				full_path = os.path.join(r, each_file)           #获取文本文件完整路径
				seek_keyword(full_path, keyword)                 #调用查找函数进行查找和打印
				