def insertion_tableau(L,v,i):
    L.append(v)
    for k in range(len(L)-1,i,-1):
        print(L)
        L[k],L[k-1]=L[k-1],L[k]

L=[1,2,3,8]
v=65
i=2
insertion_tableau(L,v,i)
print(L)


def suppression_tableau(L,i):
    
    for k in range(i,len(L)-1,-1):
        print(L)
        L[k],L[k-1]=L[k-1],L[k]
    L.pop()

L=[1,2,3,8]
i=1
suppression_tableau(L,i)
print(L)



def copietableau(x):
    c=[]
    for x in L:
        c.append(x)
    return c
L=[1,2,3,8]

copietableau(L)



def mintableau(L):
    x=L[0]
    for k in range(len(L)) :
        if x>L[k]:
            x=L[k]
    return x
L=[1,6,8,4]
mintableau(L)



def mintableautrie(L):
    return L[0]
L=[1,4,6,8]
mintableautrie(L)




def ajoutertableau(L,c):
    L.append(c)
    return L
L=[1,6,8,4]
c=5
ajoutertableau(L,c)



def ajoutertableautrier(L,c):
    for x in range (0,len(L)):
        if L[x]>=c:
            L.insert(x,c)
        else:
            L.append(c)
        return L
L=[11,12,13,14]
ajoutertableautrier(L,13)

def ajoutertableautrier(L,c):
    L.append(c)
    taille=len(L)-1
    while taille>=0 and L[taille]>c:
        L[taille+1]=L[taille]
        taille-=1
        L[taille+1]=c
L=[11,12,13,14]
ajoutertableautrier(L,10)
print(L)