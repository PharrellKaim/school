menge = float(input('Wie viele Liter haben sie getankt?'))
preis = float(input('Benzin Preis preis pro Liter'))

def benzinpreis(menge, preis):
    kosten = menge * preis
    print(kosten)


benzinpreis()

brustumfang = int(input('Bitte geben sie Ihren Brustumfang in cm an'))
geschlecht = str(input('männlich = m, weiblich = w'))
groesse = int(input('Bitte geben sie Ihre größe in cm an '))

def kleidergroeße(brustumfang):
    konfektionsgroesse = brustumfang / 2
    if geschlecht == 'w':
        konfektionsgroesse - 6


