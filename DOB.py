def calculate_age(dob):
    from datetime import date

    today = date.today()
    #dob = "12-04-1993"


    # spliting the data into seperate variable and integer
    cday = today.day
    cmonth = today.month
    cyear = today.year

    [bday, bmonth, byear] = dob.split("-")

    # Casting the dates into integers
    bday = int(bday)
    bmonth = int(bmonth)
    byear = int(byear)

    # calculating how much old the user today
    if cyear > byear:
        age_days = (cyear - byear) * 365
        age_months = age_days // 30
        age_year = age_days // 365


    else:
        print("Please Enter Right Year")


    print("You are:\n ", age_days , "days old \n ", age_months, " months old \n ", age_year, " years old \n")

calculate_age("12-04-1993")