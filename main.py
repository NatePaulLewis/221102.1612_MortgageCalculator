# #Mortgage Calculator
# formula = ((6.5 / 100 / 12) * 200000) / (1 - ((1 + (6.5 / 100 / 12)) ** (-30 * 12)))
# print(formula)
class MonthlyPaymentFunds:
    def __init__(self):
        self.interest_rate = float(input(f"Enter interest amount: "))
        self.mortgage_term = int(input(f"Enter mortgage term amount: "))
        self.principal = int(input(f"Enter principal amount: "))

    def __repr__(self):
        if self.mortgage_term == 30:
            return(f"Your monthly Mortgage Payment on a 30yr fixed: {self.c}.")
        elif self.mortgage_term == 15:
            return(f"Your monthly Mortgage Payment on a 15yr fixed: {self.c}")
        elif self.mortgage_term == 10:
            return(f"Your monthly Mortgage Payment on a 10/6 ARM: {self.c}")
        else:
            return(f"Your monthly Mortgage Payment on a {str(self.mortgage_term)} fixed: {self.c}")

    def fixedMortgageCalculation(self):
        self.r = self.interest_rate / 100 / 12
        self.n = -abs(self.mortgage_term) * 12
        self.p = self.principal
        self.c = (self.r * self.p) / (1 - ((1 + self.r) ** self.n))
        return(self.c)

    def totalInterestPaidLifetime(self):
        self.i = self.c * self.n - self.p
        print(f"Total Interest Paid Over Lifetime: {abs(self.i)}")

    def totalInterestPaid(self):
        self.i = (self.p * self.r - self.c) * (((1 +self.r) ** self.n -1) / self.r) + (self.c * self.n)
        print(f"Total Interest Paid: {abs(self.i)}")

    # def main(self):
    #     self.fixedMortgageCalculation()
    #     self.totalInterestPaidLifetime()
    #     return

# m1 = MonthlyPaymentFunds()
# if __name__ == '__main__':
#     m1

m1 = MonthlyPaymentFunds()
m1.fixedMortgageCalculation()
m1.totalInterestPaidLifetime()
m1.totalInterestPaid()
print(m1)