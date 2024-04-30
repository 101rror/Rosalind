def recur(n, k):
	if n == 0 or n == 1:
		return n
	else:
   		return recur(n - 1, k) + k * recur(n - 2, k)
   		

n, k = map(int, input().split())

ans = recur(n, k)

print(ans)