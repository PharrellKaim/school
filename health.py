class health:
    def __init__(self, groeße, gewicht, geschlecht):
        self.gewicht = gewicht
        self.groeße = groeße
        self.geschlecht = geschlecht

    def calculation(self):
        self.bmi = self.gewicht * 10000 / (self.groeße * self.groeße)


    def number(self):
        if self.geschlecht == 'Mann' and self.bmi < 20:
            print('Mit einem BMI von ', self.bmi, ' sind sie Untergewichtig')

        elif self.geschlecht == 'Frau' and self.bmi < 19:
            print('Mit einem BMI von ', self.bmi, ' sind sie Untergewichtig')

        elif self.geschlecht == 'Mann' and self.bmi < 26:
            print('Mit einem BMI von ', self.bmi, ' sind sie Normalgewichtig')

        elif self.geschlecht == 'Frau' and self.bmi < 25:
            print('Mit einem BMI von ', self.bmi, ' sind sie Normalgewichtig')

        elif self.geschlecht == 'Mann' or 'Frau' and self.bmi < 30:
            print('Mit einem BMI von ', self.bmi, ' sind sie Übergewichtig')

        else:
            print('Mit einem BMI von ', self.bmi, ' sind sie Behandlungsbedürftig Übergewichtig')





a = health(172, 68, 'Mann')
a.calculation()
a.number()