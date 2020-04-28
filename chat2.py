# 75.程式練習 對話紀錄2 - 清單分割 + 計數
# 讀取檔案
def read_file(finename):
	lines = []
	with open(finename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


# 轉換型態
def convert(lines):
	allen_word_count = 0 # 文字記數=0
	allen_sticker_count = 0 # 貼圖計數=0
	allen_image_count = 0 # 圖片計數=0
	viki_word_count = 0 # 文字計數=0
	viki_sticker_count = 0 # 貼圖計數=0
	viki_image_count = 0 # 圖片計數=0
	for line in lines:
		s = line.split(' ') # 去掉空格，存入s清單
		time = s[0] # 已知s[0]為時間，定義為time
		name = s[1] # 已知s[1]為人名，定義為name
		if name == 'Allen': # 如果s[1]為'Allen'
			if s[2] == '貼圖': # 如果s[2]為'貼圖'
				allen_sticker_count += 1 # allen貼圖計數器+1
			elif s[2] == '圖片': # 如果s[2]為'圖片'
				allen_image_count += 1 # allen圖片計數器+1
			else: # 如果都不是
				for m in s[2:]: # 清單第2格之後，一行一行列出存入m
					allen_word_count += len(m) # 將m清單長度加總
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen說了', allen_word_count, '個字')
	print('Allen傳了', allen_sticker_count, '張貼圖')
	print('Allen傳了', allen_image_count, '張圖片')
	print('Viki說了', viki_word_count, '個字')
	print('Viki傳了', viki_sticker_count, '張貼圖')
	print('Viki傳了', viki_image_count, '張圖片')


# 存入檔案
def write_file(filename, new):
	with open(filename, 'w') as f:
		for line in new:
			f.write(line)


# 主程式
def main():
	lines = read_file('LINE-Viki.txt') # 讀取檔案
	new = convert(lines)

main()