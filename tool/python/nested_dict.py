#!/usr/bin/env python3
# https://stackoverflow.com/questions/14692690/access-nested-dictionary-items-via-a-list-of-keys
from functools import reduce  # forward compatibility for Python 3
import operator

def get_by_path(root, items):
    """Access a nested object in root by item sequence."""
    return reduce(operator.getitem, items, root)

def set_by_path(root, items, value):
    """Set a value in a nested object in root by item sequence."""
    get_by_path(root, items[:-1])[items[-1]] = value

d = {'a': {'b': 1}}
print(d)

print(get_by_path(d, ['a']))
print(get_by_path(d, ['a', 'b']))

set_by_path(d, ['a', 'b'], 2)
print(get_by_path(d, ['a', 'b']))
