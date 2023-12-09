import json
import random
import os

class Ajanlo:
    """Ez egy olyan könyvajánló alkalmazás, ami egy megfelelő szerkezetű JSON
    fájllal együttdolgozva könyvet ajánl a felhaszálónak, a felhasználó
    által kiválasztott alműfaj alapján.
    Az ajánlást a végén txt fájlba írja.
    """
    
    def __init__(self, műfaj, útvonal):
        """Az adatbázis fő műfaja és elérhetősége.
        """
        self.műfaj = műfaj
        self.útvonal = útvonal

    def üdvözlés(self):
        """A folyamat kezdeteként köszöntjük a felhasználót.
        """
        üdvözlő_szöveg = f"""
Ma felvirradt a szerencsenapod. Úgy hírlik, hogy {self.műfaj} regényt keresel.
Már feketeöves rajongó vagy vagy csak most ismerkedsz vele?
Mindegy is, csapjunk bele!

Nézzünk akkor egy könyvet!

Mutatom a műfajokat:"""
        return print(üdvözlő_szöveg)
    
    def alműfaj_nyomtató(self):
        """A JSON-ból kiolvasva kiírja a terminálba az alműfajokat.
        """
        alműfajok = []
        with open(self.útvonal, "r") as file:
            db = json.load(file)

        for key, value in db.items():
            alműfajok.append(key)
        
        return alműfajok

    def alműfaj_választó(self):
        """A felhasználónak be kell gépelnie a felsorot alműfajok valamelyikét.
        """
        választott_alműfaj = input("Melyik alműfajból választasz? ")
        return választott_alműfaj

    def véletlen_szám_sorsoló(self, alműfaj):
        """Az adott alműfaj listahossza alapján generál egy véletlen számot.
        """
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            random_könyv_sorszám = random.randint(0, (len(db[alműfaj]) - 1))
            return random_könyv_sorszám

    def műfaj_véletlen_könyve(self, alműfaj, sorszám):
        """Az előző függvényben kiválasztott sorszámot felhasználva kiírja
        a konzolba a kisorsolt könyv szerzőjét és címét.
        """
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            szerző = db[alműfaj][sorszám]["szerző"]
            könyv = db[alműfaj][sorszám]["cím"]
            return f"{szerző}: {könyv}"

    def könyv_feljegyzése(self, alműfaj, sorszám):
        """A korábban kiválasztott könyvet feljegyzi egy txt fájlba,
        megfogalmazva azt is, hogy könyvsorozat része-e, valamint
        hogy van e film- vagy sorozatadaptáció belőle.
        """
        with open(self.útvonal, "r") as file:
            db = json.load(file)
            with open("ajanlas.txt", "w") as ajánlás:
                ajánlás.write("szerző: ")
                ajánlás.write(db[alműfaj][sorszám]["szerző"])
                ajánlás.write("\n")
                ajánlás.write("cím: ")
                ajánlás.write(db[alműfaj][sorszám]["cím"])
                ajánlás.write("\n")
                if db[alműfaj][sorszám]["sorozat része"] == True:
                    ajánlás.write("Egy könysorozat része, van folytatása.")
                else:
                    ajánlás.write("Sajnos folytatása nincsen.")
                ajánlás.write("\n")
                if db[alműfaj][sorszám]["film adaptáció"] == True:
                    ajánlás.write("Ha tetszik, jó hír, mert készült belőle film vagy sorozat adaptáció.")
                else:
                    ajánlás.write("Eddig nem készült belőle film- vagy sorozatadaptáció.")

    def ajánlás_hely_kiíró(self):
        """Kiírja a konzolba, hova mentette az ajánlást tartalmazó fájlt.
        """
        hely = os.getcwd()
        hely_string = print(f"\nAz ajánlást részletesen lementettem az alábbi helyre:\n{hely}/ajanlas.txt\n")

    def elköszönő(self):
        """Elköszön a felhasználótól.
        """
        print("Köszönjük a megkeresést, jó olvasást kívánunk!")
        
