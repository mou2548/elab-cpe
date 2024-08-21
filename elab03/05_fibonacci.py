def fibo(n):
  slow = 0
  fast = 1
  result = 1
  for i in range(n - 1):
    result = fast + slow
    slow = fast
    fast = result
  return result
