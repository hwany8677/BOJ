s=input()
while(s!='.'):
    expected_stack=[]
    no_match=False
    for char in s:
        if char=='(': expected_stack.append(')')
        if char=='[': expected_stack.append(']')
        if char==')' or char==']':
            if len(expected_stack)==0:
               no_match=True
               break
            else: expected=expected_stack.pop()
            if expected!=char:
                no_match=True
                break
    if no_match: print("no")
    elif len(expected_stack)>0: print("no")
    else: print("yes")
    s=input()
