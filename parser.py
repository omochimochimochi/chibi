e = parse("1")
assert e.eval() == 1

e = parse("1+2")
assert e.eval() == 3