

#EX1
def trieRang(liste):
    rg={}
    l=sorted(liste.items(),key=lambda liste: liste[1],reverse=True)
    for i in range(len(l)):
        rg[i+1]=l[i]
    return(rg)
###########################################################################
import matplotlib.pyplot as plt
import string
import os
from collections import Counter
def trieRang(liste):
    rg={}
    l=sorted(liste.items(),key=lambda liste: liste[1],reverse=True)
    for i in range(len(l)):
        rg[i+1]=l[i]
    return(rg)

os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
def select(x):
    docs= os.listdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
    for x in docs:
        fichier=open(x,"r")
        t=fichier.read()
        q=t.lower()
        l=q.translate(str.maketrans({a:None for a in string.punctuation}))
        a=l.split()
        L=Counter(a)
        return (L)
dict=trieRang(select("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé"))
rang=[]
frequence=[]
for cle,valeur in dict.items():
    rang=rang+[cle]
    frequence=frequence+[valeur[1]]
plt.plot(rang,frequence)
plt.xlabel('rang')
plt.ylabel('frequence')
plt.show()

###########################################################################
import sys
import string
import os
from collections import Counter
os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
os.chdir("C://Users//u//Desktop//projetpythonSRD")
def select(x):
    fichier=open(x,"r")
    t=fichier.read()
    fichier1=open("StopList1.txt","r")
    t1=fichier1.read()
    a1=t1.split()
    q=t.lower()
    l=q.translate(str.maketrans({a:None for a in string.punctuation}))
    b=l.split()
    L=[]
    for i in b:
        if i not in a1:

            L.append(i)
            
    M=Counter(L)            
    
    return (M)

def filtre(doc):
    L=select(doc)
    nb=len(L)
    print(nb)
    a=int(nb/100)
    b=int(nb/10)
    print(a,b)
    r={}
    
    for i in L:
        if L[i]>a and L[i]<b:
            r.update({i:L[i]})
    return r
#########################################################################################

import matplotlib.pyplot as plt
import string
import os
import sys
from collections import Counter
def trieRang(liste):
    rg={}
    l=sorted(liste.items(),key=lambda liste: liste[1],reverse=True)
    for i in range(len(l)):
        rg[i+1]=l[i]
    return(rg)

os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
def select(x):
    docs= os.listdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
    for x in docs:
        fichier=open(x,"r")
        t=fichier.read()
        q=t.lower()
        l=q.translate(str.maketrans({a:None for a in string.punctuation}))
        a=l.split()
        L=Counter(a)
        return (L)
def filtre(doc):
    L=select(doc)
    nb=len(L)
    print(nb)
    a=int(nb/30)
    b=int(nb/10)
    print(a,b)
    r={}
    
    for i in L:
        if L[i]>a and L[i]<b:
            r.update({i:L[i]})
    return r
dict=trieRang(filtre(select("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")))
rang=[]
frequence=[]
for cle,valeur in dict.items():
    rang=rang+[cle]
    frequence=frequence+[valeur[1]]
plt.plot(rang,frequence)
plt.xlabel('rang')
plt.ylabel('frequence')
plt.show()
#########################################################################################################"
#ex2
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
def tf(x,y):
    f=open(x,"r")
    t=f.read()
    q=t.split()
    a=0
    for i in q:
        if i==y:
            a=a+1
    return(y,a)
############################################################################################
import math
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé")
def df(y,x):
    docs=os.listdir(y)
    a=0
    b=0
    for doc in docs:
        a=a+1
        f=open(doc,"r")
        t=f.read()
        r=t.split()
        if x in r:
            b=b+1
                
            
        idf=math.log10(a/b)
    return(idf)
########################################################################################
def ponderation(z,x,y):
    S=tf(z,x)*df(x,y)
    return(S)
#####################################################################
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé1")
def DL(y):
    docs=os.listdir(y)
    a=0
    b=0
    for doc in docs:
        a=a+1
        f=open(doc,"r")
        t=f.read()
        r=t.split()
        b=b+len(r)
    S=b/a
    return S
######################################################################
def DLDOC(z,y):
    p=open(z,"r")
    c=p.read()
    M=c.split()
    Z=(len(M)/DL(y))
    return (Z)
#####################################################"
def PondNormal(m,n,y):
    j=1.2
    o=0.75
    v=tf(m,n)*(1+j)
    u=(1-o)+o*DLDOC(m,y)
    W=v/j*u+tf(m,n)
    return W
        
        
        

                
    
    
    
