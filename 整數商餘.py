while True:
    try:
        a,b=map(int,input("請輸入兩個數字:").split())
        print("a//b",a%b)
    except:
        break
