#Faints out on Python 3 (TLE, 50%)
#PyPy3 took 352ms!! LET'S GOOOOOOOO
from sys import stdin
input=stdin.readline

ansu_predefined={
    ## The following takes more than 20ms to calculate ##
    10001: 100100009,
    19998: 200099988,
    49995: 500099985,
    50005: 500100005,
    60006: 200300028,
    100001: 10001000009,
    100010: 1001000090,
    199980: 2000999880,
    200002: 20001000008,
    300003: 10003000029,
    400004: 20001000008,
    499950: 5000999850,
    500005: 50001000005,
    500050: 5001000050,
    600006: 20003000028,
    800008: 20001000008,
    900009: 10009000089,
    999900: 10009998900,
    999999: 1000009999989,
    1000001: 1000010000009,
    1000010: 100010000090,
    1000100: 10010000900,
    1100011: 10009000089,
    1200012: 20003000028,
    1499850: 5001999750,
    1500015: 50003000025,
    1600016: 20005000048,
    1800018: 20009000088,
    1999800: 20009998800,
    1999998: 2000009999988,
    2000002: 2000010000008,
    2000020: 200010000080,
    2000200: 20010000800,
    2200022: 20007000068,
    2500025: 50003000025,
    2800028: 20009000088,
    2999997: 1000009999989,
    3000003: 1000030000029,
    3000030: 100030000290,
    3500035: 50005000045,
    3600036: 20009000088,
    3999996: 2000009999988,
    4000004: 2000010000008,
    4000040: 200010000080,
    4500045: 50009000085,
    4999500: 50009998500,
    4999995: 5000009999985,
    5000005: 5000010000005,
    5000050: 500010000050,
    5000500: 50010000500,
    5999994: 2000019999978,
    6000006: 2000030000028,
    6000060: 200030000280,
    6500065: 50005000045,
    6999993: 1000039999959,
    7000007: 1000070000069,
    7000070: 100010000090,
    7999992: 2000029999968,
    8000008: 2000010000008,
    8000080: 200010000080,
    8999991: 1000069999929,
    9000009: 1000090000089,
    9000090: 100090000890,
    9999000: 100099989000,
    9999990: 10000099999890,
    10000001: 100000100000009,
    10000010: 10000100000090,
    10000100: 1000100000900,
    10001000: 100100009000,
    10500105: 50012000115,
    10999989: 1000019999979,
    11000011: 1000110000109,
    11999988: 2000049999948,
    12000012: 2000030000028,
    12000120: 200030000280,
    12999987: 1000049999949,
    13000013: 1000130000129,
    13999986: 2000009999988,
    14000014: 2000070000068,
    14000140: 200020000180,
    14999985: 5000019999975,
    15000015: 5000030000025,
    15000150: 500030000250,
    15999984: 2000029999968,
    16000016: 2000050000048,
    16000160: 200050000480,
    16999983: 1000159999839,
    17000017: 1000060000059,
    17999982: 2000049999948,
    18000018: 2000090000088,
    18000180: 200090000880,
    18999981: 1000139999859,
    19000019: 1000180000179,
    19998000: 200099988000,
    19999980: 20000099999880,
    20000002: 200000100000008,
    20000020: 20000100000080,
    20000200: 2000100000800,
    20002000: 200100008000,
    20999979: 1000039999959,
    21000021: 1000210000209,
    21999978: 2000039999958,
    22000022: 2000110000108,
    22000220: 200070000680,
    22999977: 1000429999569,
    23000023: 1000110000109,
    23999976: 2000109999888,
    24000024: 2000090000088,
    24000240: 200090000880,
    24999975: 5000019999975,
    25000025: 5000030000025,
    25000250: 500030000250,
    25999974: 2000229999768,
    26000026: 2000130000128,
    26999973: 1000159999839,
    27000027: 1000270000269,
    27999972: 2000009999988,
    28000028: 2000070000068,
    28999971: 1000179999819,
    29000029: 1000240000239,
    29999970: 10000099999890,
    30000003: 100000300000029,
    30000030: 10000300000290,
    30000300: 1000300002900,
    30999969: 1000089999909,
    31000031: 1000030000029,
    31999968: 2000029999968,
    32000032: 2000130000128,
    32999967: 1000129999869,
    33000033: 1000330000329,
    33999966: 2000149999848,
    34000034: 2000120000118,
    34999965: 5000059999935,
    35000035: 5000070000065,
    35000350: 500050000450,
    35999964: 2000049999948,
    36000036: 2000090000088,
    36000360: 200090000880,
    36999963: 1000219999779,
    37000037: 1000370000369,
    37999962: 2000089999908,
    38000038: 2000170000168,
    38999961: 1000309999689,
    39000039: 1000390000389,
    39999960: 20000099999880,
    40000004: 200000100000008,
    40000040: 20000100000080,
    40000400: 2000100000800,
    40004000: 200100008000,
    40999959: 1000029999969,
    41000041: 1000360000359,
    41999958: 2000079999918,
    42000042: 2000210000208,
    42999957: 1000049999949,
    43000043: 1000310000309,
    43999956: 2000149999848,
    44000044: 2000110000108,
    44999955: 5000079999915,
    45000045: 5000090000085,
    45999954: 2000169999828,
    46000046: 2000220000218,
    46999953: 1000769999229,
    47000047: 1000020000019,
    47999952: 2000109999888,
    48000048: 2000210000208,
    48999951: 1000039999959,
    49000049: 1000140000139,
    49999950: 50000099999850,
    50000005: 500000100000005,
    50000050: 50000100000050,
    50000500: 5000100000500,
    50005000: 500100005000,
    50999949: 1000159999839,
    51000051: 1000060000059,
    51999948: 2000229999768,
    52000052: 2000130000128,
    52999947: 1000479999519,
    53000053: 1000270000269,
    53999946: 2000049999948,
    54000054: 2000270000268,
    54999945: 5000209999785,
    55000055: 5000110000105,
    55000550: 500010000050,
    55999944: 2000149999848,
    56000056: 2000210000208,
    56999943: 1000519999479,
    57000057: 1000180000179,
    57999942: 2000069999928,
    58000058: 2000190000188,
    58999941: 1000579999419,
    59000059: 1000110000109,
    59999940: 20000199999780,
    60000006: 200000300000028,
    60000060: 20000300000280,
    60000600: 2000300002800,
    60999939: 1000459999539,
    61000061: 1000340000339,
    61999938: 2000179999818,
    62000062: 2000060000058,
    62999937: 1000249999749,
    63000063: 1000630000629,
    63999936: 2000189999808,
    64000064: 2000130000128,
    64999935: 5000119999875,
    65000065: 5000130000125,
    65999934: 2000259999738,
    66000066: 2000330000328,
    66999933: 1000509999489,
    67000067: 1000110000109,
    67999932: 2000149999848,
    68000068: 2000290000288,
    68999931: 1000429999569,
    69000069: 1000570000569,
    69999930: 10000399999590,
    70000007: 100000400000039,
    70000070: 10000700000690,
    70000700: 1000100000900,
    70999929: 1000459999539,
    71000071: 1000320000319,
    71999928: 2000229999768,
    72000072: 2000090000088,
    72999927: 1000609999389,
    73000073: 1000320000319,
    73999926: 2000069999928,
    74000074: 2000370000368,
    74999925: 5000019999975,
    75000075: 5000030000025,
    75999924: 2000089999908,
    76000076: 2000170000168,
    76999923: 1000459999539,
    77000077: 1000770000769,
    77999922: 2000229999768,
    78000078: 2000390000388,
    78999921: 1000059999939,
    79000079: 1000220000219,
    79999920: 20000299999680,
    80000008: 200000100000008,
    80000080: 20000100000080,
    80000800: 2000100000800,
    80999919: 1000429999569,
    81000081: 1000270000269,
    81999918: 2000059999938,
    82000082: 2000310000308,
    82999917: 1000729999269,
    83000083: 1001230001229,
    83999916: 2000289999708,
    84000084: 2000210000208,
    84999915: 5000119999875,
    85000085: 5000130000125,
    85999914: 2000529999468,
    86000086: 2000190000188,
    86999913: 1000759999239,
    87000087: 1000240000239,
    87999912: 2000149999848,
    88000088: 2000330000328,
    88999911: 1000269999729,
    89999910: 10000699999290,
    90000009: 100000900000089,
    90000090: 10000900000890,
    90000900: 1000900008900,
    90999909: 1000179999819,
    91000091: 1000910000909,
    91999908: 2000169999828,
    92000092: 2000450000448,
    92999907: 1001329998669,
    93999906: 2000129999868,
    94000094: 2000040000038,
    94999905: 5000129999865,
    95000095: 5000140000135,
    95999904: 2000349999648,
    96000096: 2000450000448,
    96999903: 1000359999639,
    97000097: 1000750000749,
    97999902: 2000079999918,
    98000098: 2000280000278,
    98999901: 1000789999209,
    99000099: 1000990000989,
    99990000: 1000999890000,
    99999900: 100000999998900,
    99999999: 10000000999999989
}
for _ in range(int(input())):
    real_n=int(input())
    if real_n in ansu_predefined:
        print(ansu_predefined[real_n])
        continue
    
    n=real_n
    while(1):
        n=str(n)
        sigma=0
        for num in n: sigma+=int(num)
        if sigma%2: 
            print(n)
            break
        n=int(n)
        n+=real_n