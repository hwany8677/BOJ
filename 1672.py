#Naive code
#Memory & time hungry (Got MLE on PyPy3)
comb={
    "A": {"A": "A", "G": "C", "C": "A", "T": "G"},
    "G": {"A": "C", "G": "G", "C": "T", "T": "A"},
    "C": {"A": "A", "G": "T", "C": "C", "T": "G"},
    "T": {"A": "G", "G": "A", "C": "G", "T": "T"}
}
n=int(input())
s=list(input())
for i in range(n-1,0,-1):
    an=s[i]
    an_1=s[i-1]
    new=comb[an][an_1]
    s[i]=''
    s[i-1]=new
for char in s: print(char,end='')
print()
