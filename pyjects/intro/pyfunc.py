def learn_it1():
    """This is a docstring. When Python generates docs, it looks for a string immediately after the function definition"""
    l1 = [1 ,2, 3, 4]
    print(f"Before work: {l1}")
    # Use pop when we want to work with the removed value. Pop by default pulls the last value but accepts index as optional argument
    l1_n = l1.pop()
    print(f"Popped: {l1_n}")
    print(f"Original: {l1}")
    # Popped using copy from original [:]
    l2_n = l1[:].pop()
    print(f"Popped from original using copy ([:]), only edits the copy - does not change original list: {l2_n}")
    print(f"Original: {l1}")


def learn_it2(*toppings: list):
    """Takes in unknown number of arguments as Tuple, iterates over them"""
    print(f"\nThe following toppings were passed:")
    for topping in toppings:
        print(f"- {topping}")


def learn_it3(fname, lname, **pizza_order):
    """Take 2 positional arguments for the users order, then take all arbitrary information about the pie"""
    pizza_order['first name'] = "Hannah"
    pizza_order['last name'] = "McCullough"
    print(f"\nOrder has the following details:\n {pizza_order}")
    

learn_it1()
learn_it2("pineapple", "pepperoni")
learn_it3("Hannah", "McCullough", size=14, topping1="pineapple", topping2="pepperoni")