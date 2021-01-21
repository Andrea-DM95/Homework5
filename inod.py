#the number of internal nodes in any unrooted binary tree having n leaves is n-2 
def inod(n):
    return n-2

with open("rosalind_inod.txt", 'r') as f:
    n= int(f.readline())
print(inod(n))