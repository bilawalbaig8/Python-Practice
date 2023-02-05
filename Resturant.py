'''

Nested if
Please choose the following items:
1.	Burger 		550
a.	If price exceed 2000
b.	Then give him / her winter discount of 10%

Summary
You ordered : 5 burger
Total price 2750
Discount: 275
Grand total: 2500
Customer Paid: 5000
Balance: 2500
(Thanking you for visiting ABC Fast Food Point, we hope to see you again)

2.	Pizza			3200
Summary
You ordered : 5 burger
Total price 2750
Discount: 275
Grand total: 2500
Customer Paid: 5000
Balance: 2500
(Thanking you for visiting ABC Fast Food Point, we hope to see you again)

'''

PriceList = {
    "Burger" : 550,
    "Pizza" : 3200,
    "Shawarma" : 250,
}

# if Order is more than 2000 Customer gets discount
DiscountLimit = 2000

# Discount amount is 10%
DiscountPercentage = 10

CustomerPaid = 4095

# Test Cases of the Order Placed

Order_01 = ["Pizza", "Pizza", "Burger", "Burger", "Shawarma", "Pizza", "Burger"]
Order_02 = ["Burger", "Shawarma", "Pizza", "Burger"]
Order_03 = ["Burger", "Burger", "Burger", "Burger"]
Order_04 = ["Burger"]
Order_05 = ["Pizza", "Pizza", "Burger", "Burger", "Shawarma", "Pizza", "Burger", "Fries", "Shake"]

Punched_Order = Order_01

# Checking if any of the order item Exists or not
ItemExist = True
Missing_Item = []

for item in Punched_Order:
    if item not in PriceList:
        ItemExist = False
        Missing_Item.append(item)
        #print(str(Missing_Item))

# Calculation for Outputs pf missing items
Missingitemstring = ''
for i in Missing_Item:
    Missingitemstring += f"{i} , "

# Main Code if all the ordered Items are Exists
if ItemExist == True:

# Counting the Items of order
    Ordered_Items = {}

    for item in Punched_Order:
        if item in Ordered_Items:
            Ordered_Items[item] += 1
        else:
            Ordered_Items[item] = 1

    #print(Ordered_Items)

# Calculating the Total Cost
    Total_Item_Price = []


    for count_item , Count_value in Ordered_Items.items():
        Total_Item = 0
        for Price_item , Price_value in PriceList.items():
            if count_item == Price_item:
                Cost = Count_value * Price_value
                Total_Item_Price.append(Cost)


    TotalCost = sum(Total_Item_Price)
    #print(TotalCost)

    DiscountedAmount = 0
    GrandTotal = 0
    Balance = 0

    #print(TotalCost)

# Calculating the Discount amount

    if TotalCost > DiscountLimit:
        Discount_Amount = (TotalCost * DiscountPercentage) / 100
        #print(Discount_Amount)
        GrandTotal = TotalCost - Discount_Amount
        #print(GrandTotal)

    else:
        Discount_Amount = 0
        GrandTotal = TotalCost - Discount_Amount

# Calculating the balance


    if CustomerPaid >= GrandTotal:
        Balance = CustomerPaid - GrandTotal
        #print(Balance)
        # Calculation for Outputs

        ItemOrdered = ''
        for item, quantity in Ordered_Items.items():
            ItemOrdered += f"{item} : {quantity} , "

        print("\n Summary: \n"
              "\n     You ordered : \n"
              "               " + str(ItemOrdered) +
              "\n     Total price : " + str(TotalCost) +
              "\n     Discount : " + str(Discount_Amount) +
              "\n     Grand total : " + str(GrandTotal) +
              "\n     Customer Paid : " + str(CustomerPaid) +
              "\n     Balance : " + str(Balance) + "\n"
              "\n(Thanking you for visiting ABC Fast Food Point, we hope to see you again)")


    else:
        print("\n     Grand total : " + str(GrandTotal) +
              "\n Your Paid Amount is Insufficient")



else:
    print("Sorry, We dont have \n" +
          "         \n" + Missingitemstring + "\n\nRight Now! \n"
          "Please Revise you Order")

