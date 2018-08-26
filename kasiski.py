# https://github.com/sdsunjay/kasiski/blob/master/asgn2.pdf
# usage: python kasisky.py [ -v ] [ -m length ] [ infile [ outfile ] ]
# python kasiski.py krypton4.in | awk '{print $4}' | tail -n+3 | sort -nu | factor

from sys import argv
import re
import math

is_debug = False
debug = lambda *args, **kwargs: is_debug and print(*args, **kwargs)

def normalize(s):
    s = s.strip().upper()
    s = re.sub(r'[^A-Z]+', '', s)
    return s

def kasiski(s, min_num = 3):
    s = normalize(s)
    out = ''

    matches = []
    found = {}
    for k in range(min_num, len(s) // 2):
        found[k] = {}
        shouldbreak = True
        for i in range(0, len(s) - k):
            v = s[i:i+k]
            if v not in found[k]:
                found[k][v] = 1
            else:
                found[k][v] += 1
                shouldbreak = False

        if shouldbreak:
            break

        for v in found[k]:
            if found[k][v] > 2:
                matches.append(v)

    out += "Length  Count  Word        Factor  Location (distance)\n"
    out += "======  =====  ==========  ======  ===================\n"
    keylens = {}
    for v in matches:
        k = len(v)
        p = []
        for i in range(len(s)):
            if s[i:i+k] == v:
                p.append(i)

        # assuming len(p) > 1
        factor = p[1] - p[0]
        for i in range(2, len(p)):
            factor = math.gcd(factor, p[i] - p[i - 1])

        locations = ""
        for i in range(len(p)):
            locations += "%d " % p[i]
            if i > 0:
                locations += "(%d) " % (p[i] - p[i-1])

        out += "%6d  %5d  %10s  %6d  %s\n" % (k, found[k][v], v, factor, locations)

    return out

i, k = 1, 0
min_num = 3
infile, outfile = None, None
while i < len(argv):
    if argv[i] == '-v':
        is_debug = True
        debug("debug: %d" % is_debug)
    elif argv[i] == '-m':
        i += 1
        min_num = int(argv[i])
        debug("min_num: %d" % min_num)
    elif argv[i][0] != '-':
        if k == 0:
            infile = argv[i]
            debug("infile: %s" % infile)
        elif k == 1:
            outfile = argv[i]
            debug("outfile: %s" % outfile)
        k += 1
    i += 1

s = None
if infile is None:
    s = input()
else:
    with open(infile, 'r') as f:
        s = f.read()

out = kasiski(s, min_num)
if outfile is None:
    print(out)
else:
    with open(outfile, 'w') as f:
        f.write(out)

