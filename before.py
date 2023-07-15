

def add_three(x:float)->float:
    return  x + 3

def add_five(x:float)->float:
    return  x + 5

def add_multiply_by_two(x:float)->float:
    return  x * 2

def add_n(x:float, n: float)->float:
    return  x + n


def main():
    x = 12 # starting value
    print(f'Before : {x}' )
    x = add_three(x)
    x = add_three(x)
    x = add_five(x)
    x = add_multiply_by_two(x)
    x = add_n(x,20) # add 20
    print(f'After math\'ing : {x}' )


if __name__ == '__main__':
    main()