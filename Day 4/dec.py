def apply_decorator(func):
    return lambda x: func(x) + 10

@apply_decorator
def add_five(n):
    return n + 5

print(add_five(3))
