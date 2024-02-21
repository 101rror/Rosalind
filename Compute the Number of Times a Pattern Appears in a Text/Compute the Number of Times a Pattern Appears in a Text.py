s = input()
p = input()

slen = len(s)
plen = len(p)

count = 0

for i in range(slen + 1 - plen):
	check = s[i : i + plen]
	
	if(check == p):
		count += 1
		
print(count)