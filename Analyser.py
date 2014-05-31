# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
Analyser Class for the cards / decks

===============================================================================
                                Analyser Class
===============================================================================
"""

from Card import Card


class Analyser:

    def __init__(self, deck, text):
        self.deck = deck
        self.text = text

    def analyseDeck(self):
        sideboard = 0
        amount = 0
        for line in self.text:
            if("/ " in line):
                line = line.replace("/ ", "")
            if('Sideboard' in line):
                sideboard = 1
                continue
            if(line == "\n"):
                continue
            if(sideboard == 0):
                card = Card((line.split('\t')[1])[:-1], line.split('\t')[0])
                self.deck.cards.append(card)
                amount = amount + int(card.amount)
            else:
                card = Card((line.split('\t')[1])[:-1], line.split('\t')[0])
                self.deck.sideboard.append(card)
        self.deck.cardAmount = amount