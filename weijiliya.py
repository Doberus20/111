letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def lenth_of_key(c, max_key_lenth):
    Ic = []
    for i in range(1, max_key_lenth+1):
        c1 = c[1::i]
        lenth = len(c1)
        count = {}
        Ic1 = 0
        for j in letterlist:
            count[j] = c1.count(j)
            Ic1 += count[j] * (count[j] - 1)
        Ic1 = Ic1 / (lenth * (lenth - 1))
        Ic.append(Ic1)
    print(Ic)
    print("密钥长度为：",Ic.index(max(Ic))+1)
    return( Ic.index(max(Ic))+1)
def interval_of_key(c,key_lenth):
    C = [c[i::key_lenth] for i in range(key_lenth)]
    MIc = [[] for i in range(key_lenth)]
    key_interval = [0]
    for i in range(1, key_lenth):
        for j in range(26):
            MIc1 = 0
            for k in letterlist:
                k1 = letterlist.index(k)
                k2 = letterlist[(k1 - j) % 26]
                MIc1 += C[0].count(k) * C[i].count(k2)
            MIc1 /= (len(C[i]) * len(C[0]))
            MIc[i - 1].append(MIc1)
    for i in range(1, key_lenth):
        print(i, ":", MIc[i - 1])
        print("偏移为：",MIc[i - 1].index(max(MIc[i - 1])))
        key_interval.append(-(MIc[i - 1].index(max(MIc[i - 1])) ))
    return key_interval
def Decryption(c,max_key_lenth):
    c=list(c)
    key_lenth = lenth_of_key(c, max_key_lenth)
    key_interval = interval_of_key(c, key_lenth)
    print("可能的明文为：")
    for i in range(26):
        K = key_interval
        for j in range(key_lenth):
            K[j] = (K[j] + i) % 26
        c1 = list(c)
        C1 = [c1[i::key_lenth] for i in range(key_lenth)]
        for j in range(key_lenth):
            for i, k in enumerate(C1[j]):
                C1[j][i] = letterlist[(letterlist.index(k) - K[j]) % 26]
        for h in range(len(c1)):
            c1[h] = C1[h % key_lenth][h // key_lenth]
        print("".join(c1))
def Encryption(m,key):
    m=list(m)
    key_lenth=len(key)
    M=[m[i::key_lenth] for i in range(key_lenth)]
    for i in range(key_lenth):
        for j in range(len(M[i])):
            M[i][j]=letterlist[(letterlist.index(M[i][j])+key[i])%26]
    for i in range(len(m)):
        m[i]=M[i%key_lenth][i//key_lenth]
    return "".join(m)
def Decryption_ifUnoK(c,key):
    c = list(c)
    key_lenth = len(key)
    C = [c[i::key_lenth] for i in range(key_lenth)]
    for i in range(key_lenth):
        for j in range(len(C[i])):
            C[i][j] = letterlist[(letterlist.index(C[i][j]) - key[i]) % 26]
    for i in range(len(m)):
        c[i] = C[i % key_lenth][i // key_lenth]
    return "".join(c)
