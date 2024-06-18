#readlines: receive an input till hitting EOF from standard input
from sys import stdin
buf=stdin.readlines()
for s in buf: print(s,end='')