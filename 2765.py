#Imperials << sra
input=open(0).readline
pi=3.1415927
dia,rev,t=input().split()
dia=float(dia)
rev=int(rev)
t=float(t)
case=1
while(rev!=0):
    dist_inch=dia*pi*rev
    dist_ft=dist_inch/12
    dist_mi=dist_ft/5280
    print(f"Trip #{case}:", "{:.2f}".format(dist_mi), "{:.2f}".format(dist_mi/t*3600))
    dia,rev,t=input().split()
    dia=float(dia)
    rev=int(rev)
    t=float(t)
    case+=1
