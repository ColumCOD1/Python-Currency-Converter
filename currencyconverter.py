def main():
    print("This program converts US Dollars to Japanese Yen")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    yen = convert_to_yen(dollars)

    print("This is", yen, "yen.")


convert_to_yen = lambda dollars: dollars * 149.34

main()