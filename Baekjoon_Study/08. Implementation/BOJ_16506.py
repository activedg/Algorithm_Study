import sys
inp = lambda : sys.stdin.readline()
opcode = {'ADD' : '00000', 'ADDC' : '00001', 'SUB' : '00010', 'SUBC' : '00011', 'MOV' : '00100', 'MOVC' : '00101',
          'AND' : '00110', 'ANDC' : '00111', 'OR' : '01000', 'ORC' : '01001', 'NOT' : '01010', 'MULT' : '01100',
          'MULTC' : '01101', 'LSFTL' : '01110', 'LSFTLC' : '01111', 'LSFTR' : '10000', 'LSFTRC' : '10001',
          'ASFTR' : '10010', 'ASFTRC' : '10011', 'RL' : '10100', 'RLC' : '10101', 'RR' : '10110', 'RRC' : '10111'
          }
# opcode rD rA rB 혹은 opcode rD rA #C 형태
# rA 사용하지 않으면 000 (MOV, MOVC, NOT)
# #C가 아니면 15비트에 0 추가
res = []

def dec2hex(num, digit):
    res = ['0'] * digit
    # 10
    ## 1010
    cur = 0
    while num:
        div = 2 ** (digit - cur - 1)
        if num >= div:
            res[cur] = '1'
            num -= div
        cur += 1
    return ''.join(res)
for _ in range(int(inp())):
    line = inp().split()
    op, num = line[0], line[1:]
    ## opcode 에 c 포함
    temp = ''
    x, y, z = int(num[0]), int(num[1]), int(num[2])
    temp += opcode[op] + '0'
    temp += dec2hex(x, 3)
    if op == 'MOV' or op =='MOVC' or op =='NOT':
        temp += '000'
    else:
        temp += dec2hex(y, 3)

    if op[-1] == 'C':
        temp += dec2hex(z, 4)
    else:
        temp += dec2hex(z, 3) + '0'
    res.append(temp)
for r in res:
    print(r)