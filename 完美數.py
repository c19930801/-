def isPerfect(a):
    arr=[]
    for i in range(1,int(a)):
        if int(a)%i==0:
            arr.append(i)
    ent=""
    sun=0
    for i in arr:
        if i==arr[-1]:
            sun=sun+int(i)
            ent=ent+str(i)+"="+str(sun)
        else:
            ent=ent+str(i)+"+"
            sun=sun+int(i)
    if sun==int(a):
        return True,ent
    else:
        return False,ent

w=input()
print(isPerfect(w))
    