from exp import Val, Add, Sub, Mul, Div
def parse(s: str):
    num = int(s)
    return val(num)

e = parse("123")
print(e)

s = "123456"
pos = s.find("+")　# + 記号を探す
print('pos', pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s, s1, s2)   # + 記号で分割


def parse(s: str):
    pos = s.find('+')
    if pos == -1:
        num = int(s)
        return Val(int(s))
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(Val(int(s1)), Val(int(s2)))

    e = parse("1+2+3")
    print(e, e.eval())