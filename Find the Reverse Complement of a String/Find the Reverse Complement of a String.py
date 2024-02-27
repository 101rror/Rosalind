def comp(s):
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
            
    return ans


def rev(s):
    ans = s[::-1]
    
    return ans
    
s = input()
comps = comp(s)
revcomp = rev(comps)


print(revcomp)