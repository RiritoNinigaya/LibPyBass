@echo off

pyinstaller Main.py --windowed --onefile --name "PyLibBASS_Example" --icon "pylibbass.ico" --collect-binaries "bass" --collect-all "PyLibBass_Python"