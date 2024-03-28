while True:
    try:
        a=[int(i) for i in input().split()]
        a.sort()
        a.reverse()
        print(a)
    except:
        break
