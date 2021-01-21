def pdst (seqs):
    pdst=[]
    lenght=len(seqs[0])
    for s1 in seqs:
        l=[]
        for s2 in seqs:
            distance=0
            for i in range(lenght):
                if s1[i]!=s2[i]:
                    distance+=1
            l.append(distance/lenght)
        pdst.append(l)
    return pdst
    
from Bio import SeqIO
seqs=[]
with open("rosalind_pdst.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
with open("output_pdst.txt", 'w') as nf:
    for l in pdst(seqs):
        nf.write(" ".join(map(str,l)))
        nf.write("\n")