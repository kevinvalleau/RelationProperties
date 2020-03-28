"""
Module permettant de vérifier les propriétés d'une relation en fonction d'une liste de paires.
"""


def estNonTuple(element):
    """
    Vérifie si l'élément passé en paramètre n'est pas une instance de tuple

    :param element: élément à vérifier
    :return: true ou false
    """
    return isinstance(element, tuple) == False


def creeFiltreParPremierMembre(membre):
    """
    Crée une clôture pour permettre la réalisation d'un filtre à passer à la fonction filter sur une liste

    :param membre: membre pour lequel on veut créer le filtre

    :return: une clôture qu'on peut passer à l'instruction filter sur une liste
    """

    def filtre(paire):
        return membre == paire[0]

    return filtre


def verifieReflexive(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété de réflexivité

    :param listePaires: liste des paires

    :return: premier élémént qui ne vérifie pas la propriété ou null
    """
    for x, _ in listePaires:
        try:
            listePaires.index((x, x))
        except ValueError:
            return x

    return None


def verifieSymetrique(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété de symétrie

    :param listePaires:  liste des paires

    :return: première paire qui ne vérifie pas la propriété ou null
    """
    for x, y in listePaires:
        try:
            listePaires.index((y, x))
        except ValueError:
            return (x, y)

    return None


def verifieTransitive(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété de transitivité

    :param listePaires: liste des paires

    :return: première paire qui ne vérifie pas la propriété ou null
    """
    for x, y in listePaires:
        filtreY = creeFiltreParPremierMembre(y)
        # On filtre les paires de la liste qui commencent pas le second membre de la paire en cours
        listePairesAPartirdeY = list(filter(filtreY, listePaires))

        if listePairesAPartirdeY != []:
            for a, b in listePairesAPartirdeY:
                # Pour chaque paire, on vérifie si on en trouve une qui commence par x et finit par b
                # On test donc le chemin suivant : x -> y et y (qui devient a) -> b => x -> b
                try:
                    listePaires.index((x, b))
                except ValueError:
                    return (x, y)
        else:
            return (x, y)

        return None


# réflexive, symétrique et transitive : [(1,2),(2,3),(1,3),(2,1),(3,2),(3,1),(1,1),(2,2),(3,3)]
if __name__ == '__main__':
    listePaires = eval(input("Entrez votre liste de paires, séparées par un point-virgule :\n"))

    # il faut que tous les éléments de la liste soient des paires

    if isinstance(listePaires, list) and listePaires != [] and isinstance(listePaires[0], tuple):
        listeNonTuple = list(filter(estNonTuple, listePaires))
        if listeNonTuple == []:
            element = verifieReflexive(listePaires)
            if element is not None:
                print(element, " ne respecte pas la réflexivité.\n")
            else:
                print("Relation réflexive.\n")

            paire = verifieSymetrique(listePaires)
            if paire is not None:
                print(paire, " n'a pas de paire symétrique.\n")
            else:
                print("Relation symétrique.\n")

            paire = verifieTransitive(listePaires)
            if paire is not None:
                print(paire, " n'a pas de paire transitive.\n")
            else:
                print("Relation transitive.\n")
        else:
            print("Format de liste invalide")
    else:
        print("Liste vide donc réflexive")
