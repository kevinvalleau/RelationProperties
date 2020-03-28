import unittest
from relation_properties import verification_proprietes



class TestRelationProperties(unittest.TestCase):

    def test_VerifieReflexive_ListeEstReflexive_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieReflexive(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieReflexive_ListeAvecAucunePaireAyantLesMemesElements_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1)]
        # Act
        element = verification_proprietes.verifieReflexive(listeTest)
        # Assert
        self.assertEqual(1, element)

    def test_VerifieReflexive_ListeAvecQuelquesPairesAyantLesMemesElements_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (3, 3)]
        # Act
        element = verification_proprietes.verifieReflexive(listeTest)
        # Assert
        self.assertEqual(1, element)

    def test_VerifieSymetrique_ListeEstSymetrique_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieSymetrique(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieSymetrique_ListeAvecAucunePaireSymétrique_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieSymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieSymetrique_ListeAvecQuelquesPairesSymétrique_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (3, 2), (3, 1), (3, 3)]
        # Act
        element = verification_proprietes.verifieSymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieTransitive_ListeEstTransitive_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieTransitive(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieTransitive_ListeAvecAucunePaireTransitive_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3)]
        # Act
        element = verification_proprietes.verifieTransitive(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieTransitive_ListeAvecQuelquesPairesTransitives_ElementUnRetourne(self):
        # Arrange
        listeTest = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (3, 1), (0, 2), (2, 1)]
        # Act
        element = verification_proprietes.verifieTransitive(listeTest)
        # Assert
        self.assertEqual((0, 2), element)

    def test_VerifieAntisymetrique_ListeEstAntisymetrique_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieAntisymetrique(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieAntisymetrique_ListeSymetrique_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieAntisymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieAntisymetrique_ListeAvecQuelquesPairesSymetrique_ElementUnRetourne(self):
        # Arrange
        listeTest =  [(1, 2), (2, 3), (1, 3), (2, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieAntisymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieIrreflexive_ListeEstIrreflexive_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1)]
        # Act
        element = verification_proprietes.verifieIrreflexive(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieIrreflexive_ListeAvecToutesLesPaireAyantLesMemesElements_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieIrreflexive(listeTest)
        # Assert
        self.assertEqual((1, 1), element)

    def test_VerifieIrreflexive_ListeAvecQuelquesPairesAyantLesMemesElements_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1)]
        # Act
        element = verification_proprietes.verifieIrreflexive(listeTest)
        # Assert
        self.assertEqual((1, 1), element)

    def test_VerifieAsymetrique_ListeEstAsymetrique_AucunElementRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3)]
        # Act
        element = verification_proprietes.verifieAsymetrique(listeTest)
        # Assert
        self.assertIsNone(element)

    def test_VerifieAsymetrique_ListeToutesLesPaireSymétriques_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieAsymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

    def test_VerifieAsymetrique_ListeAvecQuelquesPairesSymétriques_ElementUnRetourne(self):
        # Arrange
        listeTest = [(1, 2), (2, 3), (1, 3), (2, 1), (1, 1), (2, 2), (3, 3)]
        # Act
        element = verification_proprietes.verifieAsymetrique(listeTest)
        # Assert
        self.assertEqual((1, 2), element)

if __name__ == '__main__':
    unittest.main()
