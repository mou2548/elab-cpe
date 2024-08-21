# เขียนฟังก์ชันเพื่อใช้หา Alternative Sum
def altsum(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
        else:
            total -= i
    return total

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, altsum(n)))
