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
import shutil

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
                print ("Could not load " + card.name)
                mode = 'y'
                while (mode != 'y' or 'n'):
                    mode = input("Do you want to continue without the card? [y/n]\n")
                    if (mode == 'y'):
                        break
                    if (mode == 'n'):
                        if not os.path.exists("tmp\\" + card.name):
                            os.makedirs("tmp\\" + card.name)
                        input("Please insert the cardimage from http://mtgimage.com/card/" +
                            card.name + ".jpg into the folder: tmp\\" + card.name + " manually\n\nPress Enter to Continue\n")
                        while(len(os.listdir("tmp\\" + card.name)) != 1):
                            input("Please insert just one imagefile.\n\nPress Enter to continue.\n")
                        tim = Image.open("tmp\\"+ card.name + "\\" + os.listdir("tmp\\" + card.name)[0])
                        tim = tim.resize((480, 680), Image.ANTIALIAS)
                        for i in range(int(card.amount)):
                            grid.paste(tim, (x, y))
                            x = x + 480
                            if (x == 4800):
                                x = 0
                                y = y + 680
                        break
                    else:
                        print("Please insert y or n.")
                shutil.rmtree('tmp', ignore_errors=True)
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

    def createRawPicture(self, deck, c):
        grid = Image.new('RGB', (4800, 4760))
        x = 0
        y = 0
        for card in deck:
            cim = Image.open("Input(raw)\\" + card)
            cim = cim.resize((480, 680), Image.ANTIALIAS)
            grid.paste(cim, (x, y))
            x = x + 480
            if (x == 4800):
                x = 0
                y = y + 680
        bim = Image.open("Input(raw)\\back\\" + os.listdir("Input(raw)\\back")[0])
        bim = bim.resize((480, 680), Image.ANTIALIAS)
        grid.paste(bim, (4320, 4080))
        grid.save("Output\\RawDeck\\Deck " + str(c) + ".jpg")

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