#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    mot_Majuscule = ''
    for character in range(len(mot)): # range (0, len(mots), 1)
        mot_Majuscule += chr(ord(mot[character])-32) # chr() et ord(): retourne le char associé au unicode et vice-versa. (unicode-char) et (char->unicode)
    return mot_Majuscule


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

# Misssion : Capitalize all char of a list of words
# Principe de l'algorithme : Prendre les char des mots de la liste "mots" -> unicode -> soustraire 32 index ASCII -> char -> print mots
