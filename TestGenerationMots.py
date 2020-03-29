import unittest
from relation_properties import generation_mots


class TestGenerqtionMots(unittest.TestCase):
    def test_generer_liste_mots_binaires_longueur_1_liste_deux_mots(self):
        # Arrange

        # Act
        liste_mots = generation_mots.generer_liste_mots_binaires(1)
        # Assert
        self.assertEqual(['0', '1'], liste_mots)

    def test_generer_liste_mots_binaires_longueur_2_liste_six_mots(self):
        # Arrange

        # Act
        liste_mots = generation_mots.generer_liste_mots_binaires(2)
        # Assert
        self.assertEqual(['0', '1', '00', '10', '01', '11'] , liste_mots)

    def test_generer_liste_mots_binaires_longueur_3_liste_treize_mots(self):
        # Arrange

        # Act
        liste_mots = generation_mots.generer_liste_mots_binaires(3)
        # Assert
        self.assertEqual(['0', '1', '00', '10', '01', '11', '000', '100', '010', '001', '110', '011', '111'], liste_mots)

    def test_generer_liste_mots_binaires_longueur_1_liste_vingt_quatre_mots(self):
        # Arrange
        liste_a_comparer = ['0', '1', '00', '10', '01', '11', '000', '100', '010', '001', '110', '011', '111', '0000', '1000', '0100', '0010', '0001', '1100', '0110', '0011', '1110', '0111', '1111']
        # Act
        liste_mots = generation_mots.generer_liste_mots_binaires(4)
        # Assert
        self.assertEqual(liste_a_comparer, liste_mots)

    def test_generer_paires_moins_ou_autant_de_uns_liste_longueur_deux_resultat_ok(self):
        # Arrange
        liste_a_comparer = [('0', '0'), ('0', '1'), ('0', '00'), ('0', '10'), ('0', '01'), ('0', '11'), ('1', '1'), ('1', '10'), ('1', '01'), ('1', '11'), ('00', '0'), ('00', '1'), ('00', '00'), ('00', '10'), ('00', '01'), ('00', '11'), ('10', '1'), ('10', '10'), ('10', '01'), ('10', '11'), ('01', '1'), ('01', '10'), ('01', '01'), ('01', '11'), ('11', '11')]
        liste_mots = generation_mots.generer_liste_mots_binaires(2)

        # Act
        liste_paires = generation_mots.generer_paires_moins_ou_autant_de_uns(liste_mots)

        # Assert
        self.assertEqual(liste_a_comparer, liste_paires)


if __name__ == '__main__':
    unittest.main()
