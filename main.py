nyelvek = []

with open('forrasf.txt', 'r', encoding='utf-8') as forrásfájl:
    next(forrásfájl)
    for sor in forrásfájl:
        adatok = sor.strip().split(';')
        ev = adatok[0]
        nev = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        nyelvek.append([ev, nev])


print(nyelvek)

with open('csakamikell.txt', 'w', encoding='utf-8') as célfájl:
    for adat in nyelvek:
        célfájl.write(f'{adat[0]} ')
        célfájl.write(f'{adat[1]}\n')
