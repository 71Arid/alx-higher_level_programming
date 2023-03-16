def add_tuple(tuple_a=(), tuple_b=()):
    tupled = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + tupled[len[tuple_a]:]
    if len(tuple_b) < 2:
        tuple_b = tuple_b + tupled[len(tuple_b):]
    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    if tuple_a is None:
        return tuple_b
    elif tuple_b is None:
        return tuple_a
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        return (a, b)
