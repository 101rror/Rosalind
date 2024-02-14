s = "GATGGAACTTGACTACGTAAATT"
ans = ""

for i in s:
	if i == 'T':
		ans += 'U'
	else:
		ans += i

print(ans)