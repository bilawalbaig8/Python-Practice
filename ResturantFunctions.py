
PriceList = {
    "Burger" : 550,
    "Pizza" : 3200,
    "Shawarma" : 250,
}

CustomerPaid = 20000

# Test Cases of the Order Placed

Order_01 = ["Pizza", "Pizza", "Burger", "Burger", "Shawarma", "Pizza", "Burger"]
Order_02 = ["Burger", "Shawarma", "Pizza", "Burger"]
Order_03 = ["Burger", "Burger", "Burger", "Burger"]
Order_04 = ["Burger"]
Order_05 = ["Pizza", "Pizza", "Burger", "Burger", "Shawarma", "Pizza", "Burger", "Fries", "Shake"]

Punched_Order = Order_01


def check_items_exist(PriceList, Punched_Order):

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

    return ItemExist , Missingitemstring

def check_order_count(Punched_Order):
    # Counting the Items of order
    Ordered_Items = {}

    for item in Punched_Order:
        if item in Ordered_Items:
            Ordered_Items[item] += 1
        else:
            Ordered_Items[item] = 1

    return Ordered_Items

def calculate_total_cost(Ordered_Items , PriceList):
    # Calculating the Total Cost
    Total_Item_Price = []

    for count_item , Count_value in Ordered_Items.items():
        Total_Item = 0
        for Price_item , Price_value in PriceList.items():
            if count_item == Price_item:
                Cost = Count_value * Price_value
                Total_Item_Price.append(Cost)


    TotalCost = sum(Total_Item_Price)

    return TotalCost

def calculate_discount(TotalCost):
    # if Order is more than 2000 Customer gets discount
    DiscountLimit = 2000

    # Discount amount is 10%
    DiscountPercentage = 10

    # Calculating the Discount amount

    if TotalCost > DiscountLimit:
        Discount_Amount = (TotalCost * DiscountPercentage) / 100
        #print(Discount_Amount)
        GrandTotal = TotalCost - Discount_Amount
        #print(GrandTotal)

    else:
        Discount_Amount = 0
        GrandTotal = TotalCost - Discount_Amount

    return GrandTotal , Discount_Amount

def checking_customer_balance(CustomerPaid, GrandTotal, Ordered_Items):

# Calculating the balance
    Balance = 0
    if CustomerPaid >= GrandTotal:
        Balance = CustomerPaid - GrandTotal
        #print(Balance)

# Calculation for Outputs

    ItemOrdered = ''
    for item, quantity in Ordered_Items.items():
        ItemOrdered += f"{item} : {quantity} , "

    return  Balance , ItemOrdered

def billing_format(ItemExist, Missingitemstring, Ordered_Items, TotalCost, GrandTotal, Discount_Amount, Balance, ItemOrdered):
    print("\nSummary: \n"
          "     You ordered : \n"
          "               " + str(ItemOrdered) +
          "\n\n     Total price : Rs." + str(TotalCost) +
          "\n     Discount : Rs." + str(Discount_Amount) +
          "\n     Grand total : Rs." + str(GrandTotal) +
          "\n     Customer Paid : Rs." + str(CustomerPaid) +
          "\n     Balance : Rs." + str(Balance) + "\n"
                                                  "\n(Thanking you for visiting ABC Fast Food Point, we hope to see you again)")

ItemExist , Missingitemstring = check_items_exist(PriceList, Punched_Order)
Ordered_Items = check_order_count(Punched_Order)
TotalCost =  calculate_total_cost(Ordered_Items , PriceList)
GrandTotal , Discount_Amount = calculate_discount(TotalCost)
Balance , ItemOrdered = checking_customer_balance(CustomerPaid, GrandTotal, Ordered_Items)


if ItemExist == False:
    print("Sorry, We dont have \n" +
          "         \n" + Missingitemstring + "\n\nRight Now! \n"
                                              "Please Revise you Order")
else:
    if ItemExist == True and CustomerPaid > GrandTotal:
        billing_format(ItemExist, Missingitemstring, Ordered_Items, TotalCost, GrandTotal, Discount_Amount, Balance,
                       ItemOrdered)

    else:

        print("\n     Grand total : Rs." + str(GrandTotal) +
                      "\n Your Paid Amount of Rs." + str(CustomerPaid) + " is Insufficient for this Order")
