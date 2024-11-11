import unittest

from arekit_contrib_networks.src.io_utils.w2v_based import Embedding


class TestModelNamesService(unittest.TestCase):

    def test(self):
        single_element = [("a", [1])]
        e = Embedding.from_word_embedding_pairs_iter(iter(single_element))
        print(e.VocabularySize)
        print(e.VectorSize)

    def test_empty(self):
        e = Embedding.from_word_embedding_pairs_iter(iter([]))
        print(e.VocabularySize)
        print(e.VectorSize)


if __name__ == '__main__':
    unittest.main()
