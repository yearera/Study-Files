def func_a(*args):
    return 1, 2, 3, 4

if __name__ == '__main__':
    a, b, c, d = func_a()
    print(a, b, c, d)