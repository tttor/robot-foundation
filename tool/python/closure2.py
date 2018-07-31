#!/usr/bin/env python3
# https://www.learnpython.org/en/Closures

def main():
    val = 10

    def closure(val_mod):
        nonlocal val
        val += val_mod
        print('closure(): val=', val)

        def fn_inside_closure(val_mod_2):
            resp = val + val_mod_2
            print('fn_inside_closure(): resp=', resp)
            return resp

        return fn_inside_closure

    run_closure(closure_fn=closure, val_mod=2)

def run_closure(closure_fn, val_mod):
    fn_from_closure = closure_fn(val_mod=val_mod)
    print(fn_from_closure(5))

    fn_from_closure_2 = closure_fn(val_mod=2)
    print(fn_from_closure(5))
    print(fn_from_closure_2(5))

if __name__ == '__main__':
    main()
