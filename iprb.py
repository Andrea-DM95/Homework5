from itertools import product
def iprb(k,m,n):
    #hd=['AA']
    #he=['Aa']
    #hr=['aa']
    parents=['AA']*k +['Aa']*m+['aa']*n
    #print(len(parents))
    #print(parents)
    population=0
    good_childrens=0
    for x in range(len(parents)):
        for y in range(x+1,len(parents)):
            childrens=list(product(parents[x],parents[y]))
            #print(list(childrens))
            for e in childrens:
                if 'A' in e:
                    good_childrens+=1
            population+=len(childrens)
    return(good_childrens/population)

with open("rosalind_iprb.txt", 'r') as f:
    a,b,c= map(int,f.readline().split())
print(iprb(a,b,c))