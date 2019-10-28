e = parse("1")
assert e.eval() == 1

e = parse("1+2")
assert e.eval() == 3

parse("1")
parse("1+2")
parse("1+2+3")

parse("1*2+3")
parse("1+2*3")
