isbn=input()
isbn_num_w_o_missing=0
weight=1
for i in range(13):
    num=isbn[i]
    if num.isnumeric()==False: weight=3 if i%2 else 1
    elif i%2: isbn_num_w_o_missing+=int(num)*3
    else: isbn_num_w_o_missing+=int(num)
for n in range(10):
    if (isbn_num_w_o_missing+n*weight)%10==0:
        print(n)
        exit(0)
