# Textový analyzátor

## Popis projektu
Jedná se o textový analyzátor - jednoduchý program, který se snaží prokousat libovolně dlouhým textem a zjistit o něm různé informace.

Program si od uživatele vyžádá přihlašovací jméno a heslo, zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů. Pokud je uživatel registrovaný, program začne analytovat text. Pokud není registrovaný, program jej zpozorní a skončí. Program aktuálně pracuje s předpřipravenými texty pro snadnější kontrolu kódu. 

Registrovaní jsou uživatelé: 
- bob (heslo: 123)
- ann, (heslo: pass123)
- mike (heslo: password123)
- liz (heslo: pass123)


Program nechá registrovaného uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

Pro vybraný text spočítá následující statistiky:
- počet slov
- počet slov začínajících velkým písmenem
- počet slov psaných velkými písmeny
- počet slov psaných malými písmeny
- počet čísel (ne cifer)
- sumu všech čísel (ne cifer) v textu
- program také vypíše četnosti různých délek slov v textu
