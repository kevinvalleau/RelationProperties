from relation_properties import verification_proprietes

# réflexive, symétrique et transitive : [(1,2),(2,3),(1,3),(2,1),(3,2),(3,1),(1,1),(2,2),(3,3)]
if __name__ == '__main__':
    try:
        listePaires = eval(input("Entrez votre liste de paires, séparées par un point-virgule :\n"))

        if verification_proprietes.validerListePaires(listePaires):
                element = verification_proprietes.verifieReflexive(listePaires)
                if element is not None:
                    print(element, " ne respecte pas la réflexivité.\n")
                else:
                    print("Relation réflexive.\n")

                paire = verification_proprietes.verifieSymetrique(listePaires)
                if paire is not None:
                    print(paire, " n'a pas de paire symétrique.\n")
                else:
                    print("Relation symétrique.\n")

                paire = verification_proprietes.verifieTransitive(listePaires)
                if paire is not None:
                    print(paire, " n'a pas de paire transitive.\n")
                else:
                    print("Relation transitive.\n")

                paire = verification_proprietes.verifieAntisymetrique(listePaires)
                if paire is not None:
                    print(paire, " a une paire symétrique.\n")
                else:
                    print("Relation antisymétrique.\n")
        else:
            print("Format de liste invalide")
    except NameError:
        print("Format de liste invalide")

