def hamm(s1,s2):
    distance=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            distance+=1
    return distance


f=open("rosalind_hamm.txt","r")
s1=f.readline()
s2=f.readline()
f.close()

nf=open("output_hamm.txt","w")
nf.write(str(hamm(s1,s2)))
nf.close()