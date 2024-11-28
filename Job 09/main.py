def moyenne(note1, note2, note3):

    moyenne_etudiant = (note1 + note2 + note3) / 3

    if 15 <= moyenne_etudiant <= 20:
        print("Très bon élève, moyenne :", moyenne_etudiant)
    if 11 <= moyenne_etudiant <= 14:
        print("Bon élève, moyenne :", moyenne_etudiant)
    if 10 <= moyenne_etudiant <= 8:
        print("Élève moyen, moyenne :", moyenne_etudiant)
    if 0 <= moyenne_etudiant <= 7:
        print("Élève devant faire des efforts, moyenne :", moyenne_etudian)

note1 = int(input("Donne moi la première note :"))
note2 = int(input("Donne moi la deuxième note :"))
note3 = int(input("Donne moi la troisième note :"))

moyenne(note1, note2, note3)