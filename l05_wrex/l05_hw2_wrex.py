# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

line = " "
num_of_lines = 0
num_of_words = 0
eof = 0
try:
	with open("l05_hw2_text.txt", "r") as f:
		while not eof:
			line = f.readline()
			if line:
				num_of_lines += 1
				num_of_words = len(line.split())
				print(f"Line {num_of_lines} content {num_of_words} words")
			else:
				eof = 1
				print(f"Lines total: {num_of_lines}")

except:
	print(f"--Can't read file 'l05_wh2_text.txt'")