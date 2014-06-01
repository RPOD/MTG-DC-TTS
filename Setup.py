# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MTG",
        version = "0.1",
        description = "Magic the Gathering - Deckcreator for Tabletop Simulator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("G:\\Documents\\Programming\\Fun\\MTG-DC-TTS\\MTG-DC-TTS\\Mtg.py", base=base)])