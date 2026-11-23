class Recursion:

    # store lists as class variables
    numbers = [ 9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

    numb_2 = [  8, 10, 2, 14, 4]

    numb_3 = [  260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
                318, 303, 153, 290, 201, 594, 457, 607, 592, 246
    ]
    numb_4 = [  260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
                318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
                132, 135, 584, 432, 591, 204, 417, 405, 362, 658,
                136, 751, 583, 536, 293, 493, 431, 780, 563, 703,
                400, 618, 397, 320, 513, 708, 319, 317, 685, 347,
                758, 439, 145, 378, 158, 384, 551, 110, 408, 648,
                847, 498,  50,  19,     # 64 numbers
    ]


    def __init__(self):
        """
        Constructor.
        """

    def sum(self, _numbers) -> int:
        """
        Return sum of numbers using recursion.
        Follow steps:
        1. Return 0 for an empty list of numbers.
        2. Split the problem by removing the first number `n1` from the list leaving `r` as remaining list (sub-problem).
        3. Invoke `sum(r)` recursively on the remaining list.
        4. Combine the result for the sub-problem with the first number `n1`: `return n1 + sum(r)`.
        """
        # your code
        return 0


    def fib(self, _n, memo=None) -> int:
        """
        Return value of n-th Fibonacci number.
        - input: n=8
        - output: 21
        """
        # your code
        return 0


    def fib_gen(self, _n):
        """
        Return a generator object that yields two lists, one with n and the
        other with corresponding fib(n).
        input: n=16
        output: generator object that produces:
        .. code-block:: ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        .. code-block::  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987])
        """
        # your code
        yield ([], [])


    def perm(self, _numbers) -> list:
        """
        Return permutation (all possible arrangements) for a given input list.
        - input: [1, 2, 3]
        - output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        """
        # your code
        return []


    def pset(self, _numbers) -> list:
        """
        Return powerset (set of all subsets) for a given input list.
        - input: [1, 2, 3]
        - output: powerset, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        """
        # your code
        return []


    def find(self, _numbers, match_func) -> list:
        """
        Return list of elements n for which match_func(n) evaluates True.
        """
        # your code
        return []


    def find_adjacent(self, pair, _numbers, _i=0) -> list:
        """
        Return list of indexes of adjacent numbers in _numbers.
        """
        # your code
        return []


    def find_pairs(self, n, _numbers) -> list:
        """
        Return list of pairs from _numbers that add to n,
        any pair, any order, no duplicates.
        """
        # your code
        return []


    def find_all_sums(self, n, _numbers) -> list:
        """
        Return all combinations of numbers in _numbers that add to n,
        (any pair, any order, no duplicates).
        """
        # your code
        return []
