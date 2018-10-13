num1 = 1
numC = 1
stepnumber = 0
stepmax = 0
stepplot = []
numbers = []

while (numC != 1000000):
  while (num1 != 1):
    if (num1 % 2) == 0:
      num1 = (num1 / 2)
      stepnumber = stepnumber + 1
    else:
      num1 = (3 * num1) + 1
      stepnumber = stepnumber + 1
    if (stepnumber > stepmax):
      stepmax = stepnumber
  stepplot.append(stepnumber)
  numbers.append(numC)
  numC = numC + 1 
  num1 = numC
  stepnumber = 0

import matplotlib.pyplot as plt
x = numbers
y = stepplot
plt.scatter(x, y, label="circles", color="blue", marker=".", s=5)
plt.xlabel('Integer Value')
plt.ylabel('Number of Steps Taken to Converge')
plt.title('A Graphical Representation of the Collatz Problem')
plt.legend()
plt.show()
