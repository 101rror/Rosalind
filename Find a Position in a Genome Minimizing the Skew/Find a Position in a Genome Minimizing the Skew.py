s = input()
count = 0
ans = []
ans.append(count)

for i in s:
	if i == 'C':
		count -= 1
	elif i == 'G':
		count += 1
	
	ans.append(count)
		
minindex = min(ans)

for i in range(len(ans)):
	if ans[i] == minindex:
		print(i, end=' ')