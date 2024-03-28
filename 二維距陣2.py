a=[int(i) for i in input().split()]
m=3
s=[]
w=0
for i in range(3):
    t=[]
    for x in range(3):
        t.append(a[w])
        w=w+1
    s.append(t)
for i in range(3):# 0 1 2
    t=[]
    for x in range(3):#0 1 2
        t.append(s[x][i]) #0 0 # 1 0 # 2 0
    t.sort()
    c=t[1]
    for x in range(3):# 0 1 2
        s[x][i]=c
print(s)

