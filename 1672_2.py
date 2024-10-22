#If-else hellscape?
n=int(input())
s=list(input())
for i in range(n-1,0,-1):
    an=s[i]
    an_1=s[i-1]
    if an=="A":
        if an_1=="A": new="A"
        elif an_1=="G": new="C"
        elif an_1=="C": new="A"
        elif an_1=="T": new="G"
    elif an=="G":
        if an_1=="A": new="C"
        elif an_1=="G": new="G"
        elif an_1=="C": new="T"
        elif an_1=="T": new="A"
    elif an=="C":
        if an_1=="A": new="A"
        elif an_1=="G": new="T"
        elif an_1=="C": new="C"
        elif an_1=="T": new="G"
    elif an=="T":
        if an_1=="A": new="G"
        elif an_1=="G": new="A"
        elif an_1=="C": new="G"
        elif an_1=="T": new="T"
    s[i]=''
    s[i-1]=new
for char in s: print(char,end='')
print()
