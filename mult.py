from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62
scoring={('A','A'):0,('A','T'):-1,('A','G'):-1,('A','C'):-1,('T','T'):0,('T','G'):-1,('T','C'):-1,('G','G'):0,('G','C'):-1,('C','C'):0}

#makes alignment following matching dictionary provided
def glob (s,t):
    alignments = pairwise2.align.globalds(s, t, scoring,-1,-1)
    a=set()
    b=set()
    for e in alignments:
        a.add(e.seqA)
        b.add(e.seqB)
    return a, b

#Cycles through possibilities and create dictionary with scores of all possible combinations

def d_score(a,b,c,d):
    sd={}
    for x in range(len(a)):
        la=len(a[x])
        for y in range(len(b)):
            lb=len(b[y])
            for z in range(len(c)):
                lc=len(c[z])
                for j in range(len(d)):
                    ld=len(d[j])
                    if la==lb==lc==ld:
                        e=score(a[x],b[y],c[z],d[j])
                        k=(a[x],b[y],c[z],d[j])
                        if k in sd:
                            sd[k]+=e
                        else:
                            sd[k]=e
    return sd

#Scores combinations of words with mismatched -1 and match 0
def score(a,b,c,d):
    result=[a,b,c,d]
    score=0
    for e1 in range(len(result)-1):
        for e2 in range(e1+1, len(result)):
            #print('comparison {} {}'.format(e1,e2))
            for i in range(len(result[0])):
                if result[e1][i]!=result[e2][i]:
                    score-=1
    return score


from Bio import SeqIO
seqs=[]
with open("rosalind_mult.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
a=seqs[0]
b=seqs[1]
c=seqs[2]
d=seqs[3]
possible_a=set()
possible_b=set()
possible_c=set()
possible_d=set()

#All possible comparisons
a1,b1=glob(a,b)
possible_a.update(a1)
possible_b.update(b1)

a1,c1=glob(a,c)
possible_a.update(a1)
possible_c.update(c1)

a1,d1=glob(a,d)
possible_a.update(a1)
possible_d.update(d1)

b1,c1=glob(b,c)
possible_b.update(b1)
possible_c.update(c1)

b1,d1=glob(b,d)
possible_b.update(b1)
possible_d.update(d1)

c1,d1=glob(c,d)
possible_c.update(c1)
possible_d.update(d1)

#SCORE COMBINATIONS
possible_a=list(possible_a)
possible_b=list(possible_b)
possible_c=list(possible_c)
possible_d=list(possible_d)
d=d_score(possible_a,possible_b,possible_c,possible_d)

#Sort dictionary by scoring and make it a list
sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)

#Result
print(sorted_d[0])
final_result=sorted_d[0]

with open("output_mult.txt", "w") as nf:
    nf.write(str(final_result[1]))
    nf.write('\n')
    for e in final_result[0]:
        nf.write(e)
        nf.write('\n')
