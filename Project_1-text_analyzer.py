'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = "=" * 65
uzivatelske_udaje = {"bob" : "123",
                    "ann" : "pass123",
                    "mike" : "liz",
                    "liz" : "pass123"}
# Zadání a kontrola uživatele + uvítání
aktivni_uzivatel = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")
print(oddelovac)

if aktivni_uzivatel in uzivatelske_udaje and uzivatelske_udaje[aktivni_uzivatel] == heslo:
    print(f"Ahoj {aktivni_uzivatel}, vítáme tě v našem textovém analyzátoru!".center(len(oddelovac)), "Máme 3 texty, které můžeme analyzovat".center(len(oddelovac)), oddelovac, sep = "\n")
else:
    print("Nesprávné uživatelské jméno nebo heslo, ukončuji program.")
    quit()

# Zadání a kontrola čísla textu
cislo_textu = input("Zadej číslo textu, který mám analyzovat (1,2 nebo 3): ".center(len(oddelovac)))
if cislo_textu.isnumeric() and int(cislo_textu) in range(1,4):
    print(f'Analyzuji text: "{cislo_textu}".'.center(len(oddelovac)), oddelovac, sep = "\n")
else:
    print(f'Text "{cislo_textu}" není v nabídce, ukončuji program'.center(len(oddelovac)), oddelovac, sep = "\n")
    quit()

# Seznam slov (získám z nich celkový počet)
# DOTAZ = Lze slova očistit nějakým elegantnějším způsobem, přijde mi to zbytečně složité...?
seznam_slov = [slova.strip(",.?!:;") for slova in TEXTS[int(cislo_textu) -1].split()]

# slova, která začínají velkým písmenem
titlecase_word = [statistika for statistika in seznam_slov if statistika.istitle()]

# slova psaná velkými písmeny
uppercase_word = [statistika for statistika in seznam_slov if statistika.isalpha() and statistika.isupper()]

# slova psaná malými písmeny
lowercase_word = [statistika for statistika in seznam_slov if statistika.isalpha() and statistika.islower()]

# počet čísel
cisla = [int(statistika) for statistika in seznam_slov if statistika.isnumeric()]

# suma čísel
suma_cisel = sum(cisla)

print(f"""V textu se nachází celkově:
{len(seznam_slov)} slov
{len(titlecase_word)}x slovo, které začíná velkým písmenem
{len(uppercase_word)}x slovo, které obsahuje pouze velká písmena
{len(lowercase_word)}x slovo, které obsahuje pouze malá písmena
{len(cisla)}x číslo
Suma všech čísel je {suma_cisel}. 
{oddelovac} """)

# data pro sloupcový graf, klíč slovníku = délka slova, hodnota = počet slov s danou délkou
cetnost = dict()

for slovo in seznam_slov:
    if len(slovo) not in cetnost:
        cetnost[len(slovo)] = 1
        continue
    else:
        cetnost[len(slovo)] += 1

# seřazení hodnot a tisk "grafu"
tuply = sorted(cetnost.items())

d, v, p = "délka slova", "výskyt", "počet"      # pomocné proměnné sloužící jen k zarovnání tisku
print(f"{d:>15}{v:^30}{p:<15}")
print(oddelovac)

for cisla in tuply:
    vysledek_1, vysledek_2, vysledek_3 = str(cisla[0]), str("*" * cisla[1]), str(cisla[1])          # pomocné proměnné sloužící jen k zarovnání tisku
    print (f"{vysledek_1.center(len(d)):>15}{vysledek_2.center(len(v)):^30}{vysledek_3.center(len(p)):<15}")

# Prosím o komentář jak efektivně vytisknout výstup grafu. Přijde mi to krkolomné a nepřišel jsem na to, jak způsobit,
# aby graf z * byl opravdu grafem a ne zarovnanými * na střed. Pokud místo metody center() využiji metodu ljust(), vznikne z toho rozsypaný čas...
# Díky za komentář i super kurz!