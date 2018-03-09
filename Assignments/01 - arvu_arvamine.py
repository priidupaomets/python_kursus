arvatav_arv = 18
katsete_arv = 0
arvatud = False

while True:
    sisend = input("Palun sisesta number vahemikus [0..50]. Tsükli lõpetamiseks vajuta ENTER: ")
    if len(sisend) == 0:
        break

    katsete_arv += 1

    try:
        sisestatud_arv = int(sisend)
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
    print(f"Tubli Õige number oli {arvatav_arv}. Sa arvasid ära {katsete_arv} korraga")
else:
    print("Sa katkestasid ilma ära arvamata")

