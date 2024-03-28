def days(m,d):
    mr=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    ds=sum(mr[:m]) +d
    return ds
def weekdays(n):
    wd=(n+4)%7
    return ["星期天","星期一","星期二","星期三","星期四","星期五","星期六"][wd]
while True:
    try:
        m,d=map(int,input().split())
        print(weekdays(days(m,d)))
    except:
        break

