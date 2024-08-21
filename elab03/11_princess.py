def caltime(x):
  total = x
  h = total // 3600
  total -= h * 3600
  m = total // 60
  total -= m * 60
  s = total
  return (h, m, s)

s = int(input("s: "))
time = caltime(s)
print(f"{s} seconds equals {time[0]} hour(s) {time[1]} minute(s) and {time[2]} second(s)")
