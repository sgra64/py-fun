import unittest
from . import Collection

class TestCollection(unittest.TestCase):

    def test_pset_returns_all_subsets_without_duplicate_values(self):
        powerset = Collection(1, 2, 2).pset()
        self.assertEqual(
            {frozenset(subset) for subset in powerset},
            {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})},
        )
        self.assertEqual(len(powerset), 4)

    def test_pset_backtracks_over_each_set_item(self):
        powerset = Collection(1, 2, asSet=True).pset()
        self.assertEqual(
            {frozenset(subset) for subset in powerset},
            {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})},
        )

    def test_pset_of_empty_collection_contains_empty_set(self):
        self.assertEqual(Collection().pset(), [set()])

    def test_pset_gen_yields_all_subsets_without_duplicate_values(self):
        powerset = Collection(1, 2, 2).pset_gen()

        self.assertIs(iter(powerset), powerset)
        self.assertEqual(
            {frozenset(subset) for subset in powerset},
            {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})},
        )

    def test_pset_gen_of_empty_collection_yields_empty_set(self):
        self.assertEqual(list(Collection().pset_gen()), [set()])


if __name__ == "__main__":
    unittest.main()
