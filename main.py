# #Mortgage Calculator
# formula = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ** (-30 * 12)))
# print(formula)
class MonthlyPaymentFunds:
    def __init__(self, interest_rate, mortgage_term, principal):
        self.interest_rate = interest_rate
        self.mortgage_term = mortgage_term
        self.principal = principal

    def fixedMortgageCalculation(self):
        self.r = self.interest_rate / 100 / 12
        self.n = -abs(self.mortgage_term) * 12
        self.p = self.principal
        self.c = (self.r * self.p) / (1 - ((1 + self.r) ** self.n))
        print(self.c)

m1 = MonthlyPaymentFunds(6.5, 30, 200000)
m1.fixedMortgageCalculation()




