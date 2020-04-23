import math
print ("a=")
a=int(input())
print ("b=")
b=int(input())
if a>=15:
    z=math.sin (2*a)+math.cos(2*b)
elif a<15:
    z=math.sqrt(a+(b*b))
print("z=", z)
