#!/usr/bin/env python3
# https://www.learnpython.org/en/Closures

def main():
    val = 10000

    def closure(val_mod):
        nonlocal val
        val = 0
        val += val_mod
        print('closure(): val=', val)

        def fn_inside_closure(val_mod_2):
            print('fn_inside_closure(): val=', val)
            return val + val_mod_2

        return fn_inside_closure

    run_closure(closure_fn=closure, val_mod=2)

def run_closure(closure_fn, val_mod):
    fn_from_closure = closure_fn(val_mod=val_mod)
    print(fn_from_closure(5))

    fn_from_closure_2 = closure_fn(val_mod=10)
    print(fn_from_closure_2(5))
    print(fn_from_closure(5))

if __name__ == '__main__':
    main()
