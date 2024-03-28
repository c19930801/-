a=input()
a=a.split()
so=0
sx=0
for i in range(0,6+1,3): # 0 3 6 # 0 1 2= o # 3 4 5= o #  6 7 8 =o
    if a[0+i]==a[1+i]==a[2+i]=="O":
        so+=1
for i in range(0,3):# 0 1 2 # 0 3 6 # 1 4 7
    if a[0+i]==a[3+i]==a[6+i]=="O":
        so+=1
if a[0]==a[4]==a[8]=="O":
    so+=1
if a[2]==a[4]==a[6]=="O":
    so+=1
for i in range(0,6+1,3):
    if a[0+i]==a[1+i]==a[2+i]=="X":
        sx+=1
for i in range(0,3):
    if a[0+i]==a[3+i]==a[6+i]=="X":
        sx+=1
if a[0]==a[4]==a[8]=="X":
    sx+=1
if a[2]==a[4]==a[6]=="X":
    sx+=1
if so>sx:
    print("X")
elif so<sx:
    print("O")
else:
    print("平")