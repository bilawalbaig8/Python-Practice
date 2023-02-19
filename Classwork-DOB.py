#Program to calculate the age from DOB
#Function Definition
import math
def calculateAge(dob):
    current_date="18-2-2023"
    [cday, cmonth, cyear] = current_date.split("-")
    [bday, bmonth, byear] = dob.split("-")

    # casting string values to numeric
    cday = int(cday)
    cmonth = int(cmonth)
    cyear = int(cyear)
    bday = int(bday)
    bmonth = int(bmonth)
    byear = int(byear)

    # main logic
    # age in days
    if cday - bday < 0:
        cday = cday + 30
        cmonth = cmonth - 1
    age_days = cday - bday
    # age in months
    if cmonth - bmonth < 0:
        cmonth = cmonth + 12
        cyear = cyear - 1
    age_months = cmonth - bmonth
    # age in years
    age_years = cyear - byear

    return age_days,age_months,age_years

def findPrime(lower,upper):
    count_primes=0
    primes_number=[]
    isPrime = True
    for num in range(lower,upper):
        sqrt_num=int(math.sqrt(num))
        for denom in range(2,sqrt_num+1):
            if num%denom==0:
                isPrime=False
        if isPrime:
            count_primes=count_primes+1
    return count_primes



#driver program
#Function Call
print(calculateAge("17-03-1994"))
#calculateAge("5-06-2000")
# print(findPrime(1,1000))