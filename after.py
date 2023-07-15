# Used learnings from https://www.arjancodes.com/products/the-software-designer-mindset-complete-extension/categories/2149347727/posts/2158457410#
import functools
from typing import Callable

ComposableFunction = Callable[[float],float]

def compose(*functions: ComposableFunction)-> ComposableFunction:
    return functools.reduce(lambda f,g : lambda x: g(f(x)), functions)

def add_three(x:float)->float:
    return  x + 3

def add_five(x:float)->float:
    return  x + 5

def multiply_by_two(x:float)->float:
    return  x * 2

def add_n(x:float, n: float)->float:
    return  x + n


def main():
    x = 12 # starting value
    print(f'Before : {x}' )

    add_twenty = functools.partial(add_n, n=20)
    math_fns = compose(add_three, add_three, add_five, multiply_by_two, add_twenty)
    result = math_fns(x)
    print(f'After math\'ing : {result}' )


if __name__ == '__main__':
    main()