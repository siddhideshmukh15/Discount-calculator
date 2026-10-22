print("==== Discount Calculator====")
price=float(input("Entre original price:,rs"))
discount=float(input("Enter discount percentage:"))

if price>=0 and 0<=discount <=100:
    savings=price*discount/100
    final_price=price-savings
    print("Discount Amount: rs",round(savings,2))
    print("Final price:rs",round(final_price,2))

else:
    print("please enter a valid price and discount!")