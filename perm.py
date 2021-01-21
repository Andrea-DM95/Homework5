from itertools import permutations 
def perm(n):
    return list(permutations(range(1,n+1)))

f=open("rosalind_perm.txt","r")
n=int(f.readline())
f.close()
per=perm(n)
nf=open("output_perm.txt","w")
nf.write(str(len(per)))
nf.write('\n')
for subl in per:
    for item in subl:
        nf.write(str(item)+' ')
    nf.write('\n')
nf.close()