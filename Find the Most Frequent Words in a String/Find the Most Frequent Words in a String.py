from collections import defaultdict 
count = 0
mp = defaultdict(int)


s = input()
k = int(input())

slen = len(s)

for i in range(0, slen + 1 - k):
	check = s[i : i + k]
	
	mp[check] += 1
	
fre = max(mp.values())

for key, value in mp.items():
	if value == fre:
		print(key, end=" ")