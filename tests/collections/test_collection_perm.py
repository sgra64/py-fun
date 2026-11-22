import unittest
from . import Collection

class TestCollection(unittest.TestCase):

    def test_perm_preserves_duplicate_positions(self):
        self.assertEqual(Collection(1, 1).perm(), [[1, 1], [1, 1]])

    def test_perm_of_empty_collection_contains_empty_permutation(self):
        self.assertEqual(Collection().perm(), [[]])

    def test_perm_gen_yields_permutations_lazily(self):
        permutations = Collection(1, 2, 3).perm_gen()

        self.assertIs(iter(permutations), permutations)
        self.assertEqual(
            {tuple(permutation) for permutation in permutations},
            {
                (1, 2, 3),
                (1, 3, 2),
                (2, 1, 3),
                (2, 3, 1),
                (3, 1, 2),
                (3, 2, 1),
            },
        )

    def test_perm_gen_preserves_duplicate_positions(self):
        self.assertEqual(list(Collection(1, 1).perm_gen()), [[1, 1], [1, 1]])

    def test_perm_gen_of_empty_collection_yields_empty_permutation(self):
        self.assertEqual(list(Collection().perm_gen()), [[]])


if __name__ == "__main__":
    unittest.main()
