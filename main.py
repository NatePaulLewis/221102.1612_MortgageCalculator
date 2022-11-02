# #Mortgage Calculator

class MonthlyPaymentFormula:
    def __init__(self, monthly_int_rate, num_monthly_payments, amount_borrowed, monthly_payment_formula):
        self.r = monthly_int_rate
        self.n = num_monthly_payments
        self.p = amount_borrowed
        self.c = monthly_payment_formula

    def FixedMortgageCalculation(self):
        pass


formula = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ** (-30 * 12)))
print(formula)
