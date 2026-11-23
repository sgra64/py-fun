from functools import cmp_to_key
from . import Recursion

def main():
    """
    Main driver that runs when this file is executed by Python interpreter.
    """
    run_choices = [
        1,      # Challenge 1, Simple recursion: sum numbers
        # 2,      # Challenge 2, Fibonacci numbers
        # 21,     # Challenge 2.1, fig_gen()
        # 22,     # Challenge 2.2, memoization, fib(60), fib(90)
        # 3,      # Challenge 3, Permutation
        # 4,      # Challenge 4, Powerset
        # 5,      # Challenge 5, Finding matches, find()
        # 51,     # Challenge 5.1, find_adjacent() pairs
        # 52,     # Challenge 5.2, find_pairs() that add to n
        # 6,      # Challenge 6, Find all combinations that add to n
        # 61,     # Challenge 6.1, Find all in medium set
        # 7       # Challenge 7, Hard problem finding numbers
    ]

    n1 = Recursion()
    print(f'numbers: {Recursion.numbers}')

    # Challenge 1, Simple recursion: sum numbers
    if 1 in run_choices:
        s = n1.sum(Recursion.numbers)
        print(f'sum(Recursion.numbers): {s}')

    # Challenge 2, Fibonacci numbers
    if 2 in run_choices:
        n = 30
        print(f'\nfib({n}): {n1.fib(n)}')

    # Challenge 2.1, fig_gen()
    if 21 in run_choices:
        gen = n1.fib_gen(20)    # yield generator object
        n, fib = next(gen)      # trigger generator
        print(f'n(gen): {n}')
        print(f'fib(n): {fib}')

    # Challenge 2.2, memoization, fib(60), fib(90)
    if 22 in run_choices:
        n = 60
        print(f'fib_memo({n}): {n1.fib_memo(n)}')
        n = 90
        print(f'fib_memo({n}): {n1.fib_memo(n)}')


    # Challenge 3, Permutation
    if 3 in run_choices:
        lst = [1, 2, 3]
        perm = n1.perm(lst)
        print(f'\nperm({lst}) -> {perm}')


    # Challenge 4, Powerset
    if 4 in run_choices:
        lst = [1, 2, 3]
        pset = n1.pset(lst)
        print(f'\npset({lst}) -> {pset}')


    lst = Recursion.numbers
    # lst = [ 9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
    #
    # Challenge 5, Finding matches, find()
    if 5 in run_choices:
        div3 = n1.find(lst, match_func=lambda n : n % 3 == 0)
        print(f'\nfind numbers divisible by 3: {div3}')

    # Challenge 5.1, find_adjacent() pairs
    if 51 in run_choices:
        pair = [4, 8]
        adj = n1.find_adjacent(pair, lst)
        print(f'find_adjacent({pair}, list): {adj}')

    # Challenge 5.2, find_pairs() that add to n
    if 52 in run_choices:
        n = 12
        pairs = n1.find_pairs(n, lst)
        print(f'find_pairs({n}, list) -> {pairs}')

    lst = Recursion.numb_2
    # lst = [8, 10, 2, 14, 4]     # input list
    #
    # Challenge 6, Find all combinations that add to n
    if 6 in run_choices:
        print(f'\nlist: {lst}\n\\\\')
        n = 14
        all = n1.find_all_sums(n, lst)
        print(f'find_all_sums({n}, lst) -> {all}')
        #
        n = 20
        all = n1.find_all_sums(n, lst)
        print(f' - find_all_sums({n}, lst) -> {all}')
        #
        n = 32
        all = n1.find_all_sums(n, lst)
        print(f' - find_all_sums({n}, lst) -> {all}')

    lst = Recursion.numb_3
    # lst = [     # input list
    #     260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
    #     318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
    # ]
    #
    # Challenge 6.1, Find all in medium set
    if 61 in run_choices:
        print(f'\nlist({len(lst)}): {lst}\n\\\\')
        n = 101 + 201 + 167     # 469 -> [[179, 290], [101, 167, 201]]
        all = n1.find_all_sums(n, lst)
        for i, s in enumerate(all):
            print(f' {i+1:2}: find_all_sums({sum(s)}) -> {s}')

    lst = Recursion.numb_4
    # lst = [     # input list
    #     260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
    #     318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
    #     132, 135, 584, 432, 591, 204, 417, 405, 362, 658,
    #     136, 751, 583, 536, 293, 493, 431, 780, 563, 703,
    #     400, 618, 397, 320, 513, 708, 319, 317, 685, 347,
    #     758, 439, 145, 378, 158, 384, 551, 110, 408, 648,
    #     847, 498,  50,  19,     # 64 numbers
    # ]
    # Challenge 7, Hard problem finding numbers
    if 7 in run_choices:
        print(f'\nlist({len(lst)}) with {len(lst)} numbers.\n\\\\')
        n = 101 + 201 + 167     # 469
        all = n1.find_all_sums(n, lst)
        #
        sort_cpm = lambda x, y: -1 if len(x) < len(y) else 1 if len(x) > len(y) else \
            -1 if x <= y else 1 if x > y else 0
        all.sort(key=cmp_to_key(sort_cpm))  # sort by len(solution)
        normalized = [sorted(combination) for combination in all]
        #
        for i, s in enumerate(normalized):
            print(f' {i+1:2}: find_all_sums({sum(s)}) -> {s}')
        print()
