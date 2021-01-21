def prot(rna):
    d={"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V","UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V","UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A","UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A","UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D","UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E","UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G","UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"}
    protein=''
    for i in range(0,len(rna),3):
        if d[rna[i:i+3]]=="Stop":
            return protein
        else:
            protein+=d[rna[i:i+3]]
    return protein


fasta={}
with open("rosalind_splc.txt", 'r') as f:
    for line in f:
        if line.startswith('>'):
            key=line[1:-1]
            fasta[key]=""
        else:
            fasta[key]+=line.strip()
dna=list(fasta.values())[0]
remove=list(fasta.values())[1:]
exons=dna
for e in remove:
    exons=exons.replace(e,'',1)
rna=exons.replace('T','U')
with open('output_splc.txt', 'w') as nf:
    nf.write(prot(rna))