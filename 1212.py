octs={
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111"
}
n_oct=input()
res=""
for i in range(len(n_oct)):
    digit=n_oct[i]
    if i==0: print(int(octs[digit]),end='')
    else: print(octs[digit],end='')
print()