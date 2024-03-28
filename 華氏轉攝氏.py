while True:
    try:
        f=int(input("請輸入一個數字:"))
        c=(f-32)*5/9
        if c>=0:
           c=int(c)
        else:
            c=-(int(-c))
        print(int(c))
    except:
        break