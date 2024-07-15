"""
a
b
c
ab
bc
abc
"""


def all_variants(text):
    n = 1
    while n <= len(text):
        res = ''
        for lit in text:
            res += lit
            if len(res) > n:
                res = lit
                yield res
            elif len(res) == n:
                yield res
                res = lit
        n += 1


a = all_variants("abc")
for i in a:
    print(i)
