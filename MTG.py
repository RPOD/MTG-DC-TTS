# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
@version: 0.3

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
from Upload import Upload


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

    def readTextInput(self):
        files = os.listdir("Input(text)")
        names = []
        for entry in files:
            mtg = Mtg('Input(text)\\' + entry)
            text = mtg.readInputFile()
            names.append(entry[:-4])
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
        return names

    def readRawInput(self):
        files = os.listdir("Input(raw)")
        files.remove("back")
        while(len(os.listdir("Input(raw)\\back")) != 1):
            if(len(os.listdir("Input(raw)\\back")) == 0):
                input("Please insert a picture in the folder Input(raw)\\back" +
                        "\nPress Enter to continue.")
            else:
                input("Please insert just one image in Input(raw)\\back." +
                        "\nPress Enter to continue.")
        part = []
        amount = 0
        c = 1
        for card in files:
            amount = amount + 1
            if(amount >= 70):
                pg = PictureGenerator("")
                pg.createRawPicture(part, c)
                part[:] = []
                part.append(card)
                amount = 0
                c = c + 1
            else:
                part.append(card)
        pg = PictureGenerator("")
        pg.createRawPicture(part, c)

    def chunkify(self, deck):
        part = []
        amount = 0
        c = 1
        for card in deck.cards:
            amount = amount + int(card.amount)
            if(amount >= 70):
                tmpdeck = Deck(deck.name + " " + str(c), part[:], [], 0)
                pg = PictureGenerator(tmpdeck)
                pg.createPicture()
                part[:] = []
                part.append(card)
                amount = 0
                c = c + 1
            else:
                part.append(card)
        tmpdeck = Deck(deck.name + " " + str(c), part[:], [], 0)
        pg = PictureGenerator(tmpdeck)
        pg.createPicture()

    def printHeader(self):
        print("==================================================\n" +
                "           --- Welcome to MTG-DC-TTS ---\n" +
                "==================================================\n\n" +
                "Creator: \t R.P.O.D.\n" +
                "Version: \t 0.3\n\n" +
                "Please check the Readme before using this Program!\n\n" +
                "==================================================\n" +
                "\t           --- ENJOY ---\n" +
                "==================================================\n\n\n")


def main():
    mtg = Mtg("")
    mtg.printHeader()
    mode = 'r'
    while(mode != 'r' or 't'):
        mode = input("Choose an inputmode:\n\n" +
            "r = Raw input from Folder Input(raw)\n" +
            "t = Text input from Folder Input(text)\n")
        if (mode == 't'):
            names = mtg.readTextInput()
            break
        if (mode == 'r'):
            names = []
            mtg.readRawInput()
            break
        else:
            print("Please insert r or t")
    upload = 'y'
    while(upload != 'y' or 'n'):
        upload = input("Do you want to upload the picture to imgur? [y/n]\n")
        if (upload == 'n'):
            break
        if (upload == 'y'):
            up = Upload(mode, names)
            up.uploadFiles()
            break


if __name__ == '__main__':                # call if module is called as main
    main()