from name_tools import format_name


while(True):
    name = input("\n Please enter the first and last name: ")
    if name.lower() == "q":
        print(f"\nBye\n")
        break
    else:
        formatted = name.split(' ')
        print(f"{format_name(formatted[0], formatted[1])}")