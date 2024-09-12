#Little John started a farm
#Needs galvanized square steel :fire::fire:
#And eco-friendly wood veneers for the fence
#Then screw them down with screws borrowed from his aunt
from sys import stdin
input=stdin.readline

k,n=map(int,input().split())
buf=[]
for _ in range(k):
    buf.append(list(map(int,input().split())))
#Need to try EVERY combination possible
#Starting from cow no.1
