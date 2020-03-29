"""
Module permettant de vérifier les propriétés d'une relation en fonction d'une liste de paires.
"""


def validerListePaires(liste):
    """
    Valide que la liste passée en paramèetre est bien une liste non vide de paires

    :param liste: liste à valide

    :return: true ou false
    """
    if isinstance(liste, list) and liste != []:
        listeNonTuple = list(filter(estNonTuple, liste))
        return listeNonTuple == []
    else:
        return False


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
        return membre == paire[0] and membre != paire[1]

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


def verifieIrreflexive(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété d' irréflexivité

    :param listePaires: liste des paires

    :return: premier élémént qui ne vérifie pas la propriété ou null
    """
    for x, _ in listePaires:
        try:
            listePaires.index((x, x))
            return (x, x)
        except ValueError:
            pass

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


def verifieAsymetrique(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété d'asymétrie

    :param listePaires:  liste des paires

    :return: première paire qui ne vérifie pas la propriété ou null
    """
    for x, y in listePaires:
        try:
            listePaires.index((y, x))
            if x != y:
                return (x, y)
        except ValueError:
            pass

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
                    break
                except ValueError:
                    return (x, y)
        else:
            pass

    return None


def verifieAntisymetrique(listePaires):
    """
    Vérifie si les paires fournies dans la liste passée en paramètre respectent la propriété d'antisymétrie (si a R b et b R a alors a = b)
    :param listePaires: Liste de paires à vérifier
    :return: true ou false
    """
    for x, y in listePaires:
        try:
            listePaires.index((y, x))
            if x != y:
                return (x, y)
        except ValueError:
            pass

    return None
