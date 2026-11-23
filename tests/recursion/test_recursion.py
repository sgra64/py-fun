import unittest
import types
from . import Recursion

class TestRecursion(unittest.TestCase):
    """
    Complete tasks one after another. Once you are done with one task, run
    the test. It it fails, find the cause and repeat until the test works.
    Proceed to the next test until the full set of tests is complete.

    Start with the first test:
    pytest -v \
        tests/recursion/test_recursion.py::TestRecursion::test_a_sum_numbers

    Add incrementally more tests until the full set is complete:
    # 
    pytest -v \
        tests/recursion/test_recursion.py::TestRecursion::test_a_sum_numbers \
        tests/recursion/test_recursion.py::TestRecursion::test_b_fib \
        tests/recursion/test_recursion.py::TestRecursion::test_b_fib_memo \
        tests/recursion/test_recursion.py::TestRecursion::test_b_fib_gen \
        tests/recursion/test_recursion.py::TestRecursion::test_c_perm \
        tests/recursion/test_recursion.py::TestRecursion::test_d_pset \
        tests/recursion/test_recursion.py::TestRecursion::test_e_find_matches \
        tests/recursion/test_recursion.py::TestRecursion::test_f_find_adjacent \
        tests/recursion/test_recursion.py::TestRecursion::test_g_find_pairs \
        tests/recursion/test_recursion.py::TestRecursion::test_h_find_all_sums \
        tests/recursion/test_recursion.py::TestRecursion::test_h_find_all_sums_XL \
        tests/recursion/test_recursion.py::TestRecursion::test_h_find_all_sums_XXL

    Run tests in the IDE and in the terminal.
    """

    def setUp(self):
        self.r1 = Recursion()

    def test_a_sum_numbers(self):
        """Test number of numbers."""
        self.assertEqual(self.r1.sum(self.r1.numbers), 74)

    def test_b_fib(self):
        """Test number of numbers."""
        self.assertEqual(self.r1.fib(30), 832040)

    def test_b_fib_memo(self):
        """Test number of numbers."""
        self.assertEqual(self.r1.fib_memo(60), 1548008755920)
        self.assertEqual(self.r1.fib_memo(90), 2880067194370816120)

    def test_b_fib_gen(self):
        """Test number of numbers."""
        generator = self.r1.fib_gen(16)
        # 
        self.assertIsInstance(generator, types.GeneratorType)
        self.assertEqual(
            next(generator),
            (
                list(range(17)),
                [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],
            ),
        )
        with self.assertRaises(StopIteration):
            next(generator)

    def test_c_perm(self):
        """Test permutations of lists."""
        self.assertEqual(self.r1.perm([]), [[]])
        self.assertEqual(self.r1.perm([5]), [[5]])
        # 
        # check whether two iterables contain the same elements with the
        # same frequencies (counts), ignoring element order
        self.assertCountEqual(self.r1.perm([7, 14]), [[7, 14], [14, 7]])
        self.assertCountEqual(self.r1.perm([7, 14]), [[14, 7], [7, 14]])
        self.assertCountEqual(
            self.r1.perm([1, 2, 3]),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        )

    def test_d_pset(self):
        """Test power sets of lists."""
        self.assertEqual(self.r1.pset([]), [[]])
        # 
        # check whether two iterables contain the same elements with the
        # same frequencies (counts), ignoring element order
        self.assertCountEqual(self.r1.pset([5]), [[], [5]])
        self.assertCountEqual(self.r1.pset([5]), [[5], []])
        self.assertCountEqual(
            self.r1.pset([1, 2, 3]),
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
        )

    def test_e_find_matches(self):
        """Test finding matches in a list."""
        lst = Recursion.numbers     # [ 9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
        div3 = self.r1.find(lst, match_func=lambda n : n % 3 == 0)
        self.assertEqual(div3, [9, 3])
        div4 = self.r1.find(lst, match_func=lambda n : n % 4 == 0)
        self.assertEqual(div4, [4, 8, 4, 8, 4, 8])

    def test_f_find_adjacent(self):
        """Test indexes of adjacent pairs."""
        lst = Recursion.numbers     # [ 9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
        self.assertEqual(self.r1.find_adjacent([4, 8], lst), [1, 5, 9])
        self.assertEqual(self.r1.find_adjacent([9, 4], lst), [0])
        self.assertEqual(self.r1.find_adjacent([3, 14], lst), [7])
        self.assertEqual(self.r1.find_adjacent([8, 8], lst), [])
        self.assertEqual(self.r1.find_adjacent([1, 1], [1, 1, 1]), [0, 1])
        self.assertEqual(self.r1.find_adjacent([1, 2], []), [])

    def test_g_find_pairs(self):
        """Test pairs of numbers that have a given sum."""
        pairs = self.r1.find_pairs(5, [1, 2, 3, 4])
        normalized_pairs = [sorted(pair) for pair in pairs]
        self.assertCountEqual(normalized_pairs, [[1, 4], [2, 3]])

        pairs = self.r1.find_pairs(6, [1, 2, 3, 4, 5])
        normalized_pairs = [sorted(pair) for pair in pairs]
        self.assertCountEqual(normalized_pairs, [[1, 5], [2, 4]])

        self.assertEqual(self.r1.find_pairs(10, []), [])
        self.assertEqual(self.r1.find_pairs(10, [10]), [])

    def test_h_find_all_sums(self):
        """Test all combinations of numbers that add to a sum."""
        combinations = self.r1.find_all_sums(7, [1, 2, 3, 4])
        normalized = [sorted(combination) for combination in combinations]
        self.assertCountEqual(normalized, [[1, 2, 4], [3, 4]])

        combinations = self.r1.find_all_sums(5, [1, 2, 3, 4])
        normalized = [sorted(combination) for combination in combinations]
        self.assertCountEqual(normalized, [[1, 4], [2, 3]])

        self.assertEqual(self.r1.find_all_sums(10, []), [])
        self.assertEqual(self.r1.find_all_sums(0, [1, 2, 3]), [])

    def test_h_find_all_sums_XL(self):
        # lst = [     # input list
        #     260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
        #     318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
        # ]
        lst = Recursion.numb_3
        n = 469
        combinations = self.r1.find_all_sums(n, lst)
        normalized = [sorted(combination) for combination in combinations]
        self.assertCountEqual(normalized, [[179, 290], [101, 167, 201]])

    def test_h_find_all_sums_XXL(self):
        # lst = [     # input list
        #     260, 720, 225, 179, 101, 767, 167, 200, 157, 289,
        #     318, 303, 153, 290, 201, 594, 457, 607, 592, 246,
        #     132, 135, 584, 432, 591, 204, 417, 405, 362, 658,
        #     136, 751, 583, 536, 293, 493, 431, 780, 563, 703,
        #     400, 618, 397, 320, 513, 708, 319, 317, 685, 347,
        #     758, 439, 145, 378, 158, 384, 551, 110, 408, 648,
        #     847, 498,  50,  19,     # 64 numbers
        # ]
        lst = Recursion.numb_4
        n = 469
        combinations = self.r1.find_all_sums(n, lst)
        normalized = [sorted(combination) for combination in combinations]
        # accept any order of sub-lists and any order in each sub-list
        expected = [
            [290, 179],
            [19, 157, 293],
            [19, 246, 204],
            [19, 318, 132],
            [19, 400, 50],
            [50, 101, 318],
            [110, 201, 158],
            [136, 201, 132],
            [145, 167, 157],
            [158, 179, 132],
            [201, 101, 167],
            [19, 101, 204, 145],
            [19, 157, 135, 158],
            [19, 179, 135, 136],
            [19, 204, 136, 110],
            [19, 290, 110, 50],
            [19, 101, 167, 132, 50],
            [19, 132, 158, 110, 50]
        ]
        normalized_expected = [sorted(combination) for combination in expected]
        self.assertCountEqual(normalized, normalized_expected)


if __name__ == '__main__':
    unittest.main()
