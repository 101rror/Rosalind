from collections import defaultdict 

s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
lst = list(s)
lst.sort()
mp = defaultdict(int)

for i in lst:
	mp[i] += 1
	
for i in mp.values():
	print(i, end=" ")