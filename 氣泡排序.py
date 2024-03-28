while True:
    try:
        a=[int(i) for i in input().split()]
        for i in range(2):
            for j in range(len(a)-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        print(a)
    except:
        break
