def eat_junk(food):
    assert food in ["pizza", "ice cream", "burgers", "fries",
                    "bacon", "tortias"], "Food must be a jink food :(!!"
    return f"NON NON NON I'm eating {food.capitalize()}"


food = input("Enter a junk food name please: ")
print(eat_junk(food))
