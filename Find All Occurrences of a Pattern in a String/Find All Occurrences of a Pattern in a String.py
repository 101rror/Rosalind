p = input()
s = input()

plen = len(p)
slen = len(s)

ans = []

for i in range(0, slen + 1 - plen):
	check = s[i : i + plen]
	
	ans.append(check)

for i in range(len(ans)):
	if ans[i] == p:
		print(i, end=" ")