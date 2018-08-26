# https://github.com/sdsunjay/kasiski/blob/master/asgn1.pdf
# usage: python ftable.py [ -v ] [ -s num ] [ -p num ] [ infile [ outfile ] ]

from sys import argv
import re
import math

is_debug = False
debug = lambda *args, **kwargs: is_debug and print(*args, **kwargs)

def normalize(s):
    s = s.strip().upper()
    s = re.sub(r'[^A-Z]+', '', s)
    return s

def ftable(s, skip = 0, period = 1):
    s = normalize(s)

    slen = 0
    count = [0 for i in range(26)]
    for i in range(skip, len(s), period):
        slen += 1
        count[ord(s[i]) - 65] += 1

    out = "Total chars: %d\n" % slen
    for c, n in enumerate(count):
        c = chr(c + 65)
        percent = 100.0 * n / slen
        out += "%s: %10d (%6.2f%%) %s\n" % (c, n, percent, '*' * math.ceil(percent))

    ic = (
        1.00 / (slen * (slen - 1))
        * sum([f * (f - 1) for f in count])
    )
    out += "\nIndex of Coincidence: %.4f\n" % ic

    return out

i, k = 1, 0
skip = 0
period = 1
infile, outfile = None, None
while i < len(argv):
    if argv[i] == '-v':
        is_debug = True
        debug("debug: %d" % is_debug)
    elif argv[i] == '-s':
        i += 1
        skip = int(argv[i])
        debug("skip: %d" % skip)
    elif argv[i] == '-p':
        i += 1
        period = int(argv[i])
        debug("period: %d" % period)
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

out = ftable(s, skip, period)
if outfile is None:
    print(out)
else:
    with open(outfile, 'w') as f:
        f.write(out)

