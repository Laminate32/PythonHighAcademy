Price_of_buy = int(input("Input ur price of your products(UAH):"))
if Price_of_buy >= 1000:
    print("Ваша знижка 10%")
elif Price_of_buy >= 500:
    print("Ваша знижка 5%")
else:
    print("Нема знижки((")