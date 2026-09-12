no=int(input("Enter number ="))

op=input("Enter operator you want=")
match op:
    case "+":
        print("Case add")
    case "-":
            print("Case sub")
    case "*":
        print("Case M")
    case "/":
            print("Case d")
    case "//":
        print("Case d floor")
    case "**":
            print("Case power")
    case "%":
        print("Case r")
    case _:
            print("Case default")