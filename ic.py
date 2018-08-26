# https://github.com/sdsunjay/kasiski/blob/master/asgn2.pdf
# usage: python ic.py N l [ l2 ... ]

from sys import argv

is_debug = False
debug = lambda *args, **kwargs: is_debug and print(*args, **kwargs)

def ic(N, d):
    return (
        0.066 * (1 / d) * (N - d) / (N - 1)
        + 0.038 * (d - 1) / d * N / (N - 1)
    )

i, k = 1, 0
N = None
keylens = []
while i < len(argv):
    if argv[i] == '-v':
        is_debug = True
        debug("debug: %d" % is_debug)
    elif argv[i][0] != '-':
        if k == 0:
            N = int(argv[i])
            debug("N: %s" % N)
        elif k > 0:
            l = int(argv[i])
            keylens.append(l)
            debug("l: %s" % l)
        k += 1
    i += 1

assert(N is not None)
assert(len(keylens) > 0)

max_len_keylen = max(map(lambda d: len(str(d)), keylens))
print("Key%s Expected IC (N=1000)" % (' ' * (max_len_keylen - 3)))
print("---%s --------------------" % ('-' * (max_len_keylen - 3)))
for d in keylens:
    v = ic(N, d)
    print(("%" + str(max_len_keylen) + "d %.4f") % (d, v))
