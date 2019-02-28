def verifier_resultat(resultat_utilisateur, resultat):
    if resultat_utilisateur == resultat:
        return True
    else:
        return False







resultat_utilisateur = int(input("Donnez le résultat de l'opération : 5*3 - 2 + (100 % 4)"))
resultat = 5*3 - 2 + 100/4

if verifier_resultat(resultat_utilisateur, resultat):
    print("Parfait vous avez réussi")
else:
    for i in range(1,1001):
        print("I need more practice")