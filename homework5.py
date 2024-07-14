"""
a
b
c
ab
bc
abc
"""


def all_variants(text):
    n = 0
    while n <= 0:
        for lit in text:
            yield lit
        n += 1


a = all_variants("abc")
for i in a:
    print(i)
