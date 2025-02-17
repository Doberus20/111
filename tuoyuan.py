import gmpy2
import libnum
import base64
from Crypto.Util.number import *
import math
import  hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import socket
import hashlib
import itertools
import string
import sympy as sp
import numpy as np
a=497
n=9739
P=[4726,6287]
k=6534
def dianjia(a,b,a1,n):
    if((a[0]==0)*(a[1]==0)):
        return b
    if((b[0]==0)*(b[1]==0)):
        return a
    if((a[0]==b[0])*(a[1]==-b[1])):
        return[0,0]
    if((a[0]==b[0])*(a[1]==b[1])):
        g=(3*a[0]*a[0]+a1)*libnum.invmod(2*a[1],n)
    else:
        g=(b[1]-a[1])*libnum.invmod(b[0]-a[0],n)
    x3=(g*g-a[0]-b[0])%n
    y3=g*(b[0]-x3)-b[1]
    return [x3%n,y3%n]
def diancheng(p,k,a1,n):
    b=[p[0],p[1]]
    c=[0,0]
    while k>0:
        if k%2==1:
            c=dianjia(c,b,a1,n)
        b=dianjia(b,b,a1,n)
        k=k//2
    return c
print(diancheng(P,k,a,n))
