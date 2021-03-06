# 75.程式練習 對話紀錄1 - 格式改寫
# 讀取檔案

def read_file(finename):
	lines = []
	with open(finename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

# 轉換型態

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
		if person:
			new.append(person + ': ' + line + '\n')
	return new

# 存入檔案
def write_file(filename, new):
	with open(filename, 'w' ) as f:
		for line in new:
			f.write(line)

# 主程式
def main():
	lines = read_file('input.txt') # 讀取檔案
	new = convert(lines)
	write_file('output.txt', new)

main()