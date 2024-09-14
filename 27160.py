from sys import stdin
input=stdin.readline

card={
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0
}
n=int(input())
for _ in range(n):
    s=input().rstrip().split()
    crd=s[0]
    amt=int(s[1])
    card[crd]+=amt
for status in card.keys():
    if card[status]==5:
        print("YES")
        exit(0)
print("NO")