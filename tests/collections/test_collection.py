import unittest

from src.collections.collection_impl import Collection


class TestCollection(unittest.TestCase):

    def test_contains_and_add(self):
        col = Collection()
        self.assertFalse(col.contains(1))
        self.assertIs(col.add(1), col)
        self.assertTrue(col.contains(1))
        col.add(1)
        self.assertEqual(col._items, [1, 1])

    def test_contains_and_add_in_set(self):
        col = Collection(asSet=True)
        self.assertFalse(col.contains(1))
        self.assertIs(col.add(1), col)
        self.assertTrue(col.contains(1))
        col.add(1)
        self.assertEqual(col._items, {1})

    def test_add_only_keeps_unique_set_items(self):
        collection = Collection(asSet=True)
        collection.add({1, 2}).add({1, 2})
        self.assertEqual(collection._items, {frozenset({1, 2})})

    def test_constructor_accepts_list_and_set_iterables(self):
        numbers = Collection([1, 2, 3])
        letters = Collection({"a", "b", "c"})

        self.assertEqual(numbers._items, [[1, 2, 3]])
        self.assertEqual(letters._items, [frozenset({"a", "b", "c"})])

    def test_constructor_accepts_variadic_items_and_set_mode(self):
        numbers = Collection(1, 2, 2)
        unique_numbers = Collection(1, 2, 2, asSet=True)

        self.assertEqual(numbers._items, [1, 2, 2])
        self.assertEqual(unique_numbers._items, {1, 2})

    def test_repr_displays_set_braces(self):
        self.assertEqual(repr(Collection(1, 2, asSet=True)), "{1, 2}")

    def test_zip_returns_pairs_and_stops_at_shorter_collection(self):
        zipped = Collection.zip(
            Collection("a", "b", "c"),
            Collection(1, 2),
        )

        self.assertIsInstance(zipped, Collection)
        self.assertEqual(zipped._items, [("a", 1), ("b", 2)])

    def test_zip_with_empty_collection_returns_empty_collection(self):
        self.assertEqual(Collection.zip(Collection(), Collection(1))._items, [])

    # def test_constructor_rejects_other_iterables(self):
    #     with self.assertRaisesRegex(TypeError, "elements must be a list or set"):
    #         Collection((1, 2, 3))

    def test_perm_returns_all_full_length_permutations(self):
        permutations = Collection(1, 2, 3).perm()

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
