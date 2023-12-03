import json
import random

class SciFiAjanlo:
    
    def __init__(self, útvonal):
        self.útvonal = útvonal
    
    def műfaj_nyomtató(self):
        műfajok = []
        with open(self.útvonal, "r") as file:
            db = json.load(file)

        for key, value in db.items():
            műfajok.append(key)
        
        return műfajok

    def műfaj_választó(self):
        választott_műfaj = input("Melyik műfajból választasz? ")
        return választott_műfaj

    def véletlen_szám_sorsoló(self, műfaj):
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            random_könyv_sorszám = random.randint(0, (len(db[műfaj]) - 1))
            return random_könyv_sorszám

    def műfaj_véletlen_könyve(self, műfaj, sorszám):
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            könyv = db[műfaj][sorszám]["cím"]
            return könyv

    def könyv_feljegyzése(self, zsáner, sorszám):
         with open(self.útvonal, "r") as file:
            db = json.load(file)
            with open("ajanlas.txt", "w") as ajánlás:
                ajánlás.write(db[zsáner][sorszám]["cím"])
                ajánlás.write(db[zsáner][sorszám]["szerző"])
                ajánlás.write(str(db[zsáner][sorszám]["sorozat része"]))
                ajánlás.write(str(db[zsáner][sorszám]["film adaptáció"]))
        

üdvözlő = """
Ma felvirradt a szerencsenapod. Úgy hírlik, hogy sci-fi regényt keresel.
Már feketeöves rajongó vagy vagy csak most ismerkedsz vele?
Mindegy is, csapjunk bele!
"""


print(üdvözlő)
ajanlo = SciFiAjanlo("db.json")

print("Nézzünk akkor egy könyvet!\nMutatom a műfajokat:")
for i in ajanlo.műfaj_nyomtató():
    print(i)

választott_műfaj = input("Melyik műfajból szeretnél választani? A fentiek közül tudsz választani: ")

print("Remek választás! A következő könyvet tudom ajánlani:")
random_könyv = ajanlo.véletlen_szám_sorsoló(választott_műfaj)
olvasnivaló = ajanlo.műfaj_véletlen_könyve(választott_műfaj, random_könyv)
print(olvasnivaló)
ajanlo.könyv_feljegyzése(választott_műfaj, random_könyv)

