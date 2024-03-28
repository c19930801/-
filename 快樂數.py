
def happy(a):
    t=[]
    while True:
        x=(int(i)**2 for i in str(a))
        arr=sum(x)
        if arr==1:
            return True
            break
        if arr in t:
            return False
            break 
        t.append(arr)
        a=arr
w=input()
print(happy(w))