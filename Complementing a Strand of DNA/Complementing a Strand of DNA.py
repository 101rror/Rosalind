s = "AAAACCCGGT"
ans = ""

for i in s:
	if i == 'A':
		ans += 'T'
	elif i == 'T':
		ans += 'A'
	elif i == 'C':
		ans += 'G'
	elif i == 'G':
		ans += 'C'
		
x = ans[::-1]

print(x)