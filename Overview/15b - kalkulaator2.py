"""
kalkulaator2.py

Pisike kalkulaator kasutades pythoni vahendeid
"""

#
# Parandatud variant
#
import re   # Regulaaravaldised

katkesta = False
viimaneTulemus = 0

def arvuta():
    global katkesta
    global viimaneTulemus

    if viimaneTulemus == 0:
        avaldis = input("Sisesta avaldis (lõpetamiseks kirjuta \"stop\"): ")
    else:
        avaldis = input(str(viimaneTulemus))

    if avaldis == 'stop':
        print("Head aega")
        katkesta = True
    else:
        avaldis = re.sub('[a-zA-Z,.:=]', '', avaldis) # Puhastame avaldise

        if viimaneTulemus == 0:
            viimaneTulemus = eval(avaldis)
        else:
            viimaneTulemus = eval(str(viimaneTulemus) + avaldis)

while not katkesta:
    arvuta()
