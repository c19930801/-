def keepFirst(a):
    arr=""
    for i in a:
        if i not in arr:
            arr=arr+str(i)
    return arr
def keepLast(a):
    arr=""
    for i in a:
        if i in arr:
            w=arr.find(i)
            arr=arr[:w]+arr[w+1:]
        arr=arr+str(i)
    return arr    
            

a=input()
print(keepFirst(a))
print(keepLast(a))