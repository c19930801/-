def toBin(n):
    s=""
    while n>0:
        s=str(n%2)+s 
        n=n//2
    s="0"*(20-len(s)) + s 
    return s
def distance(s1,s2):
    d=0
    for i in range(20):
        if s1[i]!=s2[i]:
            d+=1
        return d
    
s=[int(i) for i in input().split()]
s1=toBin(s[0])
s2=toBin(s[1])
print(s1)
print(s2)
print(distance(s1,s2))