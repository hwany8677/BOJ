#Qwerty!!
# QWERTYUIOP
# ASDFGHJKL
# ZXCVBNM
#Shift one step, when it reaches the end shift to the beginning
to_shift={
    'Q':'W','W':'E','E':'R','R':'T','T':'Y','Y':'U','U':'I','I':'O','O':'P','P':'Q',
   'A':'S','S':'D','D':'F','F':'G','G':'H','H':'J','J':'K','K':'L','L':'A',
    'Z':'X','X':'C','C':'V','V':'B','B':'N','N':'M','M':'Z'
}
s=input()
res=''
for char in s:
    if ord(char)>64 and ord(char)<91: res+=to_shift[char]
    else: res+=char
print(res)