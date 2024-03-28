def use1(a):
    arr=[]
    for i in range(2,int(a)):
        if int(a)%int(i)==0:
            arr.append(i)
    ans=[]
    
    
    for i in arr:
        w=0
        for x in arr:
            print(f"i:{i} x:{x} w:{w}")
            if int(i)%int(x)==0:
                w=w+1
        if w==1:
            ans.append(i)
    return ans
a=input()
print(use1(a))