k=input()
if len(k)<2:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit(0)

prevCha=int(k[1])-int(k[0])
for i in range(1,len(k)):
    if int(k[i])-int(k[i-1])!=prevCha:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        exit(0)
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")