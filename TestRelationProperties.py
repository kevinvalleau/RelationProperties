import unittest
import main


class TestRelationProperties(unittest.TestCase):

    def test_VerifieReflexive_ListeIsReflexive_NoElementReturned(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = main.verifieReflexive(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieReflexive_ListeWithNoIdenticalPairs_ElementOneReturned(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1)]
        # Act
        element = main.verifieReflexive(listeTest)
        # Assert
        self.assertEqual(1, element)

    def test_VerifieReflexive_ListeFewIdenticalPairs_ElementOneReturned(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (3, 3)]
        # Act
        element = main.verifieReflexive(listeTest)
        # Assert
        self.assertEqual(1, element)

if __name__ == '__main__':
    unittest.main()
