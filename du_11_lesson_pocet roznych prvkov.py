# du_23.12.25_Počet rôznych prvkov
# Ak je daný zoznam čísel so všetkými jeho prvkami zoradenými vzostupne,
# určte a vypíšte počet rôznych
# prvkov v ňom.

cisla = input("Zadaj čísla: ").split()

posledne_cislo = cisla[0]
pocet_cisel = 1

for cislo in cisla:
    if cislo == posledne_cislo:
        pocet_cisel = pocet_cisel
    else:
        pocet_cisel = pocet_cisel + 1
        posledne_cislo = cislo

print(pocet_cisel)