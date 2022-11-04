# #Mortgage Calculator
class MonthlyPaymentFunds:
    def __init__(self):
        self.down_payment = int(input(f"How much are you putting down?: "))
        self.interest_rate = float(input(f"What's the interest rate?: "))
        self.mortgage_term = int(input(f"What is the duration of the mortgage?: "))
        self.principal = int(input(f"What is the cost of the home?: "))

    def __repr__(self):
        if self.mortgage_term == 30:
            return(f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr. fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f}")
        elif self.mortgage_term == 15:
            return(f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr. fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f}")
        elif self.mortgage_term == 10:
            return(f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}/6 ARM {self.interest_rate:.2f}% APR is: ${self.c:,.2f}")
        else:
            return(f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr. fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f}")

    def fixedMortgageCalculation(self):
        self.d = self.down_payment
        self.r = self.interest_rate / 100 / 12
        self.n = -abs(self.mortgage_term) * 12
        self.p = self.principal
        self.c = (self.r * (self.p - self.d)) / (1 - ((1 + self.r) ** self.n))
        return(self.c)

    def totalInterestPaidLifetime(self):
        self.i = (self.c * (self.n / 12)) - self.p
        print(f"Total Interest Paid Over Lifetime: ${abs(self.i):,.2f}")

m1 = MonthlyPaymentFunds()
m1.fixedMortgageCalculation()
m1.totalInterestPaidLifetime()
print(m1)