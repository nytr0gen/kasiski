# https://github.com/sdsunjay/kasiski/blob/master/asgn1.pdf
# usage: python vig.py [ -v ] [ -d ] key [ infile [ outfile ] ]
from sys import argv
import re

is_upper = lambda c: 65 <= ord(c) < 91
is_lower = lambda c: 97 <= ord(c) < 123
is_alpha = lambda c: is_upper(c) or is_lower(c)

is_debug = False
debug = lambda *args, **kwargs: is_debug and print(*args, **kwargs)

def normalize(s):
    s = s.strip().upper()
    s = re.sub(r'[^A-Z]+', '', s)
    return s

def cipher(s, key):
    key = normalize(key)
    keylen = len(key)

    ret = ''
    k = 0
    for c in s:
        if is_alpha(c):
            c = chr(
                (ord(c.upper()) + ord(key[k % keylen]) - 2 * 65) % 26
                + 65
            )
            k += 1
        ret += c

    return ret

def decipher(s, key):
    key = normalize(key)
    keylen = len(key)

    ret = ''
    k = 0
    for c in s:
        if is_alpha(c):
            c = chr(
                (ord(c.upper()) - ord(key[k % keylen]) + 26) % 26
                + 65
            )
            k += 1
        ret += c

    return ret

i, k = 1, 0
key = None
is_decipher = False
infile, outfile = None, None
while i < len(argv):
    if argv[i] == '-v':
        is_debug = True
        debug("debug: %d" % is_debug)
    elif argv[i] == '-d':
        is_decipher = True
        debug("decipher: %d" % is_decipher)
    elif argv[i][0] != '-':
        if k == 0:
            key = argv[i]
            debug("key: %s" % key)
        elif k == 1:
            infile = argv[i]
            debug("infile: %s" % infile)
        elif k == 2:
            outfile = argv[i]
            debug("outfile: %s" % outfile)
        k += 1
    i += 1

assert(key is not None)

s = None
if infile is None:
    s = input()
else:
    with open(infile, 'r') as f:
        s = f.read()

if not is_decipher:
    s = cipher(s, key)
else:
    s = decipher(s, key)

if outfile is None:
    print(s)
else:
    with open(outfile, 'w') as f:
        f.write(s)

