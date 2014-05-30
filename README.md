MTG-DC-TTS
==========

Magic the Gathering deck creator tool for Tabletop Simulator

author: R.P.O.D.
Version: 0.1

This is a little Program which reads MTG-Deck files in from tappedout.net
and creates a valid picture for Tabletopsimulator in order to load a costum
deck into the game.

Note for some reason some card images throw a 400 HTTP Error, Pictures will
be still created though will be incomplete. Check the console output to see
which cards couldn't be loaded

Usage:
download the .txt file from any deck you (or someone else) has creates on
http://tappedout.net/mtg-decks/ and insert all files into the "Input" 
folder. 
Excecute MTG.py
The outputfolder should contain the pictures.


!!!IMPORTANT NOTE!!!

If a card name contains a \ pleae replace it with just a blank symbol
For example: Bound \ Determined , it should be Bound Determined
Please check the .txt filebeforehand
