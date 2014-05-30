# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
@version: 0.1

This is a little Program which reads MTG-Deck files in from tappedout.net
and creates a valid picture for Tabletopsimulator in order to load a costum
deck into the game.

Note for some reason some card images throw a 400 HTTP Error, Pictures will
be still created though will be incomplete. Check the console output to see
which cards couldn't be loaded

!!!IMPORTANT NOTE!!!

If a card name contains a \ pleae replace it with just a blank symbol
For example: Bound \ Determined , it should be Bound Determined
Please check the .txt filebeforehand

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
            print(deck.name)
            ana = Analyser(deck, text)
            ana.analyseDeck()
            if(deck.cardAmount < 70):
                pg = PictureGenerator(deck)
                pg.createPicture()
            else:
                i = 1
                for part in self.chunks(deck):
                    tmpdeck = Deck(entry[:-4] + str(i), part, [], 0)
                    pg = PictureGenerator(tmpdeck)
                    pg.createPicture()
            if(len(deck.sideboard) != 0):
                sidedeck = Deck(deck.name + " sideboard", deck.sideboard, [], 0)
                pg = PictureGenerator(sidedeck)
                pg.createPicture()

    def chunks(self, deck):
        chunks = []
        part = []
        amount = 0
        for card in deck.cards:
            amount = amount + int(card.amount)
            if(amount >= 70):
                chunks.append(part)
                part[:] = []
                amount = 0
            else:
                part.append(card)
        return chunks


def main():
    mtg = Mtg("")
    mtg.readInput()

if __name__ == '__main__':                # call if module is called as main
    main()