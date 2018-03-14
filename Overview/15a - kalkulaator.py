"""
kalkulaator.py

Pisike kalkulaator kasutades pythoni vahendeid
"""

#
# Esmane variant
#

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
        if viimaneTulemus == 0:
            viimaneTulemus = eval(avaldis)
        else:
            viimaneTulemus = eval(str(viimaneTulemus) + avaldis)

while not katkesta:
    arvuta()
