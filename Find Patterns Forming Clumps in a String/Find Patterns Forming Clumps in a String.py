from collections import defaultdict 

def Sub(s, L):
    slen = len(s)
    ans = []
    
    for i in range(slen - L + 1):
        x = s[i : i + L]
        ans.append(x)
      
    return(ans)
    
    
def most(s, k):
	slen = len(s)
	mp = defaultdict(int)
	
	for i in range(0, slen + 1 - k):
		check = s[i : i + k]
	
		mp[check] += 1

	return mp


s = input()
k, L, t = map(int, input().split())

lst = Sub(s, L)
ans = []

for i in lst:
	newmp = most(i, k)
	
	for key, value in newmp.items():
		if value == t:
			ans.append(key)
		
st = set(ans)
	
for i in st:
	print(i, end=" ")
		



