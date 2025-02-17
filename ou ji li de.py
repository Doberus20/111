import gmpy2
import libnum
import base64
from Crypto.Util.number import *
a=198
b=252
a1=a
b1=b
q=[1]
c=b1%a1
d=b1//a1
p=[-d]
i=0
while c!=0:
    print(i)
    b1=a1
    a1=c
    c=b1%a1
    d=b1//a1
    if(i==0):
        p.append(1-d*p[0])
        q.append(-d*q[0])
    else:
        p.append(p[i-1]-d*p[i])
        q.append(q[i-1]-d*q[i])
    print(p[i])
    print(q[i])
    i+=1
i-=1
print(a,"*",p[i],"+",b,"*",q[i],"=",a*p[i]+b*q[i])