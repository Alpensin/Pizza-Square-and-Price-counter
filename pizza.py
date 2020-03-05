import math

def pizza_size_and_price(diameter, price: int, currency='$'):
    '''
    Enter pizza diameter and price as int (price*100)
    Returns square of pizza and price of 1cm**2
    Example
    pizza_size_and_price(32, 600)
    pizza_size_and_price(45, 900, 'rub.')
    '''
    pizza_square = math.pi*(diameter/2)**2
    sm2_price = price/pizza_square
    print(f'Pizza square: {round(pizza_square,2)} cm^2, Price for cm^2 {round(sm2_price,2)} {currency}')

    return pizza_square, sm2_price
