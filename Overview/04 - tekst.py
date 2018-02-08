"""
tekst.py

Teksti tüübi deklareerimine ja kasutamine
"""

# Nagu juba mainitud, kirjutatakse tekstijada (string) kas jutumärkide või ülakomade vahele
# Tähtis on see, et sama sümbol, millega string algab, peab ta ka lõppema

# Kõige lihtsam tekstijada
print("See on tekstijada")

# Vigane tekst
print("See on tekstijada')

# Järgnev annab meile samuti süntaksi vea, kuigi lõpeb sama sümboliga...
print("Ford vaatas teda. "Kas see robot ütles Zaphod Beeblebrox?", küsis ta")
# SyntaxError: invalid syntax

# Põhjuseks on teksti sees olevad jutumärgid, mis meie teksti segi ajavad

# Esimene võimalus seda parandada on kasutada ülakomasid
print('Ford vaatas teda. "Kas see robot ütles Zaphod Beeblebrox?", küsis ta')

# Mis aga teha siis, kui meie tekstis võivad ka ülakomad esineda?

# Sellisel juhul on hea kasutada päästvaid jadasid (escape sequence). 
# Need kirjutatakse kaldkriipsuga ning sellisel juhul võetaks reserveeritud
# sümboleid mitte käskude vaid tekstisümbolitena
print("Ford vaatas teda. \"Kas see robot ütles Zaphod Beeblebrox?\", küsis ta")

'Ford vaatas teda. "Kas see robot ütles Zaphod Beeblebrox?", küsis ta'


# Nii nagu me arvude juures nägime, oli seal võimalik kasutada aritmeetrilisi
# operatsioone. Tekstijadade puhul saab mõningaid sarnaseid tehteid kasutada,
# kuigi nende mõte või semantika on pisut erinev

# Esiteks liitmistehe. See ühendab erinevad tekstilõigud omavahel üheks suureks tervikuks
print("See" + "on" + "üks" + "tekstijada") # Väljund: 'Seeonükstekstijada'

# kummaline, paistab, et tühikud sõnade vahel on kaduma läinud. Tegelikult, 
# kui hästi vaadata, siis meil polnudki sõnade vahel tühikuid... Ja nii ongi,
# et kui me soovime stringide liitmist (ehk konkatenatsiooni) kasutada, 
# peame hoolitsema ka sobivas kohas asuva tühiku eest
print("See " + "on " + "üks " + "tekstijada") # Väljund: 'See on üks tekstijada'

# või selliselt
print("See" + " on" + " üks" + " tekstijada") # Väljund: 'See on üks tekstijada'

# Mis te arvate, kumb variant võiks parem olla?

# Kui me tahaks näiteks tekstijadasse sisse panna ka teisi andmetüüpe, siis 
# ilmselt esimene mõte oleks proovida midagi sellist:
print("Tekst" + 6)
#  ...kuid see annab meile vea
'''
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    "Tekst" + 6
TypeError: must be str, not int
'''

# Korrektne meetod oleks kasutada str() funktsiooni, mis muundab teised andmetüübid stringiks
print("Tekst" + str(6)) # Väljund: Tekst6



# Stringide juures saab kasutada ka korrutustehet. Mis moodi selle semantika
# defineeritud võiks olla?
# Vastus: Ta kordab teksti soovitud arv kordi

print("Tere" * 3) # Väljund: 'TereTereTere'

# Huvitav, kus meil peaks sellist asja vaja olema?

print("-" * 20) # Väljund: '--------------------'

# Lahutamise, jagamise, astendamise jt tehete semantikat stringid ei toeta 
# Kui me seda proovime, saame veateate
print("Tekst" - "st")
'''
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    "Tekst" - "st"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
'''


# Tekst on sisuliselt sümbolite jada ning meil on võimalik pöörduda ka üksikute
# sümbolite poole. Oletame, et meil on järgnev tekst, mille esimest sümbolit 
# tahaks kätte saada

tekst = "Ford vaatas teda. \"Kas see robot ütles Zaphod Beeblebrox?\", küsis ta"
print (tekst[1]) # Väljund: 'o'

# hmmmm... huvitav, me pidime ju esimese sümboli saama, aga saime hoopis teise...
# Mis küll seda põhjustada võiks?

# See tuleneb asjaolust, et enamus programmeerimiskeeli on omaks võtnud nullil
# baseeruvad indeksid (kui muutuja "tekst" viitab teksti algusele, siis teksti_algus + 0
# on esimene sümbol, teksti_algus + 1 on teine sümbol jne kuni 
# teksti_algus + (teksti_pikkus - 1) on viimane)

# Seega esimese sümboli saamiseks peame kirjutama:
print(tekst[0]) # Väljund: 'F'


#
# Kõrvalepõige kooditabelite, fontide ja tekstijadade olemusse
#


#
# Lõigud
#

# Võtame välja lõigu, mis sisaldab sõna "Ford"
print(tekst[0:4]) # Väljund: 'Ford'

# Veel üks tekstilõik
print(tekst[19:57]) # Väljund: 'Kas see robot ütles Zaphod Beeblebrox?'

# Kogu tekst alates 18-ndast indeksist
print(tekst[18:]) # Väljund: '"Kas see robot ütles Zaphod Beeblebrox?", küsis ta'

# Tekst stringi algusest kuni soovitud positsioonini
print(tekst[:4]) # Väljund: 'Ford'

# Tekst algusest, välja arvatud viimased 10 sümbolit
print(tekst[:-10]) # Väljund: 'Ford vaatas teda. "Kas see robot ütles Zaphod Beeblebrox?"'

# Indekseerimist saab kasutada ka literaalse stringi peal
print("See on tekst"[:3]) # Väljund: 'See'

# Iga teise elemendi saamine lõigust
print(tekst[19:57:2]) # Väljund: 'KsserbtülsZpo eberx'

# Me saame ka tagurpidi jada pärida
print(tekst[56:18:-1]) # Väljund: '?xorbelbeeB dohpaZ seltü tobor ees saK'
# ning ka see võib olla üle N märgi
print(tekst[56:18:-2]) # Väljund: '?obleBdha et oo e a'

# Võtame lõpust -nda sümboli
print(tekst[-12]) # Väljund: '?'


#
# print() funktsiooni laiemad kasutusvõimalused ja teksti formateerimine
#

# Esmalt vaatame, kuidas erinevaid andmetüüpe ühtseks väljundiks kokku liita. 
# Varem vaatasime seda kasutades str() funktsiooni
# Print funktsioon lubab talle parameetritena kaasa anda suvalise arvu argumente ning 
# teeb andmetüüpide konversiooni automaatselt, seega pole str() kasutamine seal vajalik.
print("Aastavahetus oli ", 33, " päeva tagasi") # Väljund: Aastavahetus oli  33  päeva tagasi

# Kui me varem stringide liitmisel pidime ise tühikud lisama, siis siin paistab, et see
# tekitab hoopis ülearused tühikud. Paistab, et print() kannab juba ise selle eest hoolt.
# Parandamiseks eemaldame ülearused tühikud:
print("Aastavahetus oli", 33, "päeva tagasi") # Väljund: Aastavahetus oli 33 päeva tagasi


#
# Stringi formateerimine (uuem formaat)
#

# stringe saab moodustada ka kasutades spetsiaalseid formateerimiskäske, mis kirjutatakse
# loogeliste sulgude {} vahele. Kui me soovime sulge endid väljastada, paneme neid topelt {{ }}
# https://docs.python.org/3/library/string.html#string-formatting

# Formateerimine positsiooniliste muutujatega
# ... lihtsalt järjekorras
print("Tere {}, aastavahetusest on möödas {} päeva".format("Mati", 33))
# ... argumendi indeksi alusel (lubab parameetrile viidata suvalisest kohast ja kasvõi mitu korda)
print("Tere {0}, aastavahetusest on möödas {1} päeva".format("Mati", 33))

# ... sama, mis eelmine, kuid kasutame väärtust mitu korda ja suva järjestuses
print("{1} Tere {0}, aastavahetusest on möödas {1} päeva".format("Mati", 33))

# ... nimeliselt - veelgi lihtsam parameetrite väärtusi määrata kuna pole kinni positsioonis
print("Tere {nimi}, aastavahetusest on möödas {vanus} päeva".format(nimi = "Mati", vanus = 33))


# Katsetame konversiooni parameetreid
print("Testime !s {0!s}, !r {0!r}, !a {0!a}".format(28.5))


# Formaadi spetsifikaatorid
# ... vasak joondamine
print('{:<30}'.format('left aligned'))
# ... parem joondamine
print('{:>30}'.format('right aligned'))
# ... tsentreerimine
print('{:^30}'.format('centered'))
# ... tsentreerimine koos täitesümboliga
print('{:*^30}'.format('centered'))  # kasuta '*' kui täite sümbolit

# ujukomaarvud
print('{0:+f}; {1:+f};  {0: f}; {1: f};  {0:-f}; {1:-f}'.format(3.14, -3.14))

# täisarvud eri kujul
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# täisarvud alternatiivsel kujul
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

# tuhandete eraldaja
print('{:,}'.format(1234567890))

# kasutame protsendi märki
print('Correct answers: {:.2%}'.format(19/22))


#
# Teksti sisestamine
#

# Sisendi ootamine ilma seletuseta
sisend = input()
print(sisend)

# sisendi ootamine koos seletava tekstiga. NB! Kui soovime tühikut selle teksti ja 
# sisestatava väärtuse vahel, tuleb see meil teksti lõppu lisada
sisend = input("Palun sisesta arv vahemikus 1..50:")
print("Sa sisestasid: {0}".format(sisend))

