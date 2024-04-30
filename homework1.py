def test():
    a = False
    b = 100
    print(a, b, "- function 'test' local print")


def test2(a, b=True, c=150):
    print(a, b, c, "- function 'test2' local print")


test()
print()
test2([True, "LIST"], 200, c="String")
