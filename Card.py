# -*- coding: utf-8 -*-
"""
@author R.P.O.D.
Objectclass for cards, consisting out of name and their amount

===============================================================================
                                Card Class
===============================================================================
"""


class Card(object):

    name = ""
    amount = 0

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount