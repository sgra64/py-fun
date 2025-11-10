
class Expressions:
    """"
    Fill in one-line expressions (no own functions) to initialize attributes
    self.b .. self.k with specified values.

    Use Python built-in functions, list expressions and list comprehension,
    but NOT own functions.

    Complete tasks one after another. Once you are done with one task,
    uncomment test cases in test_expressions.py. Remove comments for
      # Test_case_b = Test_case
      # Test_case_c = Test_case
      # Test_case_d = Test_case
      # ...
    Run tests in IDE and in a terminal:
      python test_expressions.py
      python -m unittest
    """

    default_numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]

    def __init__(self, _numbers=default_numbers):
        """
        Constructor to initialize member variables.
        """
        self.numbers = _numbers

        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)    # <-- given solution, insert one-line expressions below

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = []      # <-- write expression here

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = []

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = []

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = []

        # f) initialize with number of odd numbers: 4
        self.f = 0

        # g) initialize with sum_ of odd numbers: 28
        self.g = 0

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = []

        # i) number of duplicate numbers: 2
        self.i = 0

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = []

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k = "NEITHER"


    def print_results(self):
        print(f'\nnumbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')
