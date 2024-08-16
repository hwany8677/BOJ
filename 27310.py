s=input()
diff=0
col=0
for c in s:
    if c=='_': diff+=1
    if c==':': col+=1
diff*=5
diff+=col
diff+=len(s)
print(diff)