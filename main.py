from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
morara = Customer("Kebaso")
platnumz = Customer("Platnumz")
joel = Customer("Joel")
moraa = Customer("Moraa")

# Create coffee types
black_coffee = Coffee("Black Coffee")
white_coffee = Coffee("White Coffee")
iced_coffee = Coffee("Iced Coffee")

# Create orders
order1 = morara.create_order(black_coffee, 5.0)
order2 = joel.create_order(white_coffee, 6.0)
order3 = moraa.create_order(iced_coffee, 5.0)
order5 = joel.create_order(iced_coffee, 6.0)

# Printing data
print(joel.orders())  # List of Joel's orders
print(joel.coffees())  # List of different coffees Joel ordered
print({"coffee": order.coffee.name, "price": order.price} for order in joel.orders())
print(black_coffee.orders())  # List of orders for Black Coffee
