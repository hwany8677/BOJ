msg={"CU": "see you", 
     ":-)": "I’m happy", 
     ":-(": "I’m unhappy",
     ";-)": "wink",
     ":-P": "stick out my tongue",
     "(~.~)": "sleepy",
     "TA": "totally awesome",
     "CCC": "Canadian Computing Competition",
     "CUZ": "because",
     "TY": "thank-you",
     "YW": "you’re welcome",
     "TTYL": "talk to you later"}
while(1):
    s=input()
    try:
        print(msg[s])
    except:
        print(s)
    if s=="TTYL": break