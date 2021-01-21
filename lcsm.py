from itertools import combinations
#return set of all possible substrings
def sub(s):
    return set(s[x:y] for x, y in combinations(range(len(s) + 1), r = 2))

def lcsm(d):
    d1=sub(list(d.values())[0])
    d2=sub(list(d.values())[1])
    #intersect sets to find common substrings
    inter=d1.intersection(d2)
    #sort from longest to shortest
    s_inter=sorted(inter,key=len,reverse=True)
    #check each substring in intersection with all dna present in dictionary, if substring is present in all the dna in the dictionary -> return the substring
    for ss in s_inter:
        if all(ss in dna for dna in list(d.values())[2:]):
            return(ss)

fasta={}
with open("rosalind_lcsm.txt", 'r') as f:
    for line in f:
        if line.startswith('>'):
            key=line[1:-1]
            fasta[key]=""
        else:
            fasta[key]+=line.strip()
nf=open("output_lcsm.txt","w")
nf.write(lcsm(fasta))
nf.close()