#the minimun number of edges in a tree is nodes-1
def tree(n,e):
    return (n-1)-(e)

with open("rosalind_tree.txt", 'r') as f:
    n=int(f.readline())
    edges=[]
    for line in f.readlines():
        edges.append(line.split())
with open("output_tree.txt","w") as nf:
    nf.write(str(tree(n,len(edges))))