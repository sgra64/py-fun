from typing import Any
from . import Collection

def main():
    c1 = Collection('a', 'b', 'c')
    c2 = Collection(1, 2, 3)
    c3 = Collection(1, 2, 3, asSet=True)
    c4 = Collection([])
    c5 = Collection([], asSet=True)
    c6 = Collection([1, 2, 3])
    c7 = Collection([1, 2, 3], asSet=True)
    c8 = Collection({})
    c9 = Collection({}, asSet=True)
    c10 = Collection({1, 2, 3})
    c11 = Collection({1, 2, 3}, asSet=True)
    # 
    print(f' c1 = Collection(\'a\', \'b\', \'c\'):           -> {c1}')
    print(f' c2 = Collection(1, 2, 3):                 -> {c2}')
    print(f' c3 = Collection(1, 2, 3, asSet=True):     -> {c3}')
    print(f' c4 = Collection([]):                      -> {c4}')
    print(f' c5 = Collection([], asSet=True):          -> {c5}')
    print(f' c6 = Collection([1, 2, 3]):               -> {c6}')
    print(f' c7 = Collection([1, 2, 3], asSet=True):   -> {c7}')
    print(f' c8 = Collection({{}}):                      -> {c8}')
    print(f' c9 = Collection({{}}, asSet=True):          -> {c9}')
    print(f'c10 = Collection({{1, 2, 3}}):               -> {c10}')
    print(f'c11 = Collection({{1, 2, 3}}, asSet=True):   -> {c11}')

    print(f'\nCollection.zip(c1, c2): {Collection.zip(c1, c2)}')

    # print(f'\nc2.pset(): {c2.pset()}')
    # print(f'c2.pset_gen(): {list(c2.pset_gen())}')
    # # 
    # print(f'c2.pset_gen():')
    # for subset in c2.pset_gen():
    #     print(f" -> {'{}' if not subset else subset}")
    # # 
    # print(f'\nc2.perm():')
    # for p in c2.perm():
    #     print(f" -> {p}")
    # # 
