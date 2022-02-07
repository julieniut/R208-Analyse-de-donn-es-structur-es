######################################################################################
#fonction principale
#nom du fichier à lire

def question1(nom):
    print(f"je vais ouvrir le fichier {nom}")

    fichier =open(nom,'r',encoding="utf-8") #fais que les caractère spéciaux soit lu

    cpt=1 #compteur

    for ligne in fichier: #pour toute les lignes du fichiers

        ligne=ligne.rstrip("\n\r") #supprime les espace entre les lignes et supprime les caractères spéciaux

        print(f"ligne{cpt}:{ligne}")

        cpt=cpt+1


    fichier.close() #pas oublier de fermer le fichier quand on l'ouvre

    #####################################################################################
    # fonction principale
    # nom du fichier à lire
    #pour trouver les doublons
def question2(nom):
    print(f"je vais ouvrir le fichier {nom}")

    fichier = open(nom, 'r', encoding="utf-8")  # fais que les caractère spéciaux soit lu

    #j'enlève la première ligne
    fichier.readline()


    for ligne in fichier:  # pour toute les lignes du fichiers

        ligne = ligne.rstrip("\n\r")  # supprime les espace entre les lignes et supprime les caractères spéciaux
        liste =ligne.split(";")


        dictionnaire = {
            "n°etudiant": liste[0],
            "nom":liste[2],
            "prenom" :liste[3],
            "groupe": liste[4],
            "note":liste[5],
        }
        print(dictionnaire["nom"],dictionnaire["prenom"],dictionnaire["note"])





        #for elt in liste: #affiche tous les éléments de la liste
        #    print(elt)



    fichier.close()  # pas oublier de fermer le fichier quand on l'ouvre


#####################################################################################
if __name__ =='__main__':
    #question1("C:\\tmp\\un fichier de notes.txt") chemin absolu du fichier note
    question2("C:\\tmp\\un fichier de notes.txt")  # chemin absolu du fichier note
