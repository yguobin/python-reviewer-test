
def main():
    ask_again = True
    operations_count = 0
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        operations_count += 1
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print(f"You performed {operations_count} operations, bye!")


def perform_division(a,b):
    try:
        return int(a)/int(b)
    except ZeroDivisionError as e:
        return float("NAN")


main()
