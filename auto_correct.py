#!/usr/bin/python3
# Typo Correcter for unstructured text
# Created by Team Axenhammer, https://github.com/Axenhammer
# Licensed under MIT

from spellchecker import SpellChecker
import sys

def normalize(misspelled):
    spell = SpellChecker()
    # misspelled = sys.argv[1]
    orig_str = misspelled
    new_str = misspelled
    misspelled = list(misspelled.split(' '))
    misspelled = spell.unknown(misspelled)
    for word in misspelled:
        new_str = new_str.replace(word,spell.correction(word))
    return(new_str)

if __name__ == '__main__':
    normalize(sys.argv[1])
