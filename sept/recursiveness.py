# normal
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result
n = int(input("enter number: "))
result = factorial(n)
print(result)

# recursive
def recfact(n):
    if n == 0:
        result = 1
    else:
        result = n*recfact(n-1)
    return result
print (recfact(5))