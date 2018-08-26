# Vigenere Break Cipher Tools

Tools for breaking a vigenere cipher. Read more about them in [asgn 1](https://github.com/sdsunjay/kasiski/blob/master/asgn1.pdf) and [asgn 2](https://github.com/sdsunjay/kasiski/blob/master/asgn2.pdf)

They come in very handy for solving [OverTheWire Krypton challenges](http://overthewire.org/wargames/krypton/)

More resources:
- [dcode.fr](https://www.dcode.fr/vigenere-cipher)
- [the guy from whom I "borrowed" the assignment](https://github.com/sdsunjay/kasiski)
- [overthewire](http://overthewire.org/)

## Usage
```bash
$ python vig.py [ -v ] [ -d ] key [ infile [ outfile ] ]
$ python ftable.py [ -v ] [ -s num ] [ -p num ] [ infile [ outfile ] ]
$ python ic.py N l [ l2 ... ]
$ python kasisky.py [ -v ] [ -m length ] [ infile [ outfile ] ]
```

## Frequency Table`ftable.py`
```
$ python ftable.py -s 1 -p 6 krypton4.in
Total chars: 242
A:          0 (  0.00%)
B:          1 (  0.41%) *
C:          7 (  2.89%) ***
D:          0 (  0.00%)
E:         12 (  4.96%) *****
F:         19 (  7.85%) ********
G:          2 (  0.83%) *
H:          0 (  0.00%)
I:         12 (  4.96%) *****
J:         14 (  5.79%) ******
K:         32 ( 13.22%) **************
L:          2 (  0.83%) *
M:          3 (  1.24%) **
N:          8 (  3.31%) ****
O:          0 (  0.00%)
P:          7 (  2.89%) ***
Q:          0 (  0.00%)
R:         16 (  6.61%) *******
S:          2 (  0.83%) *
T:          6 (  2.48%) ***
U:         16 (  6.61%) *******
V:         35 ( 14.46%) ***************
W:          7 (  2.89%) ***
X:          4 (  1.65%) **
Y:         19 (  7.85%) ********
Z:         18 (  7.44%) ********

Index of Coincidence: 0.0743
```

## Kasiski Examination for finding the key length `kasisky.py`
```
$ python kasiski.py krypton4.in
Length  Count  Word        Factor  Location (distance)
======  =====  ==========  ======  ===================
     3      8         YYI       6  0 312 (312) 432 (120) 444 (12) 504 (60) 558 (54) 954 (396) 1020 (66)
     3      4         ICS       2  2 608 (606) 644 (36) 1060 (416)
     3     11         XRI       6  14 44 (30) 56 (12) 86 (30) 98 (12) 278 (180) 830 (552) 878 (48) 1292 (414) 1358 (66) 1388 (30)
     3      3         RIE       6  15 99 (84) 1389 (1290)
     3      3         FNJ       6  23 125 (102) 173 (48)
     3      3         VHD       6  31 205 (174) 373 (168)
     3      3         HDL       6  32 206 (174) 374 (168)
     3     10         DLC       6  33 75 (42) 111 (36) 207 (96) 243 (36) 375 (132) 1179 (804) 1251 (72) 1263 (12) 1413 (150)
     3      3         LYX      16  42 1274 (1232) 1338 (64)
     3      4         IQY       2  46 560 (514) 592 (32) 1306 (714)
     3      3         QYI       1  47 480 (433) 593 (113)
     3      4         UXR      24  85 829 (744) 877 (48) 1357 (480)
     3      4         RIP       6  87 279 (192) 879 (600) 1293 (414)
     3      3         LCW       6  94 364 (270) 1180 (816)
     3      3         SFJ       2  108 970 (862) 1188 (218)
     3      3         LCL      24  112 208 (96) 376 (168)
     3      3         JNM       1  119 456 (337) 882 (426)
     3      3         NXF       6  123 1143 (1020) 1425 (282)
...
```
