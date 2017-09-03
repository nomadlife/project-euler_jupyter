def getSumOfDivisors(number):
    total=0
    for i in range(1,number):
        if number%i==0:
            total=total+i
    return(total)

grandTotal=0
for i in range(1,10001):
    if i == getSumOfDivisors(getSumOfDivisors(i)):
        grandTotal = grandTotal + i
print(grandTotal)
