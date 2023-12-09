# **Könyvajánló alkalmazás**

A hetekben fogom elérni a moly.hu oldalon a sci-fi-rajongóknak járó kitüntetést, ami 200 sci-fi regény elolvasása után jár. Egy ideje észrevettem, hogy nemsokára összejöhet a kellő számú olvasmány, de a vége felé nehézséget okozott a megfelelő regény megtalálása, válogatósnak bizonyultam.
Innen jött az ötlet, hogy jó lett volna egy ehhez hasonló applikáció.
Persze megtaláltam a megfelelő google keresés után, de hát ez így szórakoztatóbb. :)

Működési mechanizmusa a következő:

- az adatbázis egy _JSON_ fájlban található (_db.json_),
- ez a _JSON_ alműfajokra van felosztva, melyekben listákban találhatóak a következő könyvek, amelyek pedig szótár formátumban tartalmazza a következőket:
  - cím (_string_),
  - szerző (_string_),
  - sorozat része-e (_boolean_),
  - meg van-e filmesítve (_boolean_).
- a használt függvényeket külön fájlban lévő osztályba helyeztem el (_ajanlo.py_), majd importálom be a main.py-ba,
  - úgy írtam meg a programot, hogy bővíthető legyen más műfajokra is, tehát maga a sci-fi nincs bele _hardcode_-olva, hanem objektumváltozóként lehet bevinni,
  - az app először üdvözli a felhasználót,
  - utána megmutatja a JSON-ből kiolvasott alműfajokat,
  - ezután a felhasználónak be kell gépelnie az adott műfajt,
    - ha az űroperát vagy hard sci-fit választotta, megdícséri,
    - egyébként pedig tanácsot ad, hogy legközelebb arrafelé is nézelődjön,
    - ha rosszul írja be a műfajt, újra rákérdez,
  - véletlengenerátorral kidob egy regényt,
    - a különböző műfajokhoz különböző számú regényt vittem be, egyrészt, mert – mint korábban is látszott - vannak kedvenc műfajaim, másrészt pedig így izgalmasabb volt megírni a _randint_ metódust, :)
  - ezután az ajánlott könyvet és adatait lementi egy _ajanlas.txt_ fájlba,
    - a _JSON_ két _boolen_ változója alapján szöveges megfogalmazásban írja ki, könyvsorozat része-e, illetve készült-e belőle film- vagy sorozatadaptáció,
  - kiírja, hova mentette a gépen az ajánlást tartalmazó _.txt_ fájlt,
  - elköszön a felhasználótól.
