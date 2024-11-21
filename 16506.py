input=open(0).readline
opcode={
    "ADD": "000000",
    "ADDC": "000010",
    "SUB": "000100",
    "SUBC": "000110",
    "MOV": "001000",
    "MOVC": "001010",
    "AND": "001100",
    "ANDC": "001110",
    "OR": "010000",
    "ORC": "010010",
    "NOT": "010100",
    "MULT": "011000",
    "MULTC": "011010",
    "LSFTL": "011100",
    "LSFTLC": "011110",
    "LSFTR": "100000",
    "LSFTRC": "100010",
    "ASFTR": "100100",
    "ASFTRC": "100110",
    "RL": "101000",
    "RLC": "101010",
    "RR": "101100",
    "RRC": "101110"
}
for _ in range(int(input())):
    buf=input().rstrip().split()
    op_code=buf[0]
    rD=bin(int(buf[1])).split('b')[1].zfill(3)
    rA=bin(int(buf[2])).split('b')[1].zfill(3)
    if op_code[len(op_code)-1]=='C': 
        hashC=bin(int(buf[3])).split('b')[1].zfill(4)
        op_code=opcode[op_code]
        print(op_code+rD+rA+hashC)
    else: 
        rB=bin(int(buf[3])).split('b')[1].zfill(3)+'0'
        op_code=opcode[op_code]
        print(op_code+rD+rA+rB)