"""
Module permettant la génération de mots binaires
"""


def generer_liste_mots_binaires(longueur_mot):
    """
    Génère une liste de mots binaires (0 et 1) jusqu'à la longueur passée en paramètre
    :param longueur_mot: longueur maximale des mots à générer
    :return: une liste de mots binaires sous forme de chaînes de caractères
    """
    listeMots = []
    for indiceLongueur in range (1, longueur_mot+1):
        listeMots.append("0"*indiceLongueur)
        for indiceNbUns in range (1, indiceLongueur+1):
            for indicePositionUns in range(0, (indiceLongueur - indiceNbUns) + 1):
                listeMots.append("0" * indicePositionUns + "1" * indiceNbUns + "0" * (indiceLongueur - indiceNbUns - indicePositionUns))

    return listeMots


def cree_filtre_mot_moins_ou_autant_de_uns(membre):
    """
    Crée une clôture pour permettre la réalisation d'un filtre à passer à la fonction filter sur une liste

    :param membre: membre pour lequel on veut créer le filtre

    :return: une clôture qu'on peut passer à l'instruction filter sur une liste
    """

    def filtre(mot):
        return mot.count("1") >= membre.count("1")

    return filtre


def generer_paires_moins_ou_autant_de_uns(liste_mots):
    """
    Génère une liste de paires en fonction de la liste de mots passée en paramètre, respectant la relation moins ou autant de uns
    :param liste_mots: liste de mots binaires
    :return: liste de paires avec les paires en relation
    """
    liste_paires = []
    for mot_binaire in liste_mots:
        filtre_moins_ou_autant_de_un = cree_filtre_mot_moins_ou_autant_de_uns(mot_binaire)

        liste_mots_en_relation = list(filter(filtre_moins_ou_autant_de_un, liste_mots))
        for mot_relation in liste_mots_en_relation:
            liste_paires.append(( mot_binaire, mot_relation))

    return liste_paires


if __name__ == '__main__':
    #print(generer_liste_mots_binaires(1), "\n")
    #print(generer_liste_mots_binaires(2), "\n")
    #print(generer_liste_mots_binaires(3), "\n")
    #print(generer_liste_mots_binaires(4), "\n")

    liste_mots = generer_liste_mots_binaires(2)

    liste_paires = generer_paires_moins_ou_autant_de_uns(liste_mots)

    print(liste_paires, "\n")

    liste_mots = generer_liste_mots_binaires(3)

    liste_paires = generer_paires_moins_ou_autant_de_uns(liste_mots)

    print(liste_paires, "\n")
