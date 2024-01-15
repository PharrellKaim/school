class stepcounter:
    def __init__(self, date):
        self.date = date
        self.steps = 0

    def incrementStep(self):
        self.steps = self.steps + 1

    def toString(self):
        print('Am ' , self.date , 'bin ich ' ,self.steps , ' Schritte gegangen.')


a = stepcounter('27.05.2022')


for i in range(1200):
    a.incrementStep()

a.toString()