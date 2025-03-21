print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
_price = 0
if height >= 120:
    print("You can ride the rollercoaster")
    _rider_age = int(input("What is your age? "))
    if _rider_age < 12:
        print("Child price is $5")
        _price = 5
    elif _rider_age < 18:
        print("Teen price is $7")
        _price = 7
    elif _rider_age >= 18:
        print("Adult price is $12")
        _price = 12
    _photo =(input("Do you want a photograph? y/n:\n"))
    if _photo == "y":
        _price += 3
        print('You cost is $' + str(_price))
    else:
        print('You cost is $' + str(_price))
else:
    print("Sorry you have to grow taller before you can ride.")
