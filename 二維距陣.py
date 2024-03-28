a=input()
a=[i for i in a.split()]
m=int(len(a)**0.5)
b=[]
k=0
for i in range(m):
    t=[]
    for j in range(m):
        t.append(a[k])
        k+=1
    b.append(t)

def symmetric(b):
    for i in range(m): #0 1 2
        for j in range(m): #0 1 2
            if b[i][j] !=b[j][i]: 
                return False
    return True
print(symmetric(b))