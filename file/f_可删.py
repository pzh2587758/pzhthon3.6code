#!python3 /bin/ect/
a, b = 0,1
while b < 10000000:
    print(b,end=" ")
    a,b = b,a+b
