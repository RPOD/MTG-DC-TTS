# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.

Object class for a Deck. Consists out of the name, cards, the cardamout and
the sideboard

===============================================================================
                                Deck Class
===============================================================================
"""


class Deck(object):

    name = ""
    cards = []
    sideboard = []
    cardAmount = 0

    def __init__(self, name, cards, sideboard, cardAmount):
        self.name = name
        self.cards = cards
        self.cardAmount = cardAmount