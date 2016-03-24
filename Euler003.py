def isPrime(num):
  if (num%2 == 0):
    return False
  for i in range(3,round(num**.5),2):
    if(num%i) == 0:
      return False
  return True

bigNum = 600851475143
toCheck = int(bigNum**.5)
while(not isPrime(toCheck)):
  while(bigNum%(toCheck-1) != 0):
    toCheck = toCheck - 1
  toCheck = toCheck - 1
print(toCheck)
