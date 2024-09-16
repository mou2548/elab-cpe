def readMat(fn='gauss01.txt'):
  m = []
  with open(fn) as fp:
    for line in fp:
      m.append(line.strip().split(' '))
  return m

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:>8}'
    print(row)
  print()

class Fraction():

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def compute_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    def simplify(self):
        gcd = Fraction.compute_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator // gcd)
        self.denominator = int(self.denominator // gcd)
        return self

    def evaluate(self):
        return self.numerator / self.denominator
    
    def __add__(self, other):
        lcm = (self.denominator * other.denominator) // Fraction.compute_gcd(self.denominator, other.denominator)
        numerator = (self.numerator * (lcm // self.denominator)) + (other.numerator * (lcm // other.denominator))
        return Fraction(numerator, lcm)
    
    def __mul__(self, other):
        new = Fraction(self.numerator, self.denominator)
        new.numerator *= other.numerator
        new.denominator *= other.denominator
        return new

    def __str__(self):
        self.simplify()
        if self.denominator == 1:
            return f'{self.numerator}'
        else:
            return f"{self.numerator}/{self.denominator}"

    def __format__(self, form):
        return f'{str(self):{form}}'
    
def divideMat(row, divisor):
    for col in range(len(m[row])):
        m[row][col] *= Fraction(divisor.denominator, divisor.numerator)

def minusMat(row, prime):
    for col in range(len(m[row])):
        m[row][col] +=  Fraction(-1) * prime[col]

def back_substitution(m):
    answer = [None]*ROWS
    for row in range(ROWS)[::-1]:
        answer[row] = m[row][-1]
        for col in range(row+1, COLS-1)[::-1]:
            if answer[col]:
                answer[row] += Fraction(-1) * m[row][col] * answer[col]
    return answer

filename = input("Enter filename: ")
m = readMat(filename)
VAL = 'abcdefghijklmnopqrstuvwxyz'
ROWS, COLS = len(m), len(m[0])

for row in range(ROWS):
    for col in range(COLS):
        m[row][col] = Fraction(int(m[row][col]))

print("Augmented Matrix:")
printMat(m)

for col in range(COLS):
    for row in range(ROWS):
        if row == col:
            divisor = m[row][col]
            print(f"R{row+1} => R{row+1}/({divisor})")
            divideMat(row, divisor)
            printMat(m)
        elif row > col and m[row][col].evaluate() != 0:
            multiplier = m[row][col]
            prime = [n*multiplier for n in m[col]]
            print(f"R{col+1}'->({multiplier})*R{col+1} [{', '.join(map(str, prime))}]")
            print(f"R{row+1} ==> R{row+1}-R{col+1}'")
            minusMat(row, prime)
            printMat(m)

answer = back_substitution(m)

print("Result from Gaussian Elimination:")
printMat(m)

print("After Back-Substitution:")
for i in range(ROWS):
    print(f"{VAL[i]} = {(answer[i])}")