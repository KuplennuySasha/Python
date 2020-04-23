import math
print ("n=")
n=int(input())
a=[0]*n
b=[]
max=-100
suma=0 
for i in range(n):
    print("s",i,"=")
    a[i]=int(input())
    
for i in range(n):
    if a[i]>max:
        max=a[i]
    if a[i]%2==0 :
        suma=suma+a[i]
    if a[i]<0:
        b.append(a[i])
        
print("Videmni elementy", b[::-1])
print("suma=", suma)
print("max=", max)
