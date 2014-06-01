# -*- coding: utf-8 -*-
"""
@author: R.P.O.D.
Class for Uploading the Output directory to imgur

===============================================================================
                                Upload Class
===============================================================================
"""

import pyimgur
import os
import datetime


class Upload:

    CLIENT_ID = "604c1ff13919c01"

    def __init__(self, mode, names):
        self.mode = mode
        self.names = names

    def uploadFiles(self):
        im = pyimgur.Imgur(self.CLIENT_ID)
        links = []
        for picture in os.listdir("Output"):
            if (picture == "RawDeck" and self.mode == 'r'):
                for rawpic in os.listdir("Output\\RawDeck"):
                    uploaded = im.upload_image("Output\\RawDeck\\" + rawpic, title=rawpic + " uploaded through MTG-DC-TTS.")
                    links.append(uploaded.link)
                break
            else:
                for name in self.names:
                    if name in picture:
                        uploaded = im.upload_image("Output\\" + picture, title=picture[:-4] + " uploaded through MTG-DC-TTS.")
                        links.append(uploaded.link)
        c = 1
        while True:
            if not os.path.exists("Output\\links " + str(datetime.date.today()) + ".txt"):
                output = open("Output\\links " + str(datetime.date.today()) + ".txt", 'w+')
                break
            if not os.path.exists("Output\\links " + str(datetime.date.today()) + " " + str(c) + ".txt"):
                output = open("Output\\links " + str(datetime.date.today()) + " " + str(c) + ".txt", 'w+')
                break
            else:
                c = c + 1
        for link in links:
            output.write(link + "\n")
        output.close()