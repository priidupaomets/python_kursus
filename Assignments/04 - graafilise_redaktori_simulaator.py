"""
04 - graafilise_redaktori_simulaator.py

Sarnane eelmisele, kuid klassi hierarhia asemel tuleb luua klasside struktuur (vajadusel
võib ka teatud määral hierarhiat kasutada). Eesmärgiks on luua graafilise kujundite redaktori
simulaator, mis võimaldaks moodustada erinevatest elementidest "põrandaplaane". Nende elementide
hulka kuuluvad tekst, pilt, graafiline sümbol (palju erinevaid tüüpe), sisse laetud suvaline 
sümbol jne.

Elemente peab olema võimalik joonistada (sarnaselt eelmisele ülesandele me hetkel lihtsalt
trükime teate, et joonistame seda elementi) ning eksportida. Samuti peab element teadma, kas
tema peale hiirega klikkides jääb tema sinna alla või mitte (ehk teisisõnu omab ta funktsiooni,
mis testib kas etteantud koordinaadid jäävad tema asukoha ja suuruse sisse).

Igal elemendil on ID (juhuslik number) ja nimi, mis lubab seda unikaalselt tuvastada. Soovi 
korral võime lisada ka kirjelduse. Kindlasti on neil asukoht, suurus, värv ja võib-olla veel
mingid omadused (võite ise välja mõelda, mida vaja võiks olla).

Rakenduse lõpuks looge klassidest objektid, lisage need mingisse listi ning testige kogu loodud 
funktsionaalsust - ehk laske neil end joonistada, eksportige kogu objektide graaf ning testige
mingeid koordinaate tuvastamaks, kas mõni objekt jääb sinna alla.

"""

