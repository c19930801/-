def prime(a):
    b=(int(i) for i in range(2,a) if a%i==0 and isprime(i))
    return b
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def isugly(n):
    for i in prime(a):
        if i not in [2,3,5]:
            return False
    return True
a=int(input())
print(isugly(a))