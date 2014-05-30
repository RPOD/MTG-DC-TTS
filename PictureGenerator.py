# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
Class for generating pictures

===============================================================================
                            Picture Generator Class
===============================================================================
"""
import urllib.request
import os
import io
from PIL import Image


class PictureGenerator:

    def __init__(self, deck):
        self.deck = deck

    def createPicture(self):
        grid = Image.new('RGB', (4800, 4760))
        x = 0
        y = 0
        for card in self.deck.cards:
            try:
                iurl = urllib.request.urlopen("http://mtgimage.com/card/" + card.name + ".hq.jpg")
            except urllib.request.HTTPError:
                print ("Please load " + card.name + " manually.")
                continue
            rawfile = io.BytesIO(iurl.read())
            cim = Image.open(rawfile)
            cim = cim.resize((480, 680), Image.ANTIALIAS)
            for i in range(int(card.amount)):
                grid.paste(cim, (x, y))
                x = x + 480
                if (x == 4800):
                    x = 0
                    y = y + 680
        try:
            burl = urllib.request.urlopen("http://s22.postimg.org/9n0ainnwh/XLHQ_Back.jpg")
        except urllib.request.HTTPError:
            print ("Backimage could not be loaded'")
        rawfileb = io.BytesIO(burl.read())
        bim = Image.open(rawfileb)
        bim = bim.resize((480, 680), Image.ANTIALIAS)
        grid.paste(bim, (4320, 4080))
        grid.save("Output\\" + self.deck.name + ".jpg")

    #Just for manual download purposes
    def pictureDownload(self):
        for card in self.deck.cards:
            url = "http://mtgimage.com/card/" + card.name + ".jpg"
            if not os.path.exists("Output\\" + self.deck.name):
                os.makedirs("Output\\" + self.deck.name)
            for i in range(int(card.amount)):
                try:
                    urllib.request.urlretrieve(url, "Output\\" + self.deck.name + "\\" + card.name + str(i) + ".jpg" )
                except urllib.request.HTTPError:
                    print ("Please load " + card.name + " manually.")
                    continue


def main():
    pg = PictureGenerator("")
    pg.createSingle()

if __name__ == '__main__':                # call if module is called as main
    main()