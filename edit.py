#Computation of Levenshtein distance, it returns the element in the last column-row which corresponds to the edit distance
def edit(s, t):
    if len(s) > len(t):
        s, t = t, s
    distances = range(len(s) + 1)
    for i2, c2 in enumerate(t):
        d= [i2+1]
        for i1, c1 in enumerate(s):
            if c1 == c2:
                d.append(distances[i1])
            else:
                d.append(1 + min((distances[i1],distances[i1 + 1],d[-1])))
        distances = d
        print(distances)
    return distances[-1]

from Bio import SeqIO
seqs=[]
with open("rosalind_edit.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
s=seqs[0]
t=seqs[1]
with open("output_edit.txt","w") as nf:
    nf.write(str(edit(s,t)))