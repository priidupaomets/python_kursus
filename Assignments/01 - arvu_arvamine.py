"""
01 - arvu_arvamine.py

Antud ülesande eesmärgiks on genereerida mingi arv vahemikus 0..50 ning lasta kasutajal see 
ära arvata. Kui vastus polnud täpne, peaks välja trükkima kas oli väiksem või suurem kui 
otsitav arv. Kui arv õigesti ära arvati, peaks selle välja trükkima ning samuti ütlema,
mitu katset ära arvamiseks tehti.
Kui kasutaja soovib arvamise katkestada enne õige ära arvamist, võib ta sisestada lihtsalt 
tühja rea (rida, milles on vaid ENTER klahvi vajutus)
"""
arvatav_arv = 18  # Praegu me ei tea veel, kuidas juhuslikku arvu saada
katsete_arv = 0
arvatud = False

while True:
    sisend = input("Palun sisesta number vahemikus [0..50]. Tsükli lõpetamiseks vajuta ENTER: ")
    if len(sisend) == 0:
        break

    katsete_arv += 1

    try:
        sisestatud_arv = int(sisend)  # int() abil muundame sisestatud stringi numbriks

        if (sisestatud_arv == arvatav_arv):
            arvatud = True;
            break
        elif (sisestatud_arv < arvatav_arv):
            print("Liiga väike arv")
        else:
            print("Liiga suur arv")
    except:
        print("Vigane arv, proovi uuesti")

if (arvatud):
    print(f"Tubli, õige number oli {arvatav_arv}. Sa arvasid selle ära {katsete_arv} korraga")
else:
    print("Sa katkestasid ilma ära arvamata")

