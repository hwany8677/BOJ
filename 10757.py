#Filthy code
#import os
a,b=map(list,input().split())
""" ^^^
https://stackoverflow.com/a/78183456
WHY VSCODE EVEN HAVE THE LIMIT AT THE FIRST PLACE?? U BRAINDEAD OR STH?
WTF DUDE :(
"""
n=len(a) if len(a)>len(b) else len(b) #Longest number first
sum=[0 for i in range(0,10000)]
lenA,lenB=len(a),len(b)
a.reverse()
b.reverse()
#print(f"Input length (A,B): ({lenA},{lenB})")
for i in range(0,n): #Reverse
    #Index out of range workaround
    if i>lenA-1: a.append(0)
    if i>lenB-1: b.append(0)
    #End of workaround
    temp=int(a[i])+int(b[i])+sum[i] #Digit calculation
#    if (i>=6380): print(f"\nDigit number {i+1} (list index no.{i})")
#    if (i>=6380): print(f"Raw digit sum: {temp}")
#    if (i>=6380): print(f"A: {a[i]}, B: {b[i]}, Extra 1: {sum[i]==1}")
    if temp>=10: 
        sum[i+1]+=1
        sum[i]=temp-10
#        if (i>=6380): 
#            print("\nTossed '1' to the next digit")
#            print(f"To confirm: index no.{i+1}'s current digit is: {sum[i+1]}\n")
    else: sum[i]=temp
#    if (i>=6380): print(f"Current digit sum: {sum[i]}\n")
#    if (i>=6380): os.system("pause")
sum.reverse()
buf=[]
startPoint=0
for i in range(0,10000): 
    if sum[i]!=0:
        startPoint=i
        break
#print(f"startPoint: {startPoint}")
for i in range(startPoint,10000): buf.append(str(sum[i]))
for b in buf: print(b,end='')
#f=open("./meh.txt","w")
#f.write(f"startPoint: {startPoint}\n")
#for i in buf: f.write(f"{i}")
#f.close()