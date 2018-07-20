#!/usr/bin/env python3
# https://www.learnpython.org/en/Closures

def main():
    def add_5(x):
        return x+5

    def call_add_5():
        nonlocal c
        x = 1000
        c = 200
        return add_5(x) + c

    c = 100
    x = 5
    y = call_add_5()
    print(y)
    print(c)

if __name__ == '__main__':
    main()
