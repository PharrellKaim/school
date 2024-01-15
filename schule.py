class cat():
    def __init__(self, gewicht, name, alter):
        self.gewicht = gewicht
        self.name = name
        self.alter = alter

    def mew(self):
        print("meow, meow, meow")

    def sleep(self):
        print("zzzzzz")

    def eat(self):
        if self.gewicht > 10:
            print("Bitte Ligth-Futter")

        else:
            print("Bitte Normales futter geben")

    def cuddle(self):
        pass


KatzeAlfons = cat(20,"Alfons", 13)
KatzeAlfons.eat()
KatzeAlfons.mew()
KatzeAlfons.sleep()

