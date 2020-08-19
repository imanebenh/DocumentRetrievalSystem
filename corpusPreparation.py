import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
def contenue(x):
    fichier=open(x,"r")
    t=fichier.read()
    return t
#####################################################################
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
def contenue(x):
    fichier=open(x,"r")
    t=fichier.read()
    return t
docs=os.listdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
for doc in docs:
    print (contenue(doc))
#############################################################################
import string
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
def analyse(x):
    fichier=open(x,"r")
    t=fichier.read()
    q=t.lower()
    l=q.translate(str.maketrans({a:None for a in string.punctuation}))
    a=l.split()
    
    return (a)
##############################################################################
import string
import os
os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
def AnalyseLexicl(x):
    fichier=open(x,"r")
    t=fichier.read()
    q=t.lower()
    l=q.translate(str.maketrans({a:None for a in string.punctuation}))
    
    return (l)    
docs=os.listdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
for doc in docs:
    os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
    M=AnalyseLexicl(doc)
    os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé1")
    f1=open(doc,"w")
    t1=f1.write(M)
    f1.close()
   
    
###########################################################################"
import string
import os
from collections import Counter
os.chdir("C://Users//u//Desktop//projetpythonSRD//Corpus")
def select(x):
    fichier=open(x,"r")
    t=fichier.read()
    q=t.lower()
    l=q.translate(str.maketrans({a:None for a in string.punctuation}))
    a=l.split()
    L=Counter(a)  
    return (L)
##############################################################################
import string
import os
from collections import Counter
os.chdir("C://Users//u//Desktop//projetpythonSRD//TP1//CorpusAnalysé1")
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
 
