##Note: I used the article en.wikipedia.org/wiki/Longest_common_subsequence_problem to understand the algorithm and program it

#Compute the length on the longest common subsequence in a table
#FIXED
def lcs_len(a,b):
    columes=len(a)+1
    rows=len(b)+1
    table=[[0 for x in range(rows)] for y in range(columes)]
    for i in range(1,columes):
        for j in range(1,rows):
            if a[i-1]==b[j-1]:
                table[i][j]=(table[i-1][j-1])+1
            else:
                table[i][j]=max(table[i][j-1],table[i-1][j])
    return table

#Compute and returns one of the longest common subsequence by backtracking the table
#FIXED
def lcsq(table,a,b,i,j):
    if i==0 or j==0:
        return ""
    elif a[i-1]==b[j-1]:
        return lcsq(table,a,b,i-1,j-1)+ a[i-1]
    elif table[i][j-1]>table[i-1][j]:
        return lcsq(table,a,b,i,j-1)
    return lcsq (table, a, b, i-1, j)

from Bio import SeqIO
seqs=[]
with open("rosalind_lcsq.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
a=seqs[0]
b=seqs[1]
table=lcs_len(a,b)
with open("output_lcsq.txt","w") as nf:
    nf.write(lcsq(table,a,b,len(a),len(b)))