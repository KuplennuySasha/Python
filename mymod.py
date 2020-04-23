def do():
    print ('n=')
    n=int(input())
    a=[0]*n
    s=0
    for i in range(n):
        print("a[",i,"]=")
        a[i]=int(input())
    for i in range(n):
        s=s+a[i]
        ser=s/n
    print("ser=", ser)
