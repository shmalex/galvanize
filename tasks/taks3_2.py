def char_enc(a):
    if not str.isalpha(a):
        return a
    c = ord(a) + 1
    if (c == 91):
        c == 65
    if (c == 123):
        c = 97
    return chr(c)


def char_dec(a):
    if not str.isalpha(a):
        return a
    c = ord(a) - 1
    if (c == 94):
        c == 91
    if (c == 96):
        c = 123
    return chr(c)


def encode(text):
    return ''.join([char_enc(c) for c in text])


def decode(text):
    return ''.join([char_dec(c) for c in text])

o = 'asd 1 j;lk'
print(o)
c = encode(o)
print(c)
d = decode(c)
print(d)
