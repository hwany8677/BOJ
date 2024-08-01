s=sorted(list(input()))
ana=sorted(list(input()))
is_there_s=True
is_there_ana=True
#두개가 다 참이어야지만 통과
for char in s:
    if char==' ': continue
    if char not in ana:
        is_there_s=False
for char in ana:
    if char==' ': continue
    if char not in s:
        is_there_ana=False
if is_there_s and is_there_ana: print("Is an anagram.")
else: print("Is not an anagram.")