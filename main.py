from relation_properties import verification_proprietes
from relation_properties import generation_mots

# réflexive, symétrique et transitive : [(1,2),(2,3),(1,3),(2,1),(3,2),(3,1),(1,1),(2,2),(3,3)]
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (3, 1), (0, 2), (2, 1)]
if __name__ == '__main__':
    try:
        #listePaires = eval(input("Entrez votre liste de paires, séparées par un point-virgule :\n"))

        liste_mot = generation_mots.generer_liste_mots_binaires(3)

        listePaires = generation_mots.generer_paires_moins_ou_autant_de_uns(liste_mot)
        if verification_proprietes.validerListePaires(listePaires):
                element = verification_proprietes.verifieReflexive(listePaires)
                if element is not None:
                    print(element, " ne respecte pas la réflexivité.\n")
                else:
                    print("Relation réflexive.\n")

                paire = verification_proprietes.verifieSymetrique(listePaires)
                if paire is not None:
                    print("Relation non symétrique ", paire, " n'a pas de paire symétrique.\n")
                else:
                    print("Relation symétrique.\n")

                paire = verification_proprietes.verifieTransitive(listePaires)
                if paire is not None:
                    print("Relation non transitive ",paire, " n'a pas de paire transitive.\n")
                else:
                    print("Relation transitive.\n")

                paire = verification_proprietes.verifieAntisymetrique(listePaires)
                if paire is not None:
                    print("Relation non antisymétrique ", paire, " a une paire symétrique.\n")
                else:
                    print("Relation antisymétrique.\n")
                paire = verification_proprietes.verifieIrreflexive(listePaires)
                if paire is not None:
                    print("Relation non irréflexive ", paire, " a une paire ayant les mêmes éléments.\n")
                else:
                    print("Relation irréflexive.\n")
                paire = verification_proprietes.verifieAsymetrique(listePaires)
                if paire is not None:
                    print("Relation non asymétique ", paire, " a une paire symétrique.\n")
                else:
                    print("Relation asymétrique.\n")
        else:
            print("Format de liste invalide")
    except NameError:
        print("Format de liste invalide")

