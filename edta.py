#s serves as rows, t as columes
#define Levenshtein Distance Table
def edta(s,t):
    rows=len(s)+1
    columes=len(t)+1
    table=[[0 for x in range(columes)] for y in range(rows)]
    for i in range(1,rows):
        table[i][0]=i
    for j in range(1,columes):
        table[0][j]=j
    for j in range(1,len(t)+1):
        for i in range(1,len(s)+1):
            if s[i-1]==t[j-1]:
                subCost=0
            else:
                subCost=1
            table[i][j]= min(table[i-1][j]+1,table[i][j-1]+1,table[i-1][j-1]+subCost)
    #for i in range(len(table)):
    #  print(table[i])
    return table

#the fuction decodes the table into the optimal alignment following a set of rule in which from the last row,column the matrix backtracks until the position 0,0 is reached
#in order for my set of rule to properly work the number of rows needs to be major or equal to the number of columns
def decoding(s,t,table,row,column):
    current=table[row][column]
    if row==0 and column==0:
        return '',''
    if column==0:
        s1,t1=decoding(s,t,table,row-1,column)
        return s1+s[row-1], t1+'-'
    if row==0:
        s1,t1=decoding(s,t,table,row,column-1)
        return s1+'-',t1+t[column-1]

    if current>=table[row-1][column] and table[row-1][column]<table[row-1][column-1]:
        s1,t1=decoding(s,t,table,row-1,column)
        return s1+s[row-1], t1+'-'
    
    if current>=table[row-1][column-1] and table[row-1][column-1]<=table[row][column-1]:
        s1,t1=decoding(s,t,table,row-1,column-1)
        return s1+s[row-1],t1+t[column-1]
    
    s1,t1=decoding(s,t,table,row,column-1)
    return s1+'-',t1+t[column-1]

from Bio import SeqIO
seqs=[]
with open("rosalind_edta.txt", 'r') as f:
    for e in SeqIO.parse(f,'fasta'):
        seqs.append(str(e.seq))
if seqs[0]>seqs[1]:
    s=seqs[0]
    t=seqs[1]
else:
    s=seqs[1]
    t=seqs[0]

table=edta(s,t)
s1,t1=decoding(s,t,table,len(s),len(t))

with open("output_edta.txt","w") as nf:
    nf.write(str(table[len(s)][len(t)]))
    nf.write('\n')
    nf.write(t1)
    nf.write('\n')
    nf.write(s1)