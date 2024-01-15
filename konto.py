class konto:
    def __init__(self,konto,guthaben,betrag):
        self.konto = konto
        self.guthaben = guthaben
        self.betrag = betrag

    def abheben(self):
        self.newbetrag = self.guthaben - self.betrag
        print(self.konto, 'sie haben ', self.betrag, ' abgehoben, Ihr aktueller Kontostand beträgt:', self.newbetrag)

    def einzahlen(self):
        self.newbetrag = self.guthaben + self.betrag
        print(self.konto, 'sie haben ', self.betrag, ' eingezahlt, Ihr aktueller Kontostand beträgt:', self.newbetrag)

a = konto('Pharrell',53,1000)
a.einzahlen()