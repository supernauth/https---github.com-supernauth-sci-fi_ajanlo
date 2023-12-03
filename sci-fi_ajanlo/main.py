import json
import random

class SciFiAjanlo:
    file_path = "db.json"

    def __init__(self):
        pass
    
    def műfaj_nyomtató(self):
        műfajok = []
        with open(self.file_path, "r") as file:
            db = json.load(file)

        for key in db.items():
            műfajok.append(key)
        
        return műfajok

    def műfaj_választó(self):
        választott_műfaj = input("Melyik műfajból választasz? ")
        return választott_műfaj

    def műfaj_véletlen_könyve(self):
        random_konyv = random.randint(0, len(self.db[self.műfaj_választó]))
        print(self.db[self.műfaj_választó][random_konyv]["cím"])
        
üdvözlő = """
Ma felvirradt a szerencsenapod. Úgy hírlik, hogy sci-fi regényt keresel.
Már feketeöves rajongó vagy vagy csak most ismerkedsz vele?

Mindegy is, csapjunk bele!
"""

print(üdvözlő)
további_könyv = True

ajanlo = SciFiAjanlo()

while további_könyv:
    pass

