def dep(A,I):
    D=[]
    for i in range(len(A)):
        for j in range(len(A)):
            D.append((A[i],A[j]))

    for e in I:
        if e in D: D.remove(e)
    return D

def emptyy(l):
    for e in l:
        if e: return False
    return True

def fnf(A,w,D):
    k=[]
    for i in range(len(A)): k.append([])

    for i in range(len(w)-1,-1,-1):
        for e in D:
            if e[0]==w[i] and e[1]!=w[i]:
                k[ord(e[1])-97].append('*')
        k[ord(w[i])-97].append(w[i])

    res=[]
    while(not emptyy(k)):
        str=""
        for i in range(len(k)):
            x=''
            if k[i] and k[i][-1]!='*': x=k[i].pop()
            str+=x
        for i in range(len(str)):
            for el in D:
                if el[0]==str[i] and el[1]!=str[i] and k[ord(el[1])-97]: k[ord(el[1])-97].pop()
        res.append(str)
    return res

def graph(w,D):
    h=[]
    e=[]
    min=[]
    for i in range(len(w)-1,-1,-1):
        min.append(i)
        for x in min:
            if x!=i and (w[i],w[x]) in D:
                h.append((i+1,x+1))
        e.append((i+1,w[i]))

    for k in h:
        for l in h:
            if l!=k:
                if k[1]==l[0] and (k[0],l[1]) in h: h.remove((k[0],l[1]))
                if k[0]==l[1] and (l[0],k[1]) in h: h.remove((l[0],k[1]))
    return h,e

def draw(v,e):
    rys="digraph g{\n"
    v.sort(key=lambda t:t[0])
    for k in v:
        rys+="  "+str(k[0])+" -> "+str(k[1])+"\n"

    e.sort(key=lambda t:t[0])
    for x in e:
        rys+="  "+str(x[0])+"[label="+x[1]+"]\n"
    rys+="}"
    return rys

def fnf2(v,e2):
    res=[[v[0][0]],[v[0][1]]]
    for i in range(1,len(v)):
        dep=False
        k=v[i]

        for x in range(len(res)):
            for e in res[x]:
                if e==k[0]:
                    dep=True
                    if x!=len(res)-1:
                        res[x+1].append(k[1])
                    else: res.append([k[1]])

        if dep==False:
            res[0].append(k[0])
            res[1].append(k[1])

    check=[]
    for i in range(len(res)-1,-1,-1):
        for x in res[i]:
            if x in check: res[i][res[i].index(x)]='*'
            else: check.append(x)
        while '*' in res[i]: res[i].remove('*')

    for i in range(len(res)):
        for x in res[i]:
            for el in e2:
                if el[0]==x: res[i][res[i].index(x)]=el[1]

    for i in range(len(res)):
        str=""
        for x in res[i]:
            str+=x
        res[i]=str
    return res

def init(file):
    f=open(file)
    lines=f.readlines()
    f.close()
    A=lines[0][3:-2].split(',')
    tmp=lines[1][4:-2].split(')')

    I=[]
    for i in range(len(tmp)-1):
        if i==0: (x,y)=(tmp[i][0],tmp[i][2])
        else: (x,y)=(tmp[i][2],tmp[i][4])
        I.append((x,y))
    w=lines[2][2:-1]
    return(A,I,w)

print("Enter the name of an input file (d1.txt, d2.txt, d3.txt):")
file=input()
(A,I,w)=init(file)
D=dep(A,I)
F=fnf(A,w,D)
(h,e)=graph(w,D)
g=draw(h,e)
h.sort(key=lambda t:t[0])
F2=fnf2(h,e)

f=open("graph.dot","w")
f.write(g)
f.close()

print()
print("Dependency relation D:")
print(D)
print()
print("FNF from D:")
print(F)
print()
print("FNF from graph:")
print(F2)
