# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
@version: 0.1

This is a little Program which reads MTG-Deck files in from tappedout.net
and creates a valid picture for Tabletopsimulator in order to load a costum
deck into the game.

Note for some reason some card images throw a 400 HTTP Error. If that occours
the program will prompt if it should be still loaded and ask the user to
insert the picture manually

===============================================================================
                                Main class
===============================================================================
"""
import os
from Deck import Deck
from Analyser import Analyser
from PictureGenerator import PictureGenerator


class Mtg:

    def __init__(self, filename):
        self.filename = filename

    def readInputFile(self):
        f = open(self.filename, 'r', encoding="utf8")
        text = []
        for line in f:
            text.append(line)
        f.close()
        return text

    def readInput(self):
        files = os.listdir("Input")
        for entry in files:
            mtg = Mtg('Input\\' + entry)
            text = mtg.readInputFile()
            deck = Deck(entry[:-4], [], [], 0)
            print("Now creating: " + deck.name + " please wait.\n")
            ana = Analyser(deck, text)
            ana.analyseDeck()
            if(deck.cardAmount < 70):
                pg = PictureGenerator(deck)
                pg.createPicture()
            else:
                self.chunkify(deck)
            if(len(deck.sideboard) != 0):
                sidedeck = Deck(deck.name + " sideboard", deck.sideboard, [], 0)
                pg = PictureGenerator(sidedeck)
                pg.createPicture()

    def chunkify(self, deck):
        part = []
        amount = 0
        c = 1
        for card in deck.cards:
            amount = amount + int(card.amount)
            if(amount >= 70):
                tmpdeck = Deck(deck.name + str(c), part[:], [], 0)
                pg = PictureGenerator(tmpdeck)
                pg.createPicture()
                part[:] = []
                amount = 0
                c = c + 1
            else:
                part.append(card)
        tmpdeck = Deck(deck.name + str(c), part[:], [], 0)
        pg = PictureGenerator(tmpdeck)
        pg.createPicture()


def main():
    mtg = Mtg("")
    mtg.readInput()

if __name__ == '__main__':                # call if module is called as main
    main()