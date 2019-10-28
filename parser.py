from exp import Val, Add, Sub, Mul, Div

def parse(s: str):
    if pos == -1:
        return val(int(s))
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add (parse(s1), parse(s2))

e = parse("123")
print(e.eval())

s = "123456"
pos = s.find("+")　# + 記号を探す
print('pos', pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s, s1, s2)   # + 記号で分割


def parse(s: str):
    pos = s.find('+')
    if pos == -1:
        return Val(int(s))
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1), parse(s2))

    e = parse("1+2+3")
    print(e, e.eval())