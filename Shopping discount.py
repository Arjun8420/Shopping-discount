shoppingAmount = int(input("Enter the shopping amount : "))

if shoppingAmount>1000 :
    discount= 10/100* shoppingAmount
    print("Discount is = %.2f " %discount)
    shoppingAmount -= discount

print("Final Shopping Amount = ", shoppingAmount)
