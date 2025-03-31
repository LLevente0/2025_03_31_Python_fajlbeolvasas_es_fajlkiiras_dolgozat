"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

versenyzok = []
futamok  = []
gyozelmek = []

with open("beolvasando_adatok/f1.txt", "r", encoding="utf-8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        versenyzo = adatok[0]
        csapat = adatok[1]
        gyozelmek_szama = int(adatok[2])
        futamok_szama = int(adatok[3])
        versenyzok.append(versenyzo)
        gyozelmek.append(gyozelmek_szama)
        futamok.append(futamok_szama)


futamok_atlaga = sum(futamok) / len(futamok)

max_futamok = max(futamok)
futamok_index = futamok.index(max_futamok)
legtobb_futamot_teljesito_versenyzo = versenyzok[futamok_index]

max_gyozelmek = max(gyozelmek)
gyozelmek_indek = gyozelmek.index(max_gyozelmek)
legtobb_gyozelem = versenyzok[gyozelmek_indek]


with open("kiirt_adatok/statisztika.txt", "w", encoding="utf-8") as celfajl:
    print(f"A beolvasott fájlban összesen {len(versenyzok)} versenyző szerepel.", file=celfajl)
    print(f"A legtöbb futamot nyert versenyző: {legtobb_gyozelem}", file=celfajl)
    print(f"A legtöbb futamot teljesített versenyző: {legtobb_futamot_teljesito_versenyzo}", file=celfajl)
    print(f"Az átlagos futamszám: {futamok_atlaga}", file=celfajl)
