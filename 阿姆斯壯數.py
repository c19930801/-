def Arms(a):
    arr=0
    b=int(len(a))
    ans=""
    for i in a:
        arr=arr+(int(i)**b)
        print(f"arr:{arr},i:{i},b:{b}")
        ans=ans+str(i)+"**"+str(b)+" + "
        if i==a[-1]:
            ans=ans+str(i)+"**"+str(b)
    if arr==int(a):
        ans="True ("+ans+" = "+str(arr)+", 等於自己)"
    else:
        ans="False ("+ans+" = "+str(arr)+", 不等於自己)"
    return ans
a=input()
print(Arms(a))