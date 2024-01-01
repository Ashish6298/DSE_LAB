import pandas as pd

# Read Excel file
df = pd.read_csv(r'D:\p3.csv')

print("First few rows")
print(df.head())
print("\nSummary statistics")
print(df.describe())

filtered_data = df[df['Age'] > 30]
print("\nFiltered data (Age > 30):")
print(filtered_data)

sorted_data = df.sort_values(by='Salary', ascending=False)
print("\nSorted data (by Salary):")
print(sorted_data)

df['Bonus'] = df['Salary'] * 0.1
print("\nData with new column (Bonus):")
print(df)

df.to_csv('output.csv', index=False)
print("\nData written to output.xlsx")



# output
# First few rows
#          first_name  Age  Salary
# 0  Ailis Drinkwater   58   63465
# 1    Osbourn Wodham   39   89604
# 2    Ainsley Antill   56   60088
# 3       Tab Midford   57   43310
# 4     Kris Somerton   24   24713

# Summary statistics
#               Age        Salary
# count  1000.00000   1000.000000
# mean     39.17300  60326.539000
# std      11.07871  22850.981467
# min      21.00000  20095.000000
# 25%      29.00000  41243.000000
# 50%      39.00000  60100.000000
# 75%      49.00000  80382.000000
# max      58.00000  99932.000000

# Filtered data (Age > 30):
#            first_name  Age  Salary
# 0    Ailis Drinkwater   58   63465
# 1      Osbourn Wodham   39   89604
# 2      Ainsley Antill   56   60088
# 3         Tab Midford   57   43310
# 6      Emelia Izakson   34   47182
# ..                ...  ...     ...
# 989  Leanor Curgenven   40   93217
# 991      Danya Bhatia   43   83873
# 992     Elissa Realph   35   91013
# 993    Kaylil Wiggall   33   59922
# 996   Vergil Purbrick   47   75850

# [711 rows x 3 columns]

# Sorted data (by Salary):
#              first_name  Age  Salary
# 975       Zondra Frenzl   30   99932
# 876    Hester Lauritzen   41   99755
# 126         Torrin Muir   34   99706
# 272       Daveen Smogur   54   99698
# 649          Valene Bea   27   99616
# ..                  ...  ...     ...
# 330  Frasier Fitzgerald   56   20488
# 44     Leonanie Peppard   54   20376
# 711    Buckie Hovington   32   20284
# 867      Randene Goudie   23   20265
# 997       Arlene Huntar   22   20095

# [1000 rows x 3 columns]

# Data with new column (Bonus):
#            first_name  Age  Salary   Bonus
# 0    Ailis Drinkwater   58   63465  6346.5
# 1      Osbourn Wodham   39   89604  8960.4
# 2      Ainsley Antill   56   60088  6008.8
# 3         Tab Midford   57   43310  4331.0
# 4       Kris Somerton   24   24713  2471.3
# ..                ...  ...     ...     ...
# 995     Tiffy Riddick   26   37969  3796.9
# 996   Vergil Purbrick   47   75850  7585.0
# 997     Arlene Huntar   22   20095  2009.5
# 998  Ester Schaumaker   25   79296  7929.6
# 999   Felipe Messiter   27   88462  8846.2

# [1000 rows x 4 columns]

# Data written to output.xlsx










# class program

from functools import partial
def square(x):
    return x*x

def derivative(x):
    return 2*x

def difference_quotient(f,x,h):
    return(f(x+h)-f(x))/h

derivative_estimate=partial(difference_quotient,square,h=0.0001)
x_value=list(range(-10,10))
actual_derivatives=list(map(derivative,x_value))

estimate_derivatives=list(map(derivative_estimate,x_value))

import matplotlib.pyplot as plt
plt.title("Actual Derivative vs Estimates")
plt.plot(x_value,actual_derivatives,'rx',label="Actual")
plt.plot(x_value,estimate_derivatives,'b+',label="Estimate")
plt.legend(loc=9)
plt.show()

