def sseq(seqs):
    a=seqs[0]
    b=seqs[1]
    result=[]
    pos=-1
    for i in range(len(b)):
        pos=a.find(b[i],pos+1)
        if pos==-1:
            return None
        else:
            result.append(str(pos+1))
    return result

from Bio import SeqIO
seqs=[]
with open("rosalind_sseq.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
with open("output_sseq.txt","w") as nf:
    nf.write(' '.join(sseq(seqs)))