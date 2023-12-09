from ajanlo import Ajanlo


ajanlo_app = Ajanlo("scifi", "db.json")
ajanlo_app.üdvözlés()

for i in ajanlo_app.alműfaj_nyomtató():
    print(i)

alműfaj_lista = ajanlo_app.alműfaj_nyomtató()
menő_műfaj = ["űropera", "hard sci-fi"]
kevésbé_menő_műfaj = [műfaj for műfaj in alműfaj_lista if műfaj not in menő_műfaj]

választott_alműfaj = input("\nMelyik műfajból szeretnél választani? A fentiek közül tudsz választani: ")

jó_választás = False

while not jó_választás:
    if választott_alműfaj in alműfaj_lista:
        if választott_alműfaj in menő_műfaj:
            print("\nRemek választás! A következő könyvet tudom ajánlani:")
            jó_választás = True
        elif választott_alműfaj in kevésbé_menő_műfaj:
            print("\nRendben, a lenti könyvet ajánlom. Azért vess egy pillantást az űropera vagy hard sci-fi felé is!")

        random_könyv = ajanlo_app.véletlen_szám_sorsoló(választott_alműfaj)
        olvasnivaló = ajanlo_app.műfaj_véletlen_könyve(választott_alműfaj, random_könyv)
        print(olvasnivaló)
        ajanlo_app.könyv_feljegyzése(választott_alműfaj, random_könyv)
        ajanlo_app.ajánlás_hely_kiíró()
        ajanlo_app.elköszönő()
        jó_választás = True
    else:
        választott_alműfaj = input("\nHibás alműfaj, próbáld újra: ")           



