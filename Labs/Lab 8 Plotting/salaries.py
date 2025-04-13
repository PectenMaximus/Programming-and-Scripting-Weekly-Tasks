#imports
import numpy as np

# Make a list of random 10 salaries
minSalary = 20000
maxSalary = 80000
numberOfSalaries = 10

# Make the random salaries the same each time 
np.random.seed(0)

#Generate the random salaries
Salaries = np.random.randint(minSalary,maxSalary,numberOfSalaries)
print (' Salaries is = ',Salaries)

# Salaries Plus 5000
SalariesPlus= (Salaries + 5000)
print (' Salaries plus 5000 is = ', SalariesPlus)

# Salaries plus 5%
SalariesPlus5Percent = (Salaries*1.05)
print (' Salaries plus 5 percent is = ', SalariesPlus5Percent)

