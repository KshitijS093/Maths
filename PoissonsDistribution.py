#Poissons Distribution
import math

def poisson_distribution(lambda_value, k):
    return (lambda_value**k * math.exp(-lambda_value)) / math.factorial(k)

lambda_value = float(input("Enter the average number of successes within the given region: "))
k = int(input("Enter the actual number of successes that result in the given region: "))
result = poisson_distribution(lambda_value, k)
print("The Poisson's distribution is: ", result)