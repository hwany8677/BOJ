input=open(0).readline
q=int(input())
quotes=[0]
for _ in range(q): quotes.append(input().rstrip())
for _ in range(int(input())):
    r=int(input())
    print(f"Rule {r}: No such rule" if r<0 or r>q else f"Rule {r}: {quotes[r]}")