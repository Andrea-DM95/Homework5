#Function returns a direct graph 'On' in which there is an edge when v1 has a suffix of len n that corresponds to a prefix in v2 of the same len
def grph(d,n):
    grph=[]
    for k1,v1 in d.items():
        for k2,v2 in d.items():
            if v1!=v2:
                if v1[-n:]==v2[:n]:
                    grph.append(k1+' '+ k2)
    return grph

from Bio import SeqIO
d={}
with open("rosalind_grph.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        d[e.id]=str(e.seq)
with open("output_grph.txt", 'w') as nf:
    nf.write('\n'.join(grph(d,3)))