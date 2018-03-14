"""
moodulid.py

Väliste moodulite kasutamine ja oma moodulite loomine
"""

#
#  funktsionaalsuse importimine ja main() funktsioon
#
import platform       # Üldine mooduli importimise formaat
from sys import argv  # Impordime sys moodulist vaid argv
from random import *  # Universaalne importimine: kogu random mooduli sisu

def main():
    message()

def message():
    print(f"Python v{platform.python_version()}")
    print(f"Argumendid: {argv}") # Trükime käsurea argumendid
    print(f"Juhuslik arv vahemikus [0..50]: {randint(0, 51)}")
    print()

# Sedasi kutsume välja main() funktsiooni
if __name__ == '__main__': 
    main()


#
# Lihtsa mooduli loomine
#
import mymodule

mymodule.tere()

#
# Korduvkasutatavate funktsioonde teistesse failidesse tõstmine
#
import mycode
from mycode import functions

print(mycode.functions.numavg(1)) # üldise import puhul 
print(functions.numavg())         # mooduli impordi puhul

print(dir(mycode))
print(dir(mycode.functions))