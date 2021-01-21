def tran(seqs):
    s1=seqs[0]
    s2=seqs[1]
    tran=[('A','C'),('C','A'),('G','T'),('T','G'),('A','T'),('T','A'),('G','C'),('C','G')]
    transvertions=0
    transitions=0

    #zip() returns list of tuple if list of same lenght
    for compare in zip(s1,s2):
        #print(compare)
        if compare[0]!=compare[1]:
            #print(compare in tran)
            if compare in tran:
                transvertions+=1
            else:
                transitions+=1
    #print(transitions)
    #print(transvertions)
    return (transitions/transvertions)

from Bio import SeqIO
seqs=[]
with open("rosalind_tran.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
with open("output_tran.txt", 'w') as nf:
    nf.write(str(tran(seqs)))