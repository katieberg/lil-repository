lilOne = 1
lilTwo = 1
lilSum = 0
while (lilOne+lilTwo<4000000):
  temp = lilOne + lilTwo
  lilOne = lilTwo
  lilTwo = temp
  if(temp%2==0):
      lilSum = lilSum + temp
print(lilSum)
