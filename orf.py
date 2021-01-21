#find codons of the three possible reads and directly translates them into proteins
def orf(rna):
    d={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}
    proteins=[]
    orfs=[rna,rna[1:],rna[2:]]
    #start=0
    #print(orfs)
    for e in orfs:
        #print(e)
        for i in range(0,len(e),3):
            #print('Start '+ str(start) + '; Actual i: ' + str(i))
            protein=''
            if e[i:i+3] in d:
                if d[e[i:i+3]]=='M':
                    protein+=d[e[i:i+3]]
                    for i2 in range(i+3,len(e),3):
                        if e[i2:i2+3] in d:
                            if d[e[i2:i2+3]]=='Stop':
                                #start=i2+3
                                proteins.append(protein)
                                break
                            else:
                                protein+=d[e[i2:i2+3]]

    return proteins

#Returns reverse complement
def revc(dna):
    r_dna=dna[::-1]
    old="ATGC"
    new="TACG"
    table=r_dna.maketrans(old,new)
    return r_dna.translate(table)

from Bio import SeqIO
seq=""
rna1=""
rna2=""
result=set()
with open("rosalind_orf.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seq=str(e.seq)

#Proteins from dna itself        
rna1=seq.replace('T','U')
result.update(orf(rna1))
#print('RNA1: '+rna1)

#Proteins from reverse complement
seq2=revc(seq)
rna2=seq2.replace('T','U')
result.update(orf(rna2))

with open("output_orf.txt", 'w') as nf:
    nf.write('\n'.join(result))
