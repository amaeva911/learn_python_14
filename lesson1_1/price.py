def format_price(price):
    price = int(price)
    return f"Цена: {price} руб \"."

test_price = format_price(56.24)
print(test_price)
