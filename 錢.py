while True:
    try:
        x,y,z=map(int,input().split())
        jj=(y+z-x)//2
        a=z-jj
        b=y-jj
        print(f"a:{a} b:{b} j:{jj}")
    except:
        break
# a+b=x
# b+jj=y
# a+jj=z
# y+z-x=jj+jj   