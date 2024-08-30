class Fraction():

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    def compute_lcm(x, y):
        lcm = (x*y) // Fraction.compute_gcd(x, y)
        return lcm
    
    def simplify(self):
        gcd = Fraction.compute_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
        return self

    def evaluate(self):
        return self.numerator / self.denominator
    
    def add(self, n):
        self.numerator += self.denominator * n
        return self
    
    def __add__(self, other):
        new = Fraction(self.numerator, self.denominator)
        lcm = Fraction.compute_lcm(new.denominator, other.denominator)
        new.numerator *= lcm / new.denominator
        new.denominator *= lcm / new.denominator
        other.numerator *= lcm / other.denominator
        other.denominator *= lcm / other.denominator
        new.numerator += other.numerator
        return new

    def multiply(self, n):
        self.numerator *= n
        return self
    
    def __mul__(self, other):
        new = Fraction(self.numerator, self.denominator)
        new.numerator *= other.numerator
        new.denominator *= other.denominator
        return new

    def __str__(self):
        self = self.simplify()
        if self.numerator == 0:
            return "0 / 1"
        else:
            return f"{self.numerator} / {self.denominator}"
        
print(Fraction(22,14))
print((Fraction(1,2) + Fraction(3,4)).multiply(0))
print((Fraction(22,14) * Fraction(2, 4)).add(1))
print(Fraction(22, 7).multiply(7).multiply(7))