from ajanlo import Ajanlo


ajanlo_app = Ajanlo("scifi", "db.json")
ajanlo_app.üdvözlés()

for i in ajanlo_app.alműfaj_nyomtató():
    print(i)

alműfaj_lista = ajanlo_app.alműfaj_nyomtató()
menő_műfaj = ["űropera", "hard sci-fi"]
kevésbé_menő_műfaj = [műfaj for műfaj in alműfaj_lista if műfaj not in menő_műfaj]

# kevésbé_menő_műfaj = ajanlo_app.alműfaj_nyomtató().remove("űropera")

választott_alműfaj = input("\nMelyik műfajból szeretnél választani? A fentiek közül tudsz választani: ")

jó_választás = True

while jó_választás:
    try:
        if választott_alműfaj == "űropera" or választott_alműfaj == "hard sci-fi":
            print("\nRemek választás! A következő könyvet tudom ajánlani:")
        else:
            print("\nRendben, a lenti könyvet ajánlom. Azpért vess egy pillantást az űropera vagy hard sci-fi felé is!")

            random_könyv = ajanlo_app.véletlen_szám_sorsoló(választott_alműfaj)
            olvasnivaló = ajanlo_app.műfaj_véletlen_könyve(választott_alműfaj, random_könyv)
            print(olvasnivaló)
            ajanlo_app.könyv_feljegyzése(választott_alműfaj, random_könyv)
            ajanlo_app.ajánlás_hely_kiíró()
            ajanlo_app.elköszönő()
        break
    except:
        print("Hibás alműfaj.")
        választott_alműfaj = input("Próbáld újra: ")



