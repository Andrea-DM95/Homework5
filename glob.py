from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62

def glob (s,t):
    #we use a global aligment (global) in which the score is assign by the dictionary blosum62 (d), each gap symbol counts as -5
    
    alignments = pairwise2.align.globalds(s, t, blosum62, -5, -5)
    #print(alignments)
    return int(alignments[0].score)

from Bio import SeqIO
seqs = []
with open("rosalind_glob.txt", 'r') as f:
    for e in SeqIO.parse(f, 'fasta'):
        seqs.append(e.seq)
s = seqs[0]
t = seqs[1]
with open ("output_glob.txt", 'w') as nf:
    nf.write(str(glob (s,t)))