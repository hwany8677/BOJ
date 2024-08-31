s=input()
if '-' not in s:
    s=s.split('+')
    sigma=0
    for num in s: sigma+=int(num)
    print(sigma)
    exit(0)
elif '+' not in s:
    s=s.split('-')
    sigma=0
    for num in s: sigma-=int(num)
    print(sigma)
    exit(0)
