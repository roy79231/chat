

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	allen_word_count = 0
	viki_word_count = 0
	for line in lines :
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen' :
			if s[2] == '貼圖' :
				continue
			if s[2] == '圖片' :
				continue
			if s[2] == '未接來電' :
				continue
			else :
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki' :
			if s[2] == '貼圖' :
				continue
			if s[2] == '圖片' :
				continue
			if s[2] == '未接來電' :
				continue
			else :
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen說了',allen_word_count)
	print('viki說了',viki_word_count)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)


main()