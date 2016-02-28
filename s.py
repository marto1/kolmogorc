def p(exp):
    return lambda: exp


def r(elem, limit):
    return "".join([elem for x in range(limit)])
