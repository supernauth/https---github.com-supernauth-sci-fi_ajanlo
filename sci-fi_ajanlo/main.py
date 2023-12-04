from ajanlo import Ajanlo


ajanlo_app = Ajanlo("scifi", "db.json")
ajanlo_app.üdvözlés()

print("Nézzünk akkor egy könyvet!\nMutatom a műfajokat:")
for i in ajanlo_app.alműfaj_nyomtató():
    print(i)

választott_alműfaj = input("Melyik műfajból szeretnél választani? A fentiek közül tudsz választani: ")

print("Remek választás! A következő könyvet tudom ajánlani:")
random_könyv = ajanlo_app.véletlen_szám_sorsoló(választott_alműfaj)
olvasnivaló = ajanlo_app.műfaj_véletlen_könyve(választott_alműfaj, random_könyv)
print(olvasnivaló)
ajanlo_app.könyv_feljegyzése(választott_alműfaj, random_könyv)

